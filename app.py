import pandas as pd

lis1 = [1,2,3,4]
lis2 = ['Item1','Item2','Item3','Item4']

dataframe = pd.DataFrame(lis1,lis2, columns =['Serial no.', 'Items'])

print(dataframe)
