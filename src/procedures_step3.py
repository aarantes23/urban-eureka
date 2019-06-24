from shutil import copyfile
""" All procedures to do the third step that is: Replace no-numeric attributes.\n
Note: Only the last function is necessary of external call, since the others are used within.
"""

def replaceNoNumericAttributes(fileName):
    """
    Each database has its own peculiarity. Therefore, each has its own specific method.
    Doesn`t return anything because all operations are made in the file.\n

    Keyword arguments:\n
        filename (string) : Full or relative string name with file path.\n
    """
    if ("church" in fileName):
        _church(fileName)
    if ("expr" in fileName):
        _expr(fileName)
    if ("pheno" in fileName):
        _pheno(fileName)
    if ("seq" in fileName):
        _seq(fileName)
    if ("spo" in fileName):
        _spo(fileName)


def _church(fileName):
    """
    Replace Column 0 {A,B,C,D,A-D} by {0,1,2,3}
    Doesn`t return anything because all operations are made in the file.\n

    Keyword arguments:\n
        filename (string) : Full or relative string name with file path.\n
    """
    file_ = open(fileName, "r+")  # Associate file to variable.
    data = file_.readlines()  # Read all lines of file.
    file_.seek(0)  # Set the pointer to the beginning of file.
    x = 0  # Column id
    newValues = [0, 1, 2, 3]  # New values

    for line in data:  # For each line on data.
        outputLine = []  # Final Output Line.
        coluns = line.split(",")
        if (coluns[x] == "A"):
            coluns[x] = newValues[0]
        elif (coluns[x] == "B"):
            coluns[x] = newValues[1]
        elif (coluns[x] == "C"):
            coluns[x] = newValues[2]
        else:
            coluns[x] = newValues[3]
        # Save the output line
        outputLine.append(coluns)
        # Write the output line, replacing the characters of the list.
        file_.write(str(outputLine).replace(
            "[", "").replace("]", "").replace("'", "").replace(" ", "")+"\n")

    file_.truncate()  # Truncate remaining file.
    file_.close()  # Finally, close the file


def _expr(fileName):
    """
    Replace Column 77 {A,B,C,D,A-D} by {0,1,2,3}
    Replace Column 549 and 550 {no,yes} by {0,1}
    Doesn`t return anything because all operations are made in the file.\n

    Keyword arguments:\n
        filename (string) : Full or relative string name with file path.\n
    """    
    file_ = open(fileName, "r+")  # Associate file to variable.
    data = file_.readlines()  # Read all lines of file.
    file_.seek(0)  # Set the pointer to the beginning of file.
    columnId = [77, 549, 550]  # Columns ids
    newValues = [0, 1, 2, 3, 4]  # New values

    for line in data:  # For each line on data.
        outputLine = []  # Final Output Line.
        coluns = line.split(",")
        # Replace Column 77 {A,B,C,D,A-D} by {0,1,2,3}
        if (coluns[columnId[0]] == "A"):
            coluns[columnId[0]] = newValues[0]
        elif (coluns[columnId[0]] == "B"):
            coluns[columnId[0]] = newValues[1]
        elif (coluns[columnId[0]] == "C"):
            coluns[columnId[0]] = newValues[2]
        elif (coluns[columnId[0]] == "D"):
            coluns[columnId[0]] = newValues[3]
        elif (coluns[columnId[0]] == "A-D"):
            coluns[columnId[0]] = newValues[4]
        # Replace Column 549 {no,yes} by {0,1}
        if (coluns[columnId[1]] == "no"):
            coluns[columnId[1]] = newValues[0]
        elif (coluns[columnId[1]] == "yes"):
            coluns[columnId[1]] = newValues[1]
        # Replace Column 550 {no,yes} by {0,1}
        if (coluns[columnId[2]] == "no"):
            coluns[columnId[2]] = newValues[0]
        elif (coluns[columnId[2]] == "yes"):
            coluns[columnId[2]] = newValues[1]
        # Save the output line
        outputLine.append(coluns)
        # Write the output line, replacing the characters of the list.
        file_.write(str(outputLine).replace(
            "[", "").replace("]", "").replace("'", "").replace(" ", "")+"\n")

    file_.truncate()  # Truncate remaining file.
    file_.close()  # Finally, close the file


def _pheno(fileName):
    """
    Replace all Columns {w,n,s,r} by {0,1,2,3}
    Doesn`t return anything because all operations are made in the file.\n

    Keyword arguments:\n
        filename (string) : Full or relative string name with file path.\n
    """    
    file_ = open(fileName, "r+")  # Associate file to variable.
    data = file_.readlines()  # Read all lines of file.
    file_.seek(0)  # Set the pointer to the beginning of file.
    newValues = [0, 1, 2, 3]  # New values

    for line in data:  # For each line on data.
        outputLine = []  # Final Output Line.
        coluns = line.split(",")
        for i in range(len(coluns)-1):
            if (coluns[i] == "w"):
                coluns[i] = newValues[0]
            elif (coluns[i] == "n"):
                coluns[i] = newValues[1]
            elif (coluns[i] == "s"):
                coluns[i] = newValues[2]
            elif (coluns[i] == "r"):
                coluns[i] = newValues[3]
        # Save the output line
        outputLine.append(coluns)
        # Write the output line, replacing the characters of the list.
        file_.write(str(outputLine).replace(
            "[", "").replace("]", "").replace("'", "").replace(" ", "")+"\n")

    file_.truncate()  # Truncate remaining file.
    file_.close()  # Finally, close the file


def _seq(fileName):
    """
    Replace Column 472 {w,c} by {0,1}
    Replace Column 477 (mit) by (17)
    Doesn`t return anything because all operations are made in the file.\n

    Keyword arguments:\n
        filename (string) : Full or relative string name with file path.\n
    """    
    file_ = open(fileName, "r+")  # Associate file to variable.
    data = file_.readlines()  # Read all lines of file.
    file_.seek(0)  # Set the pointer to the beginning of file.
    columnId = [472, 477]  # Columns ids
    newValues = [0, 1, 17]  # New values

    for line in data:  # For each line on data.
        outputLine = []  # Final Output Line.
        coluns = line.split(",")
        # Replace Column 472 {w,c} by {0,1}
        if (coluns[columnId[0]] == "w"):
            coluns[columnId[0]] = newValues[0]
        elif (coluns[columnId[0]] == "c"):
            coluns[columnId[0]] = newValues[1]
        # Replace Column 477 (mit) by (17)
        if (coluns[columnId[1]] == "mit"):
            coluns[columnId[1]] = newValues[2]
        # Save the output line
        outputLine.append(coluns)
        # Write the output line, replacing the characters of the list.
        file_.write(str(outputLine).replace(
            "[", "").replace("]", "").replace("'", "").replace(" ", "")+"\n")

    file_.truncate()  # Truncate remaining file.
    file_.close()  # Finally, close the file


def _spo(fileName):
    """
    Replace Columns 78 e 79 {no,yes} por {0,1}
    Doesn`t return anything because all operations are made in the file.\n

    Keyword arguments:\n
        filename (string) : Full or relative string name with file path.\n
    """ 
    file_ = open(fileName, "r+")  # Associate file to variable.
    data = file_.readlines()  # Read all lines of file.
    file_.seek(0)  # Set the pointer to the beginning of file.
    columnId = [78, 79]  # Columns ids
    newValues = [0, 1]  # New values

    for line in data:  # For each line on data.
        outputLine = []  # Final Output Line.
        coluns = line.split(",")
        # Replace Column 78 {no,yes} by {0,1}
        if (coluns[columnId[0]] == "no"):
            coluns[columnId[0]] = newValues[0]
        elif (coluns[columnId[0]] == "yes"):
            coluns[columnId[0]] = newValues[1]
        # Replace Column 79 {no,yes} by {0,1}
        if (coluns[columnId[1]] == "no"):
            coluns[columnId[1]] = newValues[0]
        elif (coluns[columnId[1]] == "yes"):
            coluns[columnId[1]] = newValues[1]
        # Save the output line
        outputLine.append(coluns)
        # Write the output line, replacing the characters of the list.
        file_.write(str(outputLine).replace(
            "[", "").replace("]", "").replace("'", "").replace(" ", "")+"\n")

    file_.truncate()  # Truncate remaining file.
    file_.close()  # Finally, close the file


def replaceNoNumericValuesDataSets(dataSetsNames_, path_):
    """
    Replace all no-numeric values on each dataset\n
    Doesn`t return anything, but replace values in the same file. \n
    For more info, ready all the class.\n

    Keyword arguments:\n
        dataSetsNames_ (list[string]):  list of all datasets in path folder.\n
        path_ (string) :  path of datasets folder.\n
    """
    for dataSet in dataSetsNames_:  # For each dataset in the list.
        print(dataSet)
        fileName = path_ + dataSet  # Input full file name.
        # Replace all missing values of the current dataset
        replaceNoNumericAttributes(fileName)
