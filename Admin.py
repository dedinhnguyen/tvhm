import MySQLdb
from flask import Flask, render_template, session, request, redirect, url_for
from app import app
from flask_mysqldb import MySQL
import configpass
import configadmin
import SQL
import alert
import hashlib
from pymysql import cursors
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123123'
app.config['MYSQL_DB'] = 'tonvinhhienmau'
mysql = MySQL(app)

@app.route('/')
def home():
    try:
        if 'idname' not in session:
            return render_template("login.html")
        elif 'idname' in session: 
            return render_template('container.html')
        else:
            return render_template("login.html")
    except:
        return redirect(url_for('errorpage'))

@app.route('/login', methods=['GET','POST'])
def login():
        if request.method == 'POST':
            username= request.form['idname']
            password= request.form['password']
            cursor= mysql.connection.cursor()
            cursor.execute('SELECT * FROM tk_canbo WHERE username= %s AND password= %s',(username,password))
            check = cursor.fetchone()
            if check:
                session['idname'] = request.form['idname']
                return redirect(url_for('home'))
            else:
                # Account doesnt exist or username/password incorrect
                msg = 'Incorrect username/password!'
        # Show the login form with message (if any)
        return render_template('login.html', msg=msg)
@app.route('/logout')
def logout():
    try:
        session.pop('idname', None)
        return render_template("login.html")
    except:
        return redirect(url_for('errorpage'))
@app.route('/home')
def homeadmin():
    try:
        if 'idname' in session:
            return render_template('container.html')
    except:
        return redirect(url_for('errorpage'))

@app.route('/errorpage')
def errorpage():
    return render_template('errorpage.html')