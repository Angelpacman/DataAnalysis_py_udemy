import pandas as pd
movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()
type(movies)

#vamos a filtrar el dta frame de manera que deje afuera a los que estan por encima de un rango
booleans=[]
for length in movies.duration:
    if length >=200:
        booleans.append(True)
    else:
        booleans.append(False)


booleans[0:10]

len(booleans)

is_long = pd.Series(booleans)

is_long.head()

type(booleans)

type(is_long)

#aqui nos va a mostrar el df completo pero solo con los valores True de is_long, lo que quiere
#decir que nos da las celdas que tienen una duracion mayor a 200
movies[is_long]

is_long = movies.duration >= 200
is_long.head()
type(is_long)
movies[movies.duration >= 200]
movies[movies.duration >= 200].genre
movies[movies.duration >= 200]['genre']

movies.loc[movies.duration >= 200, 'genre']
