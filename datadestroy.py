import pandas as pd
import numpy as np

df = pd.read_csv("voyage_ai_travel_data.csv")

print(df.head())
print(df.info())

#adding missing values 
df_missing = df.copy()
for col in df_missing.columns:
    df_missing.loc[df_missing.sample(frac=0.15).index, col] = np.nan

#add duplicate values
duplicates = df_missing.sample(frac=0.1)
df_dup = pd.concat([df_missing, duplicates], ignore_index=True)

#inject outliers in values
price_cols = ['trip_frequency','destination_diversity','search_behavior']  # adjust to your dataset

for col in price_cols:
    if col in df_dup.columns:
        df_dup.loc[df_dup.sample(frac=0.05).index, col] *= 8

#add numericals cols 
num_cols = df_dup.select_dtypes(include=np.number).columns

for col in num_cols:
    noise = np.random.normal(0, df_dup[col].std()*0.1, df_dup.shape[0])
    df_dup[col] = df_dup[col] + noise

df_dup['destination_diversity'] = df_dup['destination_diversity'].replace({
    'Paris': 'paris',
    'New York': 'NewYork',
    'London': 'Londn'
})

df_dup['travel_date'] = df_dup['travel_date'].astype(str)

df_dup.loc[df_dup.sample(frac=0.1).index, 'travel_date'] = '32-13-2025'

df_dup['Booking_Status'] = np.random.permutation(df_dup['Booking_Status'])

df_dup.to_csv("voyage_ai_travel_data_final.csv", index=False)
