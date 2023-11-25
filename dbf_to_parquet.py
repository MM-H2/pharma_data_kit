# author: mostafa

import pandas as pd
from dbfread import DBF
import pathlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input dbf file path", default="D:\\projects\\mdq\\db\\output\\special_request\\New folder\\cat\\phrmtran.DBF")
parser.add_argument("-f", "--format", help="output format", default="parquet")
args = parser.parse_args()

output_path = args.input.split(".")[0]

table = DBF(args.input)
df =  pd.DataFrame(table)

def dbf_to_parquet_func(output_path):
    output_path = pathlib.Path(output_path+".parquet")
    df.to_parquet(output_path)

def dbf_to_csv_func(output_path):
    output_path = pathlib.Path(output_path+".csv")
    df.to_csv(output_path)

if args.format == "parquet":
    dbf_to_parquet_func(table, output_path)
elif args.format == "csv":
    dbf_to_csv_func(table, output_path)
else:
    print("invalid format")

