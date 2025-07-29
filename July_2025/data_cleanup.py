import pandas as pd

ksi_raw_df = pd.read_csv('Motor_Vehicle_Collisions_with_KSI_Data.csv')


## Convert the Date and then filter it out ##
ksi_raw_df['DATE'] = pd.to_datetime(ksi_raw_df['DATE'], format="%Y-%m-%d")

ksi_raw_filtered = ksi_raw_df.loc[(ksi_raw_df['DATE'] >= '2015-01-01'), :].copy().reset_index()

ksi_raw_filtered['ACCIDENT_YEAR'] = ksi_raw_filtered['DATE'].dt.year

## Dump data file to our folder and overwrite ##
ksi_raw_filtered.to_csv('Motor_Vehicle_Collisions_with_KSI_Data.csv', index=False)
