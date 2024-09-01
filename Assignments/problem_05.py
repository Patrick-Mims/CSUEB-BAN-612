import pandas as pd

# read csv file
df = pd.read_csv('football_data.csv')

# debug, show first 10 rows.
print(df.head(10))

df_head = df.head(10) 

# create a new DataFrame
new_df = pd.DataFrame(data=df_head)
sorted_new_df = new_df.sort_values(by=['% Goals-to-shots'])

print(new_df.head(10))
print(sorted_new_df.head(10))

# write .xlsx to disk
sorted_new_df.to_excel("output.xlsx")

# read .xlsx from disk
df_2 = pd.read_excel("output.xlsx", index_col=0)

# obtain column data
clearances_off_line = sorted_new_df["Clearances off line"]

# clearances of Line column
print(clearances_off_line)

# # # # # # # # # # # # # # 
# 5.
# Read the csv file from the following address in a Data Frame:
# https://raw.githubusercontent.com/jokecamp/FootballData/master/UEFA_European_Championship/Euro%202012/Euro%202012%20stats%20TEAM.csv
#
# Display the head of this Dataframe containing first 3 rows. (5 pts)
# #
# #
# Get the top 10 teams in "% Goals-to-shots" 
# (also keep the information of other columns) 
# and save these 10 rows of data into a new dataframe.
# # # # # # # # # # # # # # 
