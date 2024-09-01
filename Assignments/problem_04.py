import numpy as np
import pandas as pd

data_dict = dict(
		Age=[25, 32, 28, 21, 40, 35, 22, 62], 
		Gender=['F', 'M', 'F', 'M', 'F', 'M', 'F', 'M'], 
		Education=[
		'Bachelor\'s', 
		'Master\'s', 
		'Associates\'s',
		'High School',
		'PhD',
		'Bachelor\'s',
		'Associates\'s',
		'Master\'s'
		],
		Income_Bracket=[
		"50,000-75,000",
		"75,000-100,000",
		'35,000-50,000',
		'less than 35,000',
		'over 100,000',
		'75,000-100,000',
		'35,000-50,000',
		'over 100,000'
		],
		City=[
			'Los Angeles',
			'San Francisco',
			'New York',
			'Seattle',
			'Boston',
			'San Francisco',
			'Los Angeles',
			'San Francisco'
		])

df = pd.DataFrame(data_dict)
df = df.ffill()

print()

# reindex the data frame, add 'Zip_Code'.
redefined_df = df.reindex(columns=[
		'Age', 
		'Gender', 
		'Education', 
		'Income_Bracket', 
		'City', 
		'Zip_Code'
], fill_value='-')

# using a lambda to perform the if-else function for the DataFrame.
df['Zip_Code'] = redefined_df['City'].apply(
		lambda loc: '94016' 
		if loc == 'San Francisco' else '90210' 
		if loc == 'Los Angeles' else '10001' 
		if loc == 'New York' else loc 
		)

print(df)

print()

print("Sorted By Age")

# sort the values by age
df = df.sort_values(by=['Age'])

print(df)

df.to_csv('out.csv', index=False)
