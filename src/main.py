import procedures_step1 as procedures_step1
import procedures_step2 as procedures_step2
import procedures_step3 as procedures_step3
import procedures_step4 as procedures_step4
import procedures_step5 as procedures_step5

from shutil import copyfile

# Step 0
# Download Funcat datasets at https://dtai.cs.kuleuven.be/clus/hmcdatasets/

path = "../datasets/originals/unzip/"  # Unzip each dataset in that folder
# Create a path to the output file, that each full dataset will stay
pathFull = "../datasets/full/"
# Path for the full single label files
pathSingleLabel = "../datasets/singleLabel/"
# Path for the files whitout missing values "?"
pathNoMissingValues = "../datasets/noMissingValues/"
# Path for the crossValidation
pathCrossValidation = "../datasets/crossValidation/"

# Copy the name of each dataset downloaded, for step 1, 12 original datasets
dataSetNames = ["cellcycle_FUN", "church_FUN", "derisi_FUN",
                "eisen_FUN", "expr_FUN", "gasch1_FUN",
                "gasch2_FUN", "hom_FUN", "pheno_FUN",
                "seq_FUN", "spo_FUN", "struc_FUN"]

print("\nStep 1: For each base, join test + train + valid.")
# For each base, join test + train + valid
procedures_step1.createFullDataSets(dataSetNames, path, pathFull)

# Redefine data set names, for step 2, 12 full datasets
dataSetNames = ["cellcycle_FUN.full.arff", "church_FUN.full.arff", "derisi_FUN.full.arff",
                "eisen_FUN.full.arff", "expr_FUN.full.arff", "gasch1_FUN.full.arff",
                "gasch2_FUN.full.arff", "hom_FUN.full.arff", "pheno_FUN.full.arff",
                "seq_FUN.full.arff", "spo_FUN.full.arff", "struc_FUN.full.arff"]

print("\nStep 2: Transform datasets multi-label to single-label.")
# Transform datasets multi-label to single-label
procedures_step2.convertToSingleLabelDataSets(
    dataSetNames, pathFull, pathSingleLabel)

print("\nStep 3: Replace no-numeric attributes.")
# Redefine data set names, only 5 need for this step
dataSetNames = ["church_FUN.full.arff", "expr_FUN.full.arff",
                "pheno_FUN.full.arff", "seq_FUN.full.arff", "spo_FUN.full.arff"]

# 5 dbs have some no-numeric attributes. [church_FUN, expr_FUN, pheno_FUN, seq_FUN, spo_FUN]
# The approach adopted was to replace the non-numerical attributes for numeric ones
# Ex: replace {yes,no} by {0,1}
procedures_step3.replaceNoNumericValuesDataSets(
    dataSetNames, pathSingleLabel)

print("\nStep 4: Replace missing values.")
# 3 have no missing values. [hom_FUN, struc_FUN,pheno_FUN]
# 5 have only numeric atributes [cellcycle_FUN,derisi_FUN,eisen_FUN,gasch1_FUN,gasch2_FUN]
# 5 have some no-numeric attributes. [church_FUN, expr_FUN, pheno_FUN, seq_FUN, spo_FUN]

# First, copy the datasets that has no missing values to the new location.
dataSetNames = ["hom_FUN.full.arff",
                "struc_FUN.full.arff",
                "pheno_FUN.full.arff", ]
for dataSet in dataSetNames:
    src = pathSingleLabel + dataSet  # Input full file name.
    fileName = pathNoMissingValues + dataSet  # Destination file name.
    copyfile(src, fileName)  # Create a copy of the dataset.

# Then, redefine data set names, for step 3, replace missing values, only 9 go for next step.
dataSetNames = ["cellcycle_FUN.full.arff", "church_FUN.full.arff", "derisi_FUN.full.arff",
                "eisen_FUN.full.arff", "expr_FUN.full.arff", "gasch1_FUN.full.arff",
                "gasch2_FUN.full.arff",  "seq_FUN.full.arff", "spo_FUN.full.arff"]

# Lastly, execute the procedure for this step.
procedures_step4.replaceMissingValuesDataSets(
    dataSetNames, pathSingleLabel, pathNoMissingValues)

# Step 5
print("\nStep 5: Create new Training and Test sets.")
procedures_step5.crossValidationSplitDataSets(
    dataSetNames, pathNoMissingValues, 10, 2 ^ 7, pathCrossValidation)

print("\nWork complete")
