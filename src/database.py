import mysql.connector
import yaml
import numpy as np
from datetime import datetime
import pandas as pd


# nastavenie pripojenia k db podla configu
def getDbConnection():
    with open('config.yaml') as f:
        config = yaml.safe_load(f)

    database = config['database']

    cnx = mysql.connector.connect(**database)

    return cnx


# nacitanie dat z databazy do numpy pola
def getFontData():
    cnx = getDbConnection();
    cursor = cnx.cursor()

    query = ("SELECT f.font_id,a.question_id,a.numeric_value FROM font_answer f JOIN answer a ON a.answer_id = f.answer_id")
    cursor.execute(query)

    touples = cursor.fetchall();

    result = {};
    for fid,qid,value in touples:
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
    pd.DataFrame(data).to_csv("data/answers-" +datetime.now().strftime("%m-%d-%Y::%H:%M:%S") +".csv")

