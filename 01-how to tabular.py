import pandas as pd
orders = pd.read_table('http://bit.ly/chiporders')
orders.head()

user_cols = ['user_id', 'edad', 'genero', 'ocupacion', 'zip_code']
users =pd.read_table('http://bit.ly/movieusers', sep = '|', header = None, names = user_cols)
users.head()
