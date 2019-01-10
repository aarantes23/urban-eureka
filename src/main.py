import procedures_step1 as procedures_step1
import procedures_step2 as procedures_step2
import procedures_step3 as procedures_step3
import procedures_step4 as procedures_step4

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


# Copy the name of each dataset downloaded
dataSetNames = ["cellcycle_FUN", "church_FUN", "derisi_FUN",
                "eisen_FUN", "expr_FUN", "gasch1_FUN",
                "gasch2_FUN", "hom_FUN", "pheno_FUN",
                "seq_FUN", "spo_FUN", "struc_FUN"]

# Step 1
print("Step 1: For each base, join test + train + valid")
# For each base, join test + train + valid
procedures_step1.createFullDataSets(dataSetNames, path, pathFull)

# Redefine data set names
dataSetNames = ["cellcycle_FUN.full.arff", "church_FUN.full.arff", "derisi_FUN.full.arff",
                "eisen_FUN.full.arff", "expr_FUN.full.arff", "gasch1_FUN.full.arff",
                "gasch2_FUN.full.arff", "hom_FUN.full.arff", "pheno_FUN.full.arff",
                "seq_FUN.full.arff", "spo_FUN.full.arff", "struc_FUN.full.arff"]

# Step 2
print("Step 2: Transform datasets multi-label to single-label")
# Transform datasets multi-label to single-label
procedures_step2.convertToSingleLabelDataSets(dataSetNames, pathFull, pathSingleLabel)

# Redefine data set names, for step 3, replace missing values
dataSetNames = ["cellcycle_FUN.full.arff", "derisi_FUN.full.arff",
                "eisen_FUN.full.arff", "gasch1_FUN.full.arff",
                "gasch2_FUN.full.arff"]

# Step 3
print("Step 3: Replace missing values.")
procedures_step3.replaceMissingValuesDataSets(dataSetNames,pathSingleLabel,pathNoMissingValues)

# Step 4
print("Step 4: Create new Training and Test sets.")
procedures_step4.crossValidationSplitDataSets(dataSetNames,pathNoMissingValues,10,2^7,pathCrossValidation)


print("Work complete!")