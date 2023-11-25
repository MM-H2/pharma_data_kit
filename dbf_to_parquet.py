# author: mostafa

# %%

import pandas as pd
from dbfread import DBF
import pathlib
import argparse

# %%
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input dbf file path", default="D:\\projects\\mdq\\db\\output\\special_request\\New folder\\cat\\phrmtran.DBF")
parser.add_argument("-o", "--output", help="output parquet file path", default="D:\\projects\\mdq\\db\\output\\special_request\\New folder\\cat\\phrmtran.parquet")
parser.add_argument("-f", "--format", help="output format", default="parquet")
args = parser.parse_args()

# %%
table = DBF("D:\\projects\\mdq\\db\\output\\special_request\\New folder\\cat\\phrmtran.DBF")


# %%
df =  pd.DataFrame(table)

# %%
df.to_csv("D:\\projects\\mdq\\db\\output\\special_request\\New folder\\cat\\phrmtran_csv.csv")
