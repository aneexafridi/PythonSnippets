from matplotlib import pyplot as pt
from pandas import read_csv

CSV_File = read_csv('MoviesData.csv')

# this is good way to sort the value
# CSV_File.sort_values(by=['IMDb'],inplace=True,ignore_index=True)

Titles = sorted(CSV_File['Titles'].iloc[100:130]) # 100 to 130
IMDb  = CSV_File['IMDb'].iloc[100:130]            # 100 to 130

# Colors = ['red','yellow','black','blue','green','gray','cyan']

# packing and sorted by second item or element
Ziper = sorted(zip(Titles,IMDb),key=lambda x:x[1])

# map here maping
Titles = list(map(lambda x:x[0],Ziper))
IMDb   = list(map(lambda x:x[1],Ziper))

pt.barh(y=Titles,width=IMDb,height=0.8,color='blue')

pt.xlabel('IMDb')
pt.title('Movies Records')

pt.grid(axis='x',color='k',linewidth=3)
pt.show()
