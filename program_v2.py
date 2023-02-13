import pandas as pd

#Function to calculate coefficient for leap years
def coefficient_for_leap_year_calculator(Year):
    if((Year % 400 == 0) or  (Year % 100 != 0) and  (Year % 4 == 0)):
        return 10/9
    else:
        return 10/8

#Input the excel file
df = pd.read_excel('data.xlsx')

print(df)

#Create 3 groups, A, B and C. A is for days from 1-10, B is for days 11-20 of the month and C is for the last days of the month
groups  = ['A', 'A', 'A', 'A','A', 'A', 'A', 'A','A', 'A', 'B','B','B','B','B','B','B','B','B','B','C','C','C','C','C','C','C','C','C','C','C',]
#Add the column to the existing columns
df['Groups'] = groups

print(df)

#Calculate the means for the columns for each group A B C
df_means = df.groupby('Groups').mean()

#print(df_means)

#At first we take care of the months with 31days and then the februaries
#List of months in the dataset that are of 31st days
months_with_31days = ('Jan','Mar','May','July','Aug','Oct','Dec')
columns_for_months_with_31days = [col for col in df if col.startswith(months_with_31days)]

#Multiplication for the mean in row C for columns that are for months with 31 days
df_means.loc['C',columns_for_months_with_31days] = df_means.loc['C',columns_for_months_with_31days]*(10/11)

#Now we take care of the Februaries
for column in df_means:
    if column.startswith('Feb'):
        #Extract the year from the column name
        year = int(column.split("_", 1)[1])
        #Multiply the corresponding value in the table with 10/9 if it is a leap year or 10/8 if it is not a leap year
        df_means.loc['C',column] = df_means.loc['C',column]* coefficient_for_leap_year_calculator(year)

print(df_means)







