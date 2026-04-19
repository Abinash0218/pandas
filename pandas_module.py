import pandas as pd

# Creating Dataframes
df=pd.DataFrame({
    "name":["Abinash", "Ajay", "Arun"],
    "marks":[80, 90, 78],
    "city":["Chennai", "Delhi", "Mumbai"]
})
print(df)

# Selecting data from rows and columns
print(df['marks'])
print(df[['name', 'marks']])
print(df[df.marks > 80])

# Accessing the data using the index and label
print(df.loc[0,'name']) # by label
print(df.iloc[0,1]) # by position

# Filtering & Query
print(df.query("marks >= 80"))
print(df.query("name=='Ajay'"))

# Sorting & Renaming
print(df.sort_values('marks')) # Ascending order
print(df.sort_values('marks', ascending=False)) # Descending order
print(df.rename(columns={'marks': 'score'}))

# Handling missing data
# df1=pd.DataFrame({
#     'Street':["ABC Street", "XYZ Street"],
#     'City': ["Hosur"]
# })
# print(df1)
# print(df1.dropna())