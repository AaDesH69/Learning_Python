import pandas as pds

print(pds.__version__)


dist = {
    'head':{
        'name':'Anamol Chapagain',
        'address': 'kathmandu',
        'number': 123456

    },
    'staff1':{
        'name':'Ram Bahadur',
        'adrresss': 'Bhaktapur',
        'number':9841505050
    }
}


#To convert dictionary to data frame we csn use pd. Data frame
df = pds.DataFrame(dist)
#print(df)
#print(df.head())
print(df.index)