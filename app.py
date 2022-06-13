# This is a sample Python script.
import sklearn

import src.database as database
import src.trees as trees
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.api.trees.DBNode import DBNode


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # trees.createTreeClasifier(database.getFontData())
    # database.saveDataCSV();
    # database.saveMaps();


    trees.drawFromCSV("data/answers-06-11-2022::19:20:36.csv")
    trees.drawFromCSVSmall("data/answers-06-11-2022::19:20:36.csv")
    #database.restoreQuestionAnswers("data/answers-12-14-2020__15_07_44.csv")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
