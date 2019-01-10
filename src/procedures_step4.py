# -*- coding: utf-8 -*-
"""
All procedures to do the fourt step that is: Create a new Train and Test files.\n
Note: Only the last function is necessary of external call, since the others are used within.\n
"""
import csv
import random
from random import seed
from random import randrange
import procedures_step3 as p3


def loadDatasetList(filename):
    """
    Load a file dataSet in to a list\n
    Return a list split, with each attribute in one position\n

    Keyword arguments:\n
        filename (string) : Full or relative string name with file path.\n
    Returns:\n
        (list) : List with full dataSet in it
    """
    dataSet = []
    with open(filename, 'r') as csvfile:
        data = csv.reader(csvfile)
        for line in data:
            dataSet.append(line)
    return dataSet


def splitInKFolds(fileName, folds, randomSeed):
    """
    Split a dataSet into k folds smalls datasets\n
    Ensure that there will be at least one of each class in the training and test set

    Keyword arguments:\n
        filename (string) : Full or relative string name with file path.\n
        folds (int): K folds for split dataSet.\n
        randomSeed (int or float): seed for the random picker.\n
    Returns:\n
        (list) : List with full dataSet in it, splited in k folds.
    """
    class_ = p3.getClasses(fileName)
    dataSet = loadDatasetList(fileName)  # Load a file dataSet in to a list
    random.seed(randomSeed)
    dataSet_split = list()  # New temporary list, will be the output
    dataSet_copy = list(dataSet)  # Copy the old list
    # Receive the size that each part must have from the total of the list,
    fold_size = int(len(dataSet) / folds)
    for i in range(folds):  # For each part
        flag = True
        fold = list()  # New temporary list, for the current part.
        while len(fold) < fold_size:  # While the size of the list is not the size it should have.
            # Make sure that will have at least one of each class on each dataSet part.
            while flag == True:
                for x in range(len(dataSet_copy)):  # For each instance on the dataSet.
                    for y in range(len(class_)):  # For each class in the class list.
                        # If its they have the same class.
                        if dataSet_copy[x][-1] == class_[y][-1]:
                            # Add to the list and removes the index passed to the list,
                            # ensuring that it does not repeat the item again.
                            fold.append(dataSet_copy.pop(x))
                    if y == (len(class_)-1): # If all class have been copy, flag to exit.
                        flag = False
            # Gets a random element from the list.
            index = randrange(len(dataSet_copy))
            # Add to the list and removes the index passed to the list,
            # ensuring that it does not repeat the item again.
            fold.append(dataSet_copy.pop(index))
        # Adds the list of the current k part to the return list.
        dataSet_split.append(fold)
    return dataSet_split


def crossValidationSplit(dataSetName,fileName, folds, randomSeed, outputPath):
    """
    Creates trainning and test files for the current dataSet\n
    Doesn`t return anything because all operations are made by creating new files.\n
    Trainning with size of folds-1\n
    Test with size of 1.\n

    Keyword arguments:\n
        dataSetName (string): String with file name of dataSet\n
        filename (string): Full or relative string name with file path.\n
        folds (int): K folds for split dataSet.\n
        randomSeed (int or float): seed for the random picker.\n
        outputPath (string): Path for the output folder.\n
    """
    for i in range(folds):  # For each test/train set.
        trainDataSet = []  # Final train data set.
        testDataSet = []  # Final test data set.
        # Open/Create the output for each dataSet.
        trainOutput = open(outputPath+dataSetName +
                           ".train."+str(i)+".arff", "w")
        testOutput = open(outputPath+dataSetName+".test."+str(i)+".arff", "w")
        # Set the pointer to the beginning of each file.
        testOutput.seek(0)
        trainOutput.seek(0)
        # Split a dataSet into k folds smalls datasets.
        dataSet = splitInKFolds(fileName, folds, randomSeed)
        # Take one k part for test and other k parts for training.
        for j in range(len(dataSet)):  # For the dataSet size.
            if (j == i):  # If the current part is the test part.
                # For each instance of this dataSet.
                for n in range(len(dataSet[j])):
                    # A new instance will be added to the list of the current test set.
                    testDataSet.append(dataSet[j][n])
            # If it is not the test set, the part will be added to the training set.
            else:
                for n in range(len(dataSet[j])):
                    trainDataSet.append(dataSet[j][n])
        # Write on file the output results.
        trainOutput.write(str(trainDataSet).replace("[", "").replace(
            "],", "'\n").replace("'", "").replace(" ", "")+"\n")
        testOutput.write(str(testDataSet).replace(
            "[", "").replace("],", "'\n").replace("'", "").replace(" ", "")+"\n")

def crossValidationSplitDataSets(dataSetsNames_, path_, folds, randomSeed, outputPath):
    """
    Creates trainning and test files for each dataSet\n
    Doesn`t return anything because all operations are made by creating new files.\n
    Trainning with size of folds-1\n
    Test with size of 1.\n

    Keyword arguments:\n
        dataSetsNames_ (list[string]):  list of all datasets in path folder.\n
        path_ (string) :  path of datasets folder.\n
        outputPath (string) : path for the output folder of each dataset.\n
    """
    for dataSet in dataSetsNames_:  # For each dataset in the list.
        print(dataSet)                
        fileName = path_ + dataSet
        crossValidationSplit(dataSet,fileName,folds,randomSeed,outputPath)