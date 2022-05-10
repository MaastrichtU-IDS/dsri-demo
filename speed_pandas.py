from datetime import datetime

import pandas as pd

import timeit

def a():
    data = pd.read_csv('https://snap.stanford.edu/biodata/datasets/10004/files/DCh-Miner_miner-disease-chemical.tsv.gz', sep='\t', header=0)
    data["Chemical"] = data["Chemical"].apply (lambda row: 'DRUGBANK:' + row)
    data.to_csv('mined-disease-chemical-associations.csv', index=False, header=False)

    return data

print(timeit.timeit(a, number=3))
