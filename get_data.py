import pandas as pd 

data = pd.read_csv('https://snap.stanford.edu/biodata/datasets/10004/files/DCh-Miner_miner-disease-chemical.tsv.gz', sep='\t', header=0)
# data["Chemical"] = data["Chemical"].apply (lambda row: 'DRUGBANK:' + row)
print(data)
data.to_csv('mined-disease-chemical-associations.csv', index=False, header=False)