from flask import Flask, render_template, request,  redirect, session, flash, url_for
from default_movie_db import createDb
from models import Movie
import dao 

# Start app
app = Flask(__name__)
app.secret_key = 'matrix'

# Reset database
dao.deleteAllRecords()
createDb()

'''
# initial list
dao.create(Movie('Godzilla', '1999', 'filme de monstro'))
dao.create(Movie('Pulp Fiction', '1987', 'Escrito e dirigido por Quentin tarantino'))
dao.create(Movie('Mad Max', '2017', 'Witness me'))
'''


#Main page: exhibits movies
@app.route('/')
def index():
    lista = dao.readAll()
    return render_template('movies.html', titulo='Filmes', movies=lista)

#Form for adding new movies to inventory
@app.route('/add_movie')
def add_movie():
    if 'logged_user' not in session or session['logged_user'] == None:
        return redirect(url_for('login', next=url_for('add_movie')))
    return render_template('add_movie.html', titulo='Adicionar novo filme')

#Adds movie from the form to movie inventory and returns to main 
@app.route('/create', methods=['POST',])
def create():
    title = request.form['title']
    year = request.form['year']
    sinopsis = request.form['sinopsis']
    movie = Movie(title, year, sinopsis)
    dao.create(movie)
    return redirect(url_for('index'))

#Form for editing new movies to inventory
@app.route('/edit/<title>')
def edit(title):
    if 'logged_user' not in session or session['logged_user'] == None:
        return redirect(url_for('login', next=url_for('edit')))
    movie = dao.readByTitle(title)
    return render_template('edit_movie.html', titulo=f'Editar {title}', movie=movie)

#Adds movie from the form to movie inventory and returns to main 
@app.route('/update', methods=['POST',])
def update():
    title = request.form['title']
    year = request.form['year']
    sinopsis = request.form['sinopsis']
    movie = Movie(title, year, sinopsis)
    dao.updateByTitle(movie)
    flash(f'{title} foi editado com sucesso')
    return redirect(url_for('index'))

@app.route('/delete/<title>')
def delete(title):
    dao.deleteByTitle(title)
    flash(f'{title} foi removido com sucesso')
    return redirect(url_for('index'))

@app.route('/read/<title>')
def read(title):
    movie = dao.readByTitle(title)
    return render_template('read_movie.html', titulo=f'{title}', movie=movie)


@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', next=next)

@app.route('/authenticate', methods=['POST', ])
def authenticate():
    if 'enter' == request.form['pass']:
        session['logged_user'] = request.form['user']
        flash(request.form['user'] + ' logou com sucesso!')
        next_page = request.form['next']
        return redirect(next_page)
    else:
        flash('Senha incorreta')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('Logout realizado com sucesso!')
    return redirect(url_for('index'))

# route to test db
@app.route('/testdb')
def test():
    print("------------------------------------------------------------------------------------------------")
    x = dao.readAll()
    for xx in x:
        print(xx.asString())
    return redirect(url_for('index'))

app.run(debug=True)