from flask import Flask, render_template,flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from models import User,Recipe_category

USERS= {}
CATEGORIES={}

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

        user = User(username, email, password)

        USERS[username] = user

        flash('You are now registered and can log in', 'success')
        return render_template('login.html')
    return render_template('register.html', form=form)
# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    password = form.password.data
    if request.method == 'POST':
        # Get Form Fields
        username = str(request.form['username'])
        password_candidate = str(request.form['password'])

        for user in USERS.values():
            if user.username == username and user.password == password_candidate:
                # Passed
                session['logged_in'] = True
                session['username'] = username
                flash('You are now logged in', 'success')

                return redirect(url_for('add_recipe_category'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
    return render_template("login.html")


@app.route('/dashboard')
def dashboard ():
    return render_template('categories.html')



@app.route('/add_recipe_category', methods=['GET', 'POST'])
def add_recipe_category():
    if request.method=='GET':
        return redirect(url_for('dashboard'))

    if request.method =='POST':

        CATEGORIES[request.form['title']] = Recipe_category(request.form['title'])
        return render_template("categories.html", recipe_category=CATEGORIES)


@app.route("/delete_category")
def delete_recipe_category():
    pass
@app.route("/update_category")
def update_recipe_category():
    pass
@app.route("/read_category")
def read_recipe_category():
    pass






if __name__ == '__main__':
    app.secret_key='sfxhecygdzfzrettzxgvbdsjdbshbv123'
    app.run(debug=True)