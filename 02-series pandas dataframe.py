#how do i selecr a pandas series from a dataframe
import pandas as pd
ufo = pd.read_csv('http://bit.ly/uforeports')
type(ufo)
ufo.head()
type(ufo['City'])
ufo['City']
ufo.City
ufo['Colors Reported']

ufo.City + ',' + ufo.State
ufo['Lugarcillo'] = ufo.City + ',' + ufo.State
