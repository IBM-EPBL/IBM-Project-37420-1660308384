
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



if __name__ == "__main__":
    app.run(debug=True)

