from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    friends = mysql.query_db('SELECT name,age,created_at_day,created_at_year FROM friends')
    return render_template('index.html',friendList = friends)
@app.route('/addFriend',methods=['POST'])
def addFriend():
    query = 'INSERT INTO friends (name,age,created_at_day,created_at_year) VALUES (:name,:age,NOW(),NOW())'
    data = {'name':request.form['friendName'],'age':request.form['friendAge']}
    mysql.query_db(query,data)
    return redirect('/')
app.run(debug=True)
