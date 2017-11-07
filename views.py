from flask import Flask, render_template

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

@app.route("/categories")
def categories():
    return render_template("categories.html")

@app.route("/recipes")
def recipes():
    return render_template("recipes.html")

@app.route("/details")
def details():
    return render_template("details.html")

@app.route("/add_recipe_category")
def add_recipe_category():

    return render_template("add_recipe_category.html")


if __name__ == "__main__":
    app.run()
