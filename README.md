# Yum-yum-recipes
This app stores your recipes
This app will make you enjoy your recipes at any time any where in the world

[![Build Status](https://travis-ci.org/doreenmatsiko/Yum-yum-recipes.svg?branch=develop)](https://travis-ci.org/doreenmatsiko/Yum-yum-recipes)
A food recipe is defined a set of instructions for making or preparing something, especially a food dish. eg a recipe for a cake.

The challenge of keeping track of awesome food recipes is a need for many individuals who love to cook and eat good food that requires an innovative and robust solution that will allow them to remember recipes and share with others

YummyRecipes

The innovative yummy recipes app is an application that allows users to create, save and share meeting the needs of keeping track of awesome food recipes.

Installation

$ git clone https://github.com/doreenmatsiko/Yum-yum-recipes
Navigate to the root folder

Then navigate to $ YummyRecipes

Setup Virtual Environment

$ pip install virtualenv

$ virtualenv venv
you will see (venv) at the beginning of the terminal text

$ workon venv
install the requirements

$ pip install  -r requirements.txt
OR

$ pip install --upgrade -r requirements.txt
Provide the flask application environment variable

and then run the serverby;

$ python run.py

Testing.

i have used unittests for test. Navigate into the root directory .

 run

  $nose2