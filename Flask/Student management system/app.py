from flask import Flask,render_template,request,redirect,url_for ,session
from werkzeug.security import generate_password_hash,check_password_hash
from cryptography.fernet import Fernet

import mysql.connector as mysql
import bcrypt

app = Flask(__name__)    # Object for Flask class
con = mysql.connect(host="localhost",
                     user="root",
                     password="vamsi@2004ABC",
                     database="student_flask"
                     )

app.secret_key = "123456789"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/authentication")
def authentication():
    return render_template("authentication.html")

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/view")
def view():
    if "user" in session:
        cur = con.cursor()
        cur.execute("select * from student")
        result = cur.fetchall()
        return render_template("view.html",result=result)
    else:
        return render_template("login.html")
    

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        id = request.form.get("id")
        password = request.form.get("password")
        cur = con.cursor()
        query = "select * from student where id = %s and password = %s"
        values = (id,password)
        cur.execute(query,values)
        result = cur.fetchone()
        if result:
          session['id'] = result[0]
          session['firstname'] = result[1]
          session['user'] = result[2]
          return redirect(url_for('dashboard'))
        else:
          return redirect(url_for('login'))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect('login')

@app.route("/update/<int:id>/",methods=["POST","GET"])
def update(id):
    cur = con.cursor()
    cur.execute("select * from student where id = %s", (id,))
    result = cur.fetchone()
    if request.method == "POST":
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        password = request.form.get("password")
        gender = request.form.get("gender")
        mobileno = request.form.get("mobileno")
        course = request.form.get("course")
        department = request.form.get("department")
        guardian_name = request.form.get("guardian_name")
        address = request.form.get("address")
        cur = con.cursor()
        query = """update student set firstname = %s, lastname = %s, password = %s,
                gender = %s, mobileno = %s,  course = %s, department = %s, guardian_name = %s,
                address = %s where id = %s"""
        values = (firstname,lastname,password,gender,mobileno,course,department,
                  guardian_name,address,id)
        cur.execute(query,values)
        con.commit()
        return redirect(url_for('view'))
    return render_template("update.html",result=result)

@app.route("/delete/<int:id>/",methods=["POST","GET"])
def delete(id):
    cur = con.cursor()
    cur.execute("delete from student where id = %s", (id,))
    con.commit()
    return redirect(url_for('view'))

@app.route("/registration",methods=["POST","GET"])
def registration():
    if request.method == "POST":
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        password = request.form.get("password")
        gender = request.form.get("gender")
        mobileno = request.form.get("mobileno")
        course = request.form.get("course")
        department = request.form.get("department")
        guardian_name = request.form.get("guardian_name")
        address = request.form.get("address")
        cur = con.cursor()
        query = """insert into student(firstname,lastname,password,gender,
                   mobileno,course,department,guardian_name,address)
                   values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (firstname,lastname,password,gender,
                   mobileno,course,department,guardian_name,address)
        cur.execute(query,values)
        con.commit()
        return redirect(url_for("login"))
    return render_template("registration.html")

    
@app.route("/hashing1")
def hashing1():
    data = "student_no_1"
    result = generate_password_hash(data)
    if check_password_hash(result,data):
        return "Both Are Same"
    else:
        return "Both Are Not Same"

@app.route("/hashing2")
def hashing2():
    data = "student_no_1"
    data = data.encode()
    salt = bcrypt.gensalt()
    result = bcrypt.hashpw(data,salt)
    if bcrypt.checkpw("student_no_1".encode(),result):
        return "Both Are Same"
    else:
        return "Both Are Not Same"

@app.route("/encrypt")
def encryption():
    data = "student1234"
    key = Fernet.generate_key() # generating key
    data = data.encode() # Data into bytes
    f1 = Fernet(key) # Object For Key
    encrypt_data = f1.encrypt(data)
    decrypt_data = f1.decrypt(encrypt_data)
    return (decrypt_data)


if __name__ == "__main__":
    app.run(debug=True,port=12000,host="localhost")


