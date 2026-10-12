import pandas as pd

# 1. Load and inspect - PDF Step 1
df = pd.read_csv('trades.csv')

# head(), shape, info(), dtypes - PDF me yahi bola hai
print("--- head() ---")
print(df.head())

print("\n--- shape ---")
print(df.shape)

print("\n--- info() ---")
print(df.info())

print("\n--- dtypes ---")
print(df.dtypes)

print("\n--- column names ---")
print(df.columns.tolist())