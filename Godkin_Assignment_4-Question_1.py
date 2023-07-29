# Module 4 Assignment
# Question 1
# Author: Ralph Godkin

# IMPORTS
import pandas as pd

# Create the DataFrame
hmeq = pd.read_csv("hmeq_small.csv")

# Remove rows with missing data
df1 = hmeq.dropna()

# Use Mean as default value
df2 = hmeq.fillna(hmeq.mean())

# Print the means of the columns for each new data frame
print('\nMean of the data with empty rows removed:')
print(df1.mean(), '\n')

print('Mean of the data with the mean used in place of missing fields:')
print(df2.mean(), '\n')