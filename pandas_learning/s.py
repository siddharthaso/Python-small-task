import time
from dask import dataframe as dd
import pandas as pd


dask_df = dd.read_csv('/home/siddharthasodariya/Pandas/huge_data.csv')
pd_df = pd.read_csv('/home/siddharthasodariya/Pandas/huge_data.csv')

new_positions = ['C1', 'C11', 'C12', 'C13', 'C14', 'C15', 'C2', 'C3', 'C4', 'C7', 'C8', 'C9', 'C10']

start = time.time()

dask_df = 
# # dask_df1 = dask_df (columns = new_positions)
# print(dask_df1.columns.tolist())
# end = time.time()
# print("reorder with dask: ",(end-start),"sec")

# start = time.time()
# pd_df1 = pd_df.reindex(columns=new_positions)
# print(pd_df1.columns.tolist())
# end = time.time()
# print("reorder with pd: ",(end-start),"sec")