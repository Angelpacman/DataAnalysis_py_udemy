import pandas as pd
ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.head()
ufo.columns
ufo.rename(columns = {'Colors Reported' : 'Colors_Reported', 'Shape Reported':'Shape_Reported'}, inplace= True)
ufo.columns
ufo_cols = ['city', 'colors reported', 'shape reported', 'state', 'time']
ufo.columns = ufo.cols
ufo.head()
ufo = pd.read_csv('http://bit.ly/uforeports', names =ufo_cols, header=0)
ufo.head()
ufo.columns
ufo.columns=ufo.columns.str.replace(' ','_')
ufo.columns
