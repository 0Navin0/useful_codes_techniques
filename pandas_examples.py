## Pandas: merging, joining and concatenating DataFrames
## df.concat() , df.join(), df.merge()
import pandas as pd
import numpy as np

#-----------df.concat()-------------------------
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
   
# Define a dictionary containing employee data 
data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'], 
        'Age':[17, 14, 12, 52], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
 
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])
 
print(df, "\n\n", df1)

# using a .concat() method
frames = [df, df1]
 
res1 = pd.concat(frames) 

# next, what if two dfs don't have the same keys??

data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
        'new_axis':[4,5,6,7]} 

data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'], 
        'Age':[17, 14, 12, 52], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 

df = pd.DataFrame(data1,index=[0, 1, 2, 3]) 
df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])
frames = [df, df1]
#res1 = pd.concat(frames)
res1= pd.concat(frames, sort=False)
## blank places get filled by NaN during concatenation.

##concatenating by some logic on axes of DataFrames

data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
        'Mobile No': [97, 91, 58, 76]} 
   
data2 = {'Name':['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'], 
        'Age':[22, 32, 12, 52], 
        'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons'],
        'Salary':[1000, 2000, 3000, 4000]} 
 
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
# what happens if you change the index of the first two entries below??
# the concatenation join=inner will give empty intersection.
df1 = pd.DataFrame(data2, index=[2, 3, 6, 7]) 
print(df, "\n\n", df1) 
# Now we set join = inner for intersection of dataframe

# applying concat with axes,with the intersection defined by the content of axis=1
res2 = pd.concat([df, df1], axis=1, join='inner')

# what happens when you don't give sort=False....check.
# join = outer ....default
res3 = pd.concat([df, df1], axis=1, sort=False)

# concatenating along the axes of df, using join_axes argument.
res4 = pd.concat([df, df1], axis=1, join_axes=[df.index])
#---------------------------------------------

#--------------df.append()-----------------
# append is same as concat along axis=0
# axis=0 means the index column
res=pd.concat([df,df1],axis=0,sort=False)
res=df.append(df1)

# appending by ignoring the indices of the two dfs
res = pd.concat([df, df1], ignore_index=True)



