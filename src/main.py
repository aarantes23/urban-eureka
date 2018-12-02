import procedures_step1 as procedures_step1

# Step 0
# Download Funcat datasets at https://dtai.cs.kuleuven.be/clus/hmcdatasets/

path = "../datasets/originals/unzip/"  # Unzip each dataset in that folder
# Create a path to the output file, that each full dataset will stay
pathFull = "../datasets/full/"

# Copy the name of each dataset downloaded
dbNames = ["cellcycle_FUN", "church_FUN", "derisi_FUN",
           "eisen_FUN", "expr_FUN", "gasch1_FUN",
           "gasch2_FUN", "hom_FUN", "pheno_FUN",
           "seq_FUN", "spo_FUN", "struc_FUN"]

# Step 1
# For each base, join test + train + valid
procedures_step1.createFullDataSets(dbNames, path, pathFull)

# Step 2
# Transform datasets multi-label to single-label
