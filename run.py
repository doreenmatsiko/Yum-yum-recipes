from flask import Flask, render_template
import os
from app import app

#app = Flask(__name__)
port=int(os.environ.get('PORT', 5000))
if __name__ == "__main__":
    app.run()
app.config['DEBUG'] = True
app.run(host='0.0.0.0', port=port)

''''
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
''''


