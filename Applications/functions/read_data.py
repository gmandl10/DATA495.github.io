# function for loading the data

def load_cgc_data():
    import pandas as pd, os

    metadata = pd.read_csv(os.path.dirname(os.path.dirname(os.getcwd()))+"\\Data\\GeneExpression\\manifest_20240128_210036.csv").loc[:, ["name", "disease_type", "id"]]
    # read metadata file for id, name, and disease type (target variable)

    directory = os.path.dirname(os.path.dirname(os.getcwd())) + "\\Data\\GeneExpression\\Files\\"
    master = pd.DataFrame() 
    # initialize data frame

    for file in os.listdir(directory):
        tsv_file_path = directory + file

        df = pd.read_csv(tsv_file_path, sep='\t')
        df = pd.DataFrame(df.set_index("miRNA_ID")["reads_per_million_miRNA_mapped"]).rename(columns={"reads_per_million_miRNA_mapped":file}).T
        # extract miRNA reads from sample

        master = pd.concat([master,df])
        # add sample to master
    
    df = metadata.set_index("name").join(master).set_index("id")
    # join miRNA data to master
        
    return df