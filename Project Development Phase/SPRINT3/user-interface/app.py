
import email
from pyexpat import model
from tkinter import S
from flask import Flask , render_template , request , redirect , url_for
from flask import Flask, render_template, request, redirect, session
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')


@app.route('/search1')
def search1():
    return render_template('search1.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/companies')
def companies():
    return render_template('companies.html')

@app.route('/postjob')
def postjob():
    return render_template('postjob.html')


       
   



if __name__ == "__main__":
    app.run(debug=True)

