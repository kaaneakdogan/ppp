# %%
import os
from dotenv import load_dotenv
load_dotenv()
# %%
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
sample_df = pd.read_csv(sample_data_dir, encoding='latin-1')
# %%
df.head()
# %%
#this can be used to view data for testing purposes, but the full dataset is too large to view in its entirety.
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
# As you see here, there are a lot of cells with missing values.
df.isnull().sum()
# %%
if df["DateApproved"].isnull().sum() == 0:
    df["DateApproved"] = pd.to_datetime(df["DateApproved"])
    print("All values in 'DateApproved' column are valid and have been converted to {} format.".format(df["DateApproved"].dtype))
else:
    print("There are missing values in 'DateApproved' column.")
# %%
loan_date_range = df["DateApproved"].min(), df["DateApproved"].max()
sum_of_all_loans = format(df["CurrentApprovalAmount"].sum().astype(int), ",")
print(f"The loan date range is from {loan_date_range[0]} to {loan_date_range[1]} with a total approved amount of {sum_of_all_loans}.")
# %%
column_na_sum_dict = {col: df[col].isnull().sum() for col in df.columns}
column_na_sum_dict = dict(sorted(column_na_sum_dict.items(), key=lambda item: item[1], reverse=True))
print("column_na_sum_dict: ", list(column_na_sum_dict.items()))
# %%
for col in df.columns:
    if df[col].isnull().sum() > 0:
        print(f"Column '{col}' has {df[col].isnull().sum()} missing values with the percentage being {df[col].isnull().sum() / len(df[col]):.2%}.")
    else:
        print(f"Column '{col}' has no missing values.")
# %%
# Assessing how many unique states, borrowers, and lenders are present in the dataset.
borrower_lender_state = "There are {} unique borrowers, {} unique lenders, and {} unique states in the dataset.".format(df["BorrowerName"].nunique(), df["ServicingLenderName"].nunique(), df["BorrowerState"].nunique())
print(borrower_lender_state)
# %%
# Apparently there are 56 unique states (plus 1 NaN value). Curious about how that can be possible :)
df["BorrowerState"].unique()
# All 50 states are present, plus 7 additional entries: "DC for District of Columbia", "PR for Puerto Rico", "VI for U.S. Virgin Islands", "GU for Guam", "AS for American Samoa", "MP for Northern Mariana Islands" and NaN.
# %%
# Assessing top 10 lenders by total loan amount and by number of loans serviced.
top10_lenders_by_loan_amount = df.groupby("ServicingLenderName")["CurrentApprovalAmount"].sum().sort_values(ascending=False).head(10)
top10_lenders_by_loan_count = df.groupby("ServicingLenderName")["LoanNumber"].count().sort_values(ascending=False).head(10)
print("Lenders by loan amount: ", top10_lenders_by_loan_amount)
print("Lenders by loan count: ", top10_lenders_by_loan_count)
# %%

# %%
