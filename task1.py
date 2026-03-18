import pandas as pd

df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

print(df.head())
print(df.info())
print(df.isnull().sum())

df = df.drop_duplicates()
df = df.fillna(method='ffill')

if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

df.to_csv("cleaned_superstore.csv", index=False)

print("Data cleaned successfully!")