# -*- coding: utf-8 -*-
""" All procedures to do the first step that is: join test + train + valid to one single file.\n
Note: Only the last function is necessary of external call, since the others are used within.
"""


def clearFile(filename):
    """ 
    Removes all blank and metadata lines.\n
    Doesn`t return anything because all operations are made in the file.\n

    Keyword arguments:\n
        filename (string) : Full or relative string name with file path.
    """
    file_ = open(filename, "r+")  # Associate file to variable.
    data = file_.readlines()  # Read all lines of file.
    file_.seek(0)  # Set the pointer to the beginning of file.
    for line in data:  # For each line on data.
        # If its not in blak and not a meta.
        if not line.isspace() and not line.startswith('@'):
            file_.write(line)  # Rewrite that line on file.
    file_.truncate()  # Truncate remaining file.
    file_.close()  # Finally, close the file


def joinFiles(train_, valid_, test_, full_):
    """
    Join train, valid and test files to create one full file.\n
    Doesn`t return anything, but create a new file in the full_ location with the result.\n
    All Keyword arguments are full or relative strings name with file path.\n  

    Keyword arguments:\n
        train_ (string) : .train.arff database, string name.\n
        valid_ (string) : .valid.arff database, string name.\n
        test_ (string) : .test.arff database, string name.\n
        full_ (string) : the result database, string name.\n 
    """
    list_ = [train_, valid_, test_]  # Create a list with files names.
    all_ = ""  # String must be initialize, before it uses +=.
    for file_ in list_:  # For each file in the list of files.
        # Ensure that all blank and metadata lines are removed.
        clearFile(file_)
    for file_ in list_:  # For each file in the list of files.
        f = open(file_, "r")  # Open and associate file to variable.
        data = f.read()  # Read all file.
        all_ += data  # Add file content to one single string.
        f.close()  # Close that file.
    # Open the output file and associate file to variable.
    file_ = open(full_, "w")
    file_.write(all_)  # Write the result.
    file_.close()  # Close output file


def createFullDataSets(dataSetsNames_, path_, pathFull_):
    """
    Creates a full dataset for each one in the path.\n
    Doesn`t return anything, but create a new file in the full_ location with the result.\n

    Keyword arguments:\n
        dataSetsNames_ (list[string]):  list of all datasets in path folder.
        path_ (string) :  path of datasets folder.
        pathFull_ (string) : path for the output of each dataset.
    """
    for dataSet in dataSetsNames_:  # For each dataset in the list
        print(dataSet)
        # Create a full path string, by adding path + dataset + end of file name of each string.
        test = path_ + dataSet + ".test.arff"
        train = path_ + dataSet + ".train.arff"
        valid = path_ + dataSet + ".valid.arff"
        full = pathFull_ + dataSet + ".full.arff"
        # Join train, valid and test files to create one full file.
        joinFiles(train, valid, test, full)
