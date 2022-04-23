from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

'''
connection = sqlite3.connect('database.db')
print("Database Opened")
connection.execute('CREATE TABLE Documents(Name Text,Age Number,Adress Text,DOB Date,Phone Number)')
print("Table Created Successfully")
connection.close()
'''


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/documents')
def documents():
    return render_template("submit.html")


if __name__ == "__main__":
    app.run(debug=True)
