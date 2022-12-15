from flask import Flask, render_template, request, redirect, url_for, session, flash, g, app
from logging.config import dictConfig
import re, json
from pymysql import connect, cursors

app = Flask(__name__)

# convert DB response to required format for usage in HTML
def preprocess_tuples(data: list):
    if data:
        header = list(data[0].keys())
        rows = list(map(lambda x:list(x.values()), data))
        return {"header":header, "rows":rows}
    return {"header":[], "rows":[]}

# connect to DB
try:
    connection = connect(
            host="localhost",
            user="root",
            password="Sh_reyasi03",
            database="finalproject",
            charset="utf8mb4",
            cursorclass=cursors.DictCursor
        )

except Exception as e:
    app.logger.info(e)

# reset the session
@app.before_request
def before_request():
    g.user = None
    if 'username' in session:
        g.user = session['username']


# validate login credentials and/or show login page
@app.route("/", methods=['POST', 'GET'])
def login():
    cursor = connection.cursor()
    if request.method == "POST":

        tempUseremail = request.form['login_email']
        tempPassword = request.form['login_password']
        cursor.callproc("check_user", [tempUseremail, tempPassword])
        temp = cursor.fetchall()
        connection.commit()

        if (temp[0]['response'] == "yes"):
            session['loggedin'] = True
            session['username'] = tempUseremail
            g.user = tempUseremail
            flash("Logged in successfully")
            return redirect(url_for('home'))
        else:
            flash("Invalid Email or Password")
            session['username'] = None
            return render_template("login.html")

    return render_template("login.html")


# home page after login
@app.route('/home')
def home():
    return render_template('shortlist.html', data={"header":[], "rows":[]})

# clear session and go back to login page for logout
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    g.user = None
    flash("Successfully logged out")
    return redirect(url_for('login'))

# If new user, register
@app.route("/register", methods=['POST', 'GET'])
def register():
    cursor = connection.cursor()
    if request.method == "POST":
        firstName = request.form['register_firstname']
        lastName = request.form['register_lastname']
        email_address = request.form['register_email']
        password = request.form['register_password']
        address = request.form['register_address']
        phone = request.form['register_phone']

        cursor.callproc("create_user", [firstName, lastName, address, phone, email_address, password])
        temp = cursor.fetchall()
        connection.commit()
        app.logger.info(temp)
        if (temp[0]['response'] == 1):
            flash("Successfully registered")
            return redirect(url_for('login'))
        if (temp[0]['response'] == 0):
            flash("Invalid Details")
    return render_template("register.html")


# Send user requirements to DB and populate the UI with the response
@app.route("/shortlist", methods=['POST', 'GET'])
def shortlist_unis():
    if g.user:
        cursor = connection.cursor()
        if request.method == "POST":
            gre_ = request.form['gre']
            toefl_ = request.form['toefl']
            cgpa_ = request.form['cgpa']
            cursor.callproc("shortlist", args=[gre_, toefl_, cgpa_])
            result = cursor.fetchall()
            connection.commit()
            app.logger.info(result)

            return render_template("shortlist.html",
                                   data=preprocess_tuples(result))
        return render_template("shortlist.html",data={"header":[], "rows":[]})
    else:
        return redirect(url_for('login'))


# start the flask app
if __name__=="__main__":
    app.secret_key = '1234567890somesh'
    app.run(host="localhost", port=8080, debug=True)