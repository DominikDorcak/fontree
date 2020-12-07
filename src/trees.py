
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




def drawGraph(clf, Y):
    dot_data = open("trees.dot","w+")
    export_graphviz(clf, out_file=dot_data,
                    filled=True, rounded=True,
                    special_characters=True, class_names=[str(x) for x in Y])
    dot_data.close()
    dot_data = open("trees.dot","r")
    graph = pydotplus.graph_from_dot_data(dot_data.read())
    graph.write_png('tree.png')
    Image(graph.create_png())
