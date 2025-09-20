# Panda -> Data Manipulation & Data Analysis
# pip install pandas


import pandas as pd
import numpy as np

#object creation
s = pd.Series([1,2,3])   #series means coloumn with index
print(s)
#object creation with empty cell
s1 = pd.Series([1,2,np.nan,3])   
print(s1)
#object creation with range of dates
s3 = pd.date_range("20250901", periods=6)   
print(s3)


#convert into datasheet / worksheet (data frame) rows & column
df = pd.DataFrame(np.random.rand(6,4), index=s3, columns=list("ABCD"))
print(df)


#make dataframe using dictionary
df2 = pd.DataFrame(
    {
    "A":1.0,
    "B":pd.Timestamp(20250920),
    "C":pd.Series(1, index=list(range(4)), dtype="float32"),
    "D":np.array([3] * 4, dtype="int32"),
    "E":pd.Categorical(["girl","women","girl","women"]),
    "F":"females",
})
print(df2)

#type of dataframe
print(df.dtypes)
print(df2.dtypes)


#how to view data
print(df.head(2))   #shows first 2 rows
print(df.tail(2))   #shows last 2 rows

#index of dataframe
print(df.index)
print(df2.index)

#convert dataframe into numpy
print(df.to_numpy)   #converted to array

#describe func
print(df.describe())

#transpose data (rows into column and column into rows)
print(df.T)

#sort data
print(df.sort_index(axis=0, ascending=False))

#select data (Selection/Filteration)
print(df["A"])

#row wise selection - selection of rows using indexing
print(df[0:2])

#selection by labels
print(df.loc[s3[4]])  #shows data of date 5 (index 4)

#column wise selection - selection of column using indexing
print(df[0:2])

#selected selection
print(df.loc["20250901": "20250903", ["A", "B"]])

#get specific value
print(df.at[s3[5], "A"])

#iloc fun for specific selection
print(df.iloc[0:4 , 0:2])  #left - rows & right - columns


#all rows specific column
print(df.iloc[: , 0:3])

#all columns specific rows
print(df.iloc[0:5 , :])

#bool operators (filteration)
print(df["A"] > 0)

print(df > 0)

#copy
df1 = df.copy()
print(df1)

#addition/concatenation
df1["E"] = ["one","one","two","three","four","three"]
print(df1)