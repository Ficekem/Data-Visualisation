
#Author: Laszlo Koosz

import pandas as pd
df = pd.read_csv('balance.txt',sep=' ')

# Select the 'Limit' and 'Rating' columns of the first five observations
limits_5 = df['Limit'][:5]
ratings_5 = df["Rating"][:5]

# Select the first five observations with 4 cards
cards_4 = df[df["Cards"] == 4][:5]

# Sort the observations by 'Education'. Show users with a high education value first. 
sorted_education_descending = df.sort_values(['Education'], ascending=False)
print(sorted_education_descending)

#Write a short explanation in the form of a comment for the following lines of code.

#select all the rows and all the columns in each row
df.iloc[:,:] 

# select all rows excluding the first 5, and all columns excluding the first 5 columns
df.iloc[5:,5:] 

# select all the rows and only the first columns in each row
df.iloc[:,0]

# select the 9th row and all columns of this row
df.iloc[9,:]
