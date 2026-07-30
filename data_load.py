# %%
import os
from dotenv import load_dotenv
load_dotenv()
data_dir = os.getenv("DATA_DIR", "./data")
sample_data_dir = os.getenv("SAMPLE_DATA_DIR", "./data/sample_1k.csv")
# %%
# Check if the data directory is valid:
print(data_dir)
print(sample_data_dir)
# %%
import pandas as pd
# df is your data frame generated from the CSV.
df = pd.read_csv(data_dir, encoding='latin-1')
df.head()
# %%
#this can be used to view data for testing purposes, but the full dataset is too large to view in its entirety.
sample_df = pd.read_csv(sample_data_dir, encoding='latin-1')
sample_df.head()
# %%
# Inspect column names and understand your variables.
df.columns
# %%
# Checking for missing values in the dataset and understanding the shape of the data.
print(f"Dataset has {len(df.columns)} columns and {len(df)} rows. There are {df.isnull().any(axis=1).sum()} rows with missing values.")
# %%
# Understanding the data types of each column.
df.dtypes.unique()
# %%
sample_df["BorrowerAddress"].isnull().sum()          # count of missing
# %%
