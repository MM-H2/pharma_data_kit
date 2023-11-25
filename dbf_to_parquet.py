# author: mostafa

# %%

import pandas as pd
from dbfread import DBF
# %%
table = DBF("D:\\projects\\mdq\\db\\output\\special_request\\New folder\\cat\\phrmtran.DBF")


# %%
df =  pd.DataFrame(table)

# %%
df.to_csv("D:\\projects\\mdq\\db\\output\\special_request\\New folder\\cat\\phrmtran_csv.csv")
