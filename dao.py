import peewee 
from models import Movie as MovieModel

db = peewee.SqliteDatabase('moviecatalog.db')

class Movie(peewee.Model):
    title = peewee.CharField()
    year = peewee.CharField()
    sinopsis = peewee.CharField()

    class Meta:
        database = db # This model uses the "people.db" database.
        db_table = 'movies'

Movie.create_table()

def create(movie: MovieModel):
    dao = Movie.create(title=movie.title, year=movie.year, sinopsis=movie.sinopsis)
    dao.save()

def readAll():
    rows = Movie.select()
    movies = []
    for row in rows:
        movies.append(MovieModel(row.title, row.year, row.sinopsis))
    return movies

def readByTitle(title): 
    movie = Movie.select().where(Movie.title==title).get()
    return movie

def updateByTitle(movie: MovieModel):
    qry = Movie.update(title=movie.title, year=movie.year, sinopsis=movie.sinopsis).where(Movie.title==movie.title)
    qry.execute()

def deleteByTitle(title):
    qry = Movie.delete().where(Movie.title==title)
    qry.execute()

def deleteAllRecords():
    qry = Movie.delete().where(Movie.id >= 0)
    qry.execute()