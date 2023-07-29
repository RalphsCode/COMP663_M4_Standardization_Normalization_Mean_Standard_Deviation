# Module 4 Assignment
# Question 2
# Author: Ralph Godkin

# IMPORTS
import pandas as pd
import numpy as np
from sklearn import preprocessing as pp

# Create the DataFrame
hmeq = pd.read_csv("hmeq_lab412.csv")

# Standardizes the data
standardized = pp.scale(hmeq)

# Output the standardized data as a data frame
df1 = pd.DataFrame(standardized, columns=['Loan', 'Mort Due','Value','YOJ', 'CLAge', 'CLNO', 'DebtInc'])

# Print the mean and standard deviation of the standardized data.
print('\nThe means of the df1 data is: ')
print(df1.mean(), '\n')
print('\nThe Standard Deviations of the df1 data is: ')
print(np.std(df1, ddof=1), '\n')

# Normalize the data
normalized = pp.MinMaxScaler().fit_transform(hmeq)

# Output the normalized data as a data frame
df2 = pd.DataFrame(normalized, columns=['Loan', 'Mort Due','Value','YOJ', 'CLAge', 'CLNO', 'DebtInc'])

# Print the mean and standard deviation of the normalized data.
print('\nThe means of the df2 data is: ')
print(df2.mean(), '\n')
print('\nThe Standard Deviations of the df2 data is: ')
print(np.std(df2, ddof=1), '\n')
