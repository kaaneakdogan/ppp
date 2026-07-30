# %%
import os
from dotenv import load_dotenv
load_dotenv()
data_dir = os.getenv("DATA_DIR", "./data")
# %%
# Check if the data directory is valid:
print(data_dir)
# %%
import pandas as pd
# df is your data frame generated from the CSV.
df = pd.read_csv(data_dir, encoding='latin-1')
df.head()
# %%
# Inspect column names and understand your variables.
df.columns
# %%
print(f"Dataset has {len(df.columns)} columns and {len(df)} rows. There are {df.isnull().any(axis=1).sum()} rows with missing values.")

# %%
