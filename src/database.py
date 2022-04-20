import psycopg2
import yaml
import numpy as np
from datetime import datetime
import pandas as pd
import csv

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

from . import config

cnx = None

# nastavenie pripojenia k db podla configu
def getDbConnection():
    global cnx
    if cnx is None:
        cfg = yaml.safe_load(pkg_resources.read_text(config,'config.yaml'))
        db = cfg['database']
        cnx = psycopg2.connect(host=db['host'],database=db['database'],user=db['user'],password=db['password'])
    return cnx


# nacitanie dat z databazy do numpy pola
def getFontData():
    cnx = getDbConnection();
    cursor = cnx.cursor()

    query = (
        "SELECT f.font_id,a.question_id,a.numeric_value FROM font_answer f JOIN answer a ON a.answer_id = f.answer_id")
    cursor.execute(query)

    touples = cursor.fetchall();

    result = {};
    for fid, qid, value in touples:
        if not (fid in result.keys()):
            result[fid] = [None for x in range(22)]
            result[fid][0] = fid
        result[fid][qid] = value
    # for (id,name) in cursor:
    #     print(name)

    return np.array([result[x] for x in result.keys()]);


# ulozenie dat do csv filu
def saveDataCSV():
    data = getFontData()
    # np.savetxt("data/answers-" +datetime.now().strftime("%m-%d-%Y::%H:%M:%S") +".csv", data, delimiter=",")
    pd.DataFrame(data).to_csv("data/answers-" + datetime.now().strftime("%m-%d-%Y::%H:%M:%S") + ".csv")


def fontMap():
    cnx = getDbConnection();
    cursor = cnx.cursor()

    query = (
        "SELECT f.font_id,f.name FROM font f")
    cursor.execute(query)

    touples = cursor.fetchall()
    return touples


def questionMap():
    cnx = getDbConnection();
    cursor = cnx.cursor()

    query = (
        "SELECT q.question_id,q.text FROM question q")
    cursor.execute(query)

    touples = cursor.fetchall()
    return touples

def answerMap():
    cnx = getDbConnection();
    cursor = cnx.cursor()

    query = (
        "SELECT a.answer_id,a.question_id,a.numeric_value FROM answer a")
    cursor.execute(query)

    touples = cursor.fetchall()

    question_answer_map = {}

    for aid,qid,v in touples:
        if question_answer_map.keys().__contains__(qid):
            question_answer_map[qid][v] = aid
        else:
            question_answer_map[qid] = {v:aid}

    return question_answer_map

def saveMaps():
    questions = questionMap()
    with open('data/questions.txt', 'w') as fp:
        fp.write('\n'.join('%s %s' % x for x in questions))
    fonts = fontMap()
    with open('data/fonts.txt', 'w') as fp:
        fp.write('\n'.join('%s %s' % x for x in fonts))


def restoreFonts():
    cnx = getDbConnection()
    cursor = cnx.cursor()
    sql = "INSERT INTO font (font_id,name) VALUES (%s,%s)"

    with open('data/fonts.txt','r') as fonts:
        lines = fonts.readlines()
        for l in lines:
            touple = l.split(' ',1)
            cursor.execute(sql,(touple[0],touple[1].strip()))

    cnx.commit()
    print("Rekonstrukcia db: fonty zapisane");

def restoreQuestionAnswers(answers_csv):
    answers_map = answerMap()
    cnx = getDbConnection()
    cursor = cnx.cursor()

    sql = "INSERT INTO font_answer (font_id,answer_id) VALUES (%s,%s)"

    with open(answers_csv,'r') as answers:
        answers_reader = csv.reader(answers,delimiter=',')
        for row in answers_reader:
            if not row[0] == '':
                for qid in range(2,len(row)):
                    cursor.execute(sql,(row[1],answers_map[qid-1][int(row[qid])]))
                    #print(row[1],answers_map[qid-1][int(row[qid])])

    cnx.commit()
    print("Rekonstrukcia DB: odpovede zapisane")



