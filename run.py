from flask import Flask, render_template,flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from models.user import User
from models.categories import Category
from models.recipes import Recipe


USERS= {}
CATEGORIES={}
RECIPES={}

recipes = {}
app = Flask(__name__)

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')
class LoginForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    password = PasswordField('Password',)



@app.route('/')
def home():
    return render_template('home.html')


# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = str(form.password.data)

        user = User(username, email, password)#creating an instance of a user

        USERS[username] = user #storing a user object in the USERS dictionary

        flash('You are now registered and can log in', 'success')
        return render_template('login.html')
    #if a GET request
    return render_template('register.html', form=form)
# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    password = form.password.data
    if request.method == 'POST':
        username = str(request.form['username'])
        #comparison if the input password is equal to the password used for registration
        password_candidate = str(request.form['password'])

        for user in USERS.values():
            if user.username == username and user.password == password_candidate:
                # if the users username and password pass, we set the session
                session['logged_in'] = True
                session['username'] = username
                flash('You are now logged in', 'success')

                return redirect(url_for('dashboard'))
            else:#if any of the two are not satisfied
                error = 'Invalid login'
                return render_template('login.html', error=error)
    return render_template("login.html")


@app.route('/dashboard')
def dashboard ():
    return render_template('categories.html',categories = CATEGORIES)# we are passing the CATEGORIES dict to the template

@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        #Adding the Category object to the CATEGORIES dict
        CATEGORIES[request.form['title']] = Category(request.form['title'])
        return render_template('categories.html', categories=CATEGORIES)
    return redirect(url_for('dashboard'))#this is a get request


@app.route('/delete_category/<title>')
def delete_category(title):
    if title in CATEGORIES:
        del CATEGORIES[title] # deleting a the value for title from the CATEGORIES dictionary
        return redirect(url_for('dashboard'))


@app.route('/edit_category/<title>', methods=['GET', 'POST'])

def edit_category(title):
    category = CATEGORIES[title]#category represents category object(value) to title

    if request.method == 'POST':
        category.title = request.form['title'] #what we put on the form is the title of the category object

        return render_template('categories.html', categories = CATEGORIES, title= category.title)
    #IF its a get request we render the edit template to update the data on the form
    return render_template('edit_category.html', title = category.title,category=Category(title))

@app.route('/add_Recipe/<title>',methods=['GET','POST'])
def add_Recipe(title):
    if request.method == 'POST':
        RECIPES[request.form['title']] = Recipe(request.form['title'])
        return redirect(url_for('recipes_dashboard'))#this is a get request
    return render_template('recipe_dashboard.html', recipes=RECIPES)



@app.route('/recipes_dashboard/<title>')
def recipes_dashboard(title):
    return render_template('recipes.html',recipes=RECIPES)






@app.route

@app.route('/logout')
def logout():
    session.clear() #clear the session
    flash('You are now logged out', 'success')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.secret_key='sfxhecygdzfzrettzxgvbdsjdbshbv123'
    app.run(debug=True)