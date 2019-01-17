#how do i sort a pandas dataframe or series?
import pandas as pd
movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()
movies.title.sort_values()
#or
movies['title'].sort_values()
movies['title'].sort_values(ascending=False)
movies['title']
movies.sort_values('title')
movies.sort_values('duration')
movies.sort_values('duration', ascending=False)
movies.head()
movies.sort_values(['content_rating', 'duration'])
