
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier, export_graphviz

from IPython.display import Image
import pydotplus

def createTreeClasifier(dataArr):
    data = pd.DataFrame(dataArr)
    Y = data[0]
    X = data[range(1,22)]
    clf = DecisionTreeClassifier()
    clf.fit(X,Y)
    pred = clf.predict(X)

    print("Accuracy:", metrics.accuracy_score(Y,pred))
    drawGraph(clf,Y)


def loadFontMap(filePath):
    file = open(filePath)
    lines = file.readlines()
    file.close()
    d = {}
    for l in lines:
        space = l.find(' ')
        id = int(l[:space])
        name = l[space+1:len(l)-1]
        d[id] = name
    return d


def drawFromCSV(filename):
    data = pd.read_csv(filename)
    Y = data['0']
    xheaders = [str(x) for x in range(1, 22)]
    X = data[xheaders]
    clf = DecisionTreeClassifier()
    clf.fit(X, Y)
    pred = clf.predict(X)

    print("Accuracy:", metrics.accuracy_score(Y, pred))
    drawGraph(clf, Y)


def drawFromCSVSmall(filename):
    data = pd.read_csv(filename)
    Y = data['0']
    xheaders = [str(x) for x in range(1, 11)]
    X = data[xheaders]
    clf = DecisionTreeClassifier()
    clf.fit(X.head(10), Y.head(10))
    pred = clf.predict(X.head(10))

    print("Accuracy:", metrics.accuracy_score(Y.head(10), pred))
    drawGraph(clf, Y,"smallTree.png")


def drawGraph(clf, Y, imageName="tree.png"):
    dot_data = open("trees.dot","w+")
    fontmap = loadFontMap('data/fonts.txt')
    export_graphviz(clf, out_file=dot_data,
                    filled=True, rounded=True,
                    special_characters=True, class_names=[fontmap[x] for x in Y])
    dot_data.close()
    dot_data = open("trees.dot","r")
    graph = pydotplus.graph_from_dot_data(dot_data.read())
    graph.write_png(imageName)
    Image(graph.create_png())
