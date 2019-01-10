# -*- coding: utf-8 -*-
""" All procedures to do the third step that is: replace missing values.\n
Given an attribute F containing a missing value associated with class Cj,
this missing value will be replaced by the average of all known values of F associated with class Cj.
Note: Only the last function is necessary of external call, since the others are used within.
"""
from shutil import copyfile


def getClasses(fileName):
    """
    Creates a list of all classes of the file\n

    Keyword arguments:\n
        filename (string) : Full or relative string name with file path.
    Returns:\n
        (list) : List with all classes, sorted and unique.
    """
    classList = []  # List with all class names
    file_ = open(fileName, "r")  # Associate file to variable.
    data = file_.readlines()  # Read all lines of file.
    file_.close()  # Close input file.
    for line in data:  # For each line on data file.
        # .strip() # Remove \n from and of line.
        # Creates a list with all atributes of the instance by divided wiht .split(",")
        # The last atribute is the classe. [-1]
        c = line.strip().split(",")[-1]
        classList.append(c)
    return sorted(set(classList))


def split_list(list_, n):
    """
    Split the list into n sub-lists every time it arrives at the counter "n".\n

    Keyword arguments:\n
        list_ (list) : Common list.\n
        n (int) : Delimiter of each list.\n
    Return (yield):\n
        (list) : "n" sub-lists of the main list .
    """
    for i in range(0, len(list_), n):
        yield list_[i:i + n]


def masterClass(fileName):
    """
    Create master instance for each class.\n
    In her, every attribute, is the average of her classe.\n

    Keyword arguments:\n
        filename (string) : Full or relative string name with file path.\n
    Returns:\n
        (list) : List with all classes and average attributes.
    """
    # List with all class names
    classList = getClasses(fileName)
    # First list, with all classes, used to start values on list.
    masterInstance = []
    # Final list, splited lists, with real (average) values.
    masterInstance_ = []

    file_ = open(fileName, "r")  # Associate file to variable.
    data = file_.readlines()  # Read all lines of file.
    file_.close()  # Close input file.

    # Creates a empty instance for each class.
    # Ex: [0,0,...,0,0,"01/01/01"]
    size_ = len(data[1].strip().split(","))  # Get attribute lenght.
    for i in range(len(classList)):  # For each class on list.
        for j in range(size_):  # For each atributte on instance.
            if j == size_-1:  # If is the last attribute,it`s the class.
                masterInstance.extend([classList[i]])
            else:  # Else, it`s an attribute, then assign 0.
                masterInstance.extend([0.0])

    # Split the list (masterInstance) into n sub-lists every time it arrives at the counter (size_).
    masterInstance_ = list(split_list(masterInstance, size_))

    # Finally, creates the master class for each class.
    # Atributes value are the average of each one per class.
    for i in range(len(masterInstance_)):  # For each master instance.
        count = 0  # Start a count for division.
        for line in data:  # For each line on the data file.
            instance = line.strip().split(",")  # Get the instance.
            # If the class of the instance is the current masterInstance class.
            if instance[-1] == masterInstance_[i][-1]:
                count += 1  # Add 1 to the division counter.
                # For each attribute, unless the class (thats why -1).
                for j in range(len(instance)-1):
                    if instance[j] != "?":  # If the attibute has a value.
                        # Add with the previous value, and divide, obtaining the partial average each time.
                        masterInstance_[i][j] = (
                            float(masterInstance_[i][j]) + float(instance[j])) / count

    # Round numbers to "decimal" digits.
    decimal = 3
    for i in range(len(masterInstance_)):
        for j in range(len(masterInstance_[i])-1):
            masterInstance_[i][j] = round(masterInstance_[i][j], decimal)

    # Return the list with all master instances.
    return masterInstance_


def replaceMissingValues(fileName):
    """
    Replace all missing values with the master class value.\n
    Doesn`t return anything because all operations are made in the file.\n

    Keyword arguments:\n
        filename (string) : Full or relative string name with file path.        
    """
    masterClasses = masterClass(fileName)
    file_ = open(fileName, "r+")  # Associate file to variable.
    data = file_.readlines()  # Read all lines of file.
    file_.seek(0)  # Set the pointer to the beginning of file.

    for line in data:  # For each line on the file.
        outputLine = []  # Final Output Line.
        # Split each line to create a list of attributes.
        attribute = line.strip().split(",")
        for j in range(len(attribute)):  # For each attribute on the line.
            if attribute[j] == "?":  # If is missing the value.
                for k in masterClasses:  # Seach the class in the master classes list.
                    if attribute[-1] == k[-1]:  # When find.
                        # Replace the missing value with the master value.
                        outputLine.append(k[j])
            else:  # If is a normal value.
                outputLine.append(attribute[j])  # Keep the line value.
        # Write the output line, replacing the characters of the list.
        file_.write(str(outputLine).replace(
            "[", "").replace("]", "").replace("'", "").replace(" ","")+"\n")

    file_.truncate()  # Truncate remaining file.
    file_.close()  # Finally, close the file.


def replaceMissingValuesDataSets(dataSetsNames_, path_, outputPath):
    """
    Replace all missing values on each dataset\n
    Doesn`t return anything, but create a new file in the outputPath location with the result.\n
    For more info, ready all the class.\n

    Keyword arguments:\n
        dataSetsNames_ (list[string]):  list of all datasets in path folder.\n
        path_ (string) :  path of datasets folder.\n
        outputPath (string) : path for the output folder of each dataset.\n
    """
    for dataSet in dataSetsNames_:  # For each dataset in the list.
        print(dataSet)
        src = path_ + dataSet  # Input full file name.
        fileName = outputPath + dataSet
        # Create a copy of the old dataset to work in it.
        copyfile(src, fileName)
        # Replace all missing values of the current dataset
        replaceMissingValues(fileName)
