# author: mostafa

# %%

import pandas as pd
from dbfread import DBF
import pathlib
import argparse

# %%
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input dbf file path", default="D:\\projects\\mdq\\db\\output\\special_request\\New folder\\cat\\phrmtran.DBF")
parser.add_argument("-o", "--output", help="output parquet file path", default="D:\\projects\\mdq\\db\\output\\special_request\\New folder\\cat\\phrmtran")
parser.add_argument("-f", "--format", help="output format", default="parquet")
args = parser.parse_args()

# %%
table = DBF("D:\\projects\\mdq\\db\\output\\special_request\\New folder\\cat\\phrmtran.DBF")

df =  pd.DataFrame(table)
# %%
def dbf_to_parquet(table, output_path):
    output_path = pathlib.Path(output_path+".parquet")
    df.to_parquet(output_path)

def dbf_to_csv(table, output_path):
    output_path = pathlib.Path(output_path+".csv")
    df.to_csv(output_path)
