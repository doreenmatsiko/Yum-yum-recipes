from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template("login.html")



if __name__ == "__main__":
    app.run()
