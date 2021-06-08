import pandas as pd
import csv

df = pd.read_csv(r"C:\Users\Pramanik\Documents\Projects\spark\files_test\table1.csv",header = 0)

print(df.head(10))
df['C3'] = df['C3'].astype('datetime64[ns]')

df['C5'] = df.groupby(['C1','C2'])['C3'].rank(ascending= False)

print(df.head(10))

def cus_filter(df):
    if df['C1'] in ['c','e','g'] and df['C5']==1.0: return 'Y'
    elif df['C1']== 'a' and df['C5']==2.0: return 'Y'

df['keep'] = df.apply(cus_filter,axis = 1)

print( df.head(10))

dfres = df.loc[df['keep']=='Y']

print(dfres.head())

df['C6'] = df.groupby(['C1','C2'])['C3'].rank(ascending= True)

dfval = df.loc[df['C6']==1.0]

dfres = pd.merge(df,dfval,on=['C1'],how = 'left')
print(dfres[['C1','C2_x','C3_x','C4_y']])


df1 = pd.read_csv(r"C:\Users\Pramanik\Documents\Projects\spark\files_test\tab2.csv",header = 0)
df2 = pd.read_csv(r"C:\Users\Pramanik\Documents\Projects\spark\files_test\tabb3.csv",header = 0)
df2['max_delivery_date'] = df2['max_delivery_date'].astype('datetime64[ns]')

print( df1.head())
print( df2.head())

df1exp = df1.assign(regions = df1.regions.str.split(",")).explode('regions')

dfres = pd.merge( df1exp,df2, how='left', left_on = ['regions'], right_on=['region'])
dfres['keep'] = dfres.groupby(['item','manufacturing_plant'])['max_delivery_date'].rank( method='min',ascending= False)
dfres2 = dfres.loc[dfres['keep']==1.0]
dfres2.drop_duplicates(keep=False, inplace=True)
print ( dfres2.head(15))

