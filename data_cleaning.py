import pandas as pd

# 1. Loading the dataset
df = pd.read_csv('online_retail.csv')

#  Removing Unnecessary index if present 
if 'index' in df.columns:
    df.drop(columns=['index'], inplace=True)

# 2. Data Cleaning
df_clean = df.drop_duplicates()  #  Removing Duplicates 
df_clean = df_clean.dropna(subset=['CustomerID']) 
df_clean = df_clean[(df_clean['Quantity'] > 0) & (df_clean['UnitPrice'] > 0)]  # Removing Negative values 

# 3. Data Transformation & Feature Engineering
df_clean['CustomerID'] = df_clean['CustomerID'].astype(int).astype(str)
df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'])

df_clean['TotalAmount'] = df_clean['Quantity'] * df_clean['UnitPrice']
df_clean['InvoiceYearMonth'] = df_clean['InvoiceDate'].dt.to_period('M').astype(str)
df_clean['DayOfWeek'] = df_clean['InvoiceDate'].dt.day_name()
df_clean['Hour'] = df_clean['InvoiceDate'].dt.hour

# 4. Saving Cleaned Dataset 
df_clean.to_csv('cleaned_online_retail.csv', index=False)
print("Data Cleaning Complete! Saved as 'cleaned_online_retail.csv'")