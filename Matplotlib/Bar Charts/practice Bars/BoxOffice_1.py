from matplotlib import pyplot as pt
from pandas import read_csv

CSV = read_csv('MoviesData.csv')

print(CSV.loc[[*(range(30))],['Year', 'Romance', 'Horror', 'Mystery']])

