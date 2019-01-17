import pandas as pd
movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()
movies[movies.duration >= 200]
movies[(movies.duration >= 200) & (movies.genre == 'Drama')]
movies[(movies.duration >= 200) | (movies.genre == 'Drama')]

movies[(movies.genre == 'Crime') | (movies.genre == 'Drama')]

(movies.genre == 'Crime') | (movies.genre == 'Drama')
