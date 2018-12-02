# -*- coding: utf-8 -*-
""" All procedures to do the second step that is: transform datasets multi-label to single-label.\n
Note: Only the last function is necessary of external call, since the others are used within.
"""
import operator
from shutil import copyfile


def getClasses(fileName):
    """
    Collects all classes that appear in a file.\n
    Return a dictionary with classes that appear more than 10 times.\n

    Keyword arguments:\n
        filename (string) : Full or relative string name with file path.\n

    Returns:\n
        (Dictionary) : Dictionary with classes that appear more than 10 times.    
    """
    classCount = {}  # Dictionary to make the class count.
    file_ = open(fileName, "r")  # Associate file to variable.
    data = file_.readlines()  # Read all lines of file.
    file_.close()  # Close input file.
    for line in data:  # For each line on data file.
        # .strip() # Remove \n from and of line.
        # Creates a list with all atributes of the instance by divided wiht .split(",")
        # The last atribute are the classes. [-1]
        # Creates a list with all classes of the instance by divided wiht .split("@")
        classes = line.strip().split(",")[-1].split("@")
        # Count how many times each class appears
        for c in classes:  # For each class
            if c in classCount:
                # Add 1 to the counter if that class alredy existes.
                classCount[c] += 1
            else:
                # Or creates a new key if it`s a new class.
                classCount[c] = 1
    # After counting, delete items they appear less than 10 times on dataset.
    for item in list(classCount.keys()):
        if classCount[item] < 10:
            del classCount[item]
    # Lastly, return the sorted items.
    return dict(sorted(classCount.items(), key=operator.itemgetter(1), reverse=True))


def convertToSingleLabel(fileName):
    """
    Convert class of the instances from multi label to single label.\n
    Doesn`t return anything because all operations are made in the file.\n

    Keyword arguments:\n
        filename (string) : Full or relative string name with file path.\n
    """
    classCount = getClasses(fileName)  # Collects all classes on the file.
    file_ = open(fileName, "r+")  # Associate file to variable.
    data = file_.readlines()  # Read all lines of file.
    file_.seek(0)  # Set the pointer to the beginning of file.

    for line in data:  # For each line on data.
        # Get the current multilabel class
        oldClasses = line.strip().split(",")[-1]
        # Split in a list of single labels class.
        classes_ = oldClasses.split("@")
        classValue = 0  # Aux to class num value.
        classKey = ""  # Aux to class num key.
        deleteFlag = False  # Used to check if its a line to delete or not.
        for c in classes_:  # For each class in the list of single label classes.
            if c in classCount:  # If that class is on the list.
                deleteFlag = False  # Do not flag to delete that line.
                if classCount[c] > classValue:  # If it`s the most count class.
                    classKey = c  # Save that key.
            else:
                deleteFlag = True  # Flag to delete that line.
        if deleteFlag:  # If its a line to delete, write nothing on it.
            file_.write("")
        else:
            # Rewrite that line on file, replacing the multilabel for the correct single label.
            file_.write(line.replace(oldClasses, classKey))
    file_.truncate()  # Truncate remaining file.
    file_.close()  # Finally, close the file.


def convertToSingleLabelDataSets(dataSetsNames_, path_, pathSingleLabel_):
    """
    Convert a full multilabel dataset in single label dataset\n
    Doesn`t return anything, but create a new file in the pathSingleLabel_ location with the result.\n
    For more info, ready all the class.\n

    Keyword arguments:\n
        dataSetsNames_ (list[string]):  list of all datasets in path folder.
        path_ (string) :  path of datasets folder.
        pathSingleLabel_ (string) : path for the output of each dataset.
    """
    for dataSet in dataSetsNames_:  # For each dataset in the list.
        src = path_ + dataSet  # Input full file name.
        fileName = pathSingleLabel_ + dataSet
        # Create a copy of the old dataset to work in it.
        copyfile(src, fileName)
        # Convert class of the instances from multi label to single label.\n
        convertToSingleLabel(fileName)
