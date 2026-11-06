from flask import Flask,render_template,request,redirect,url_for,session
from werkzeug.security import generate_password_hash,check_password_hash
from cryptography.fernet import Fernet

import mysql.connector as mysql
import bcrypt

app = Flask(__name__)    # Object for Flask class
con = mysql.connect(host="localhost",user="root",password="vamsi@2004ABC",database="employee_flask")

app.secret_key = "123456789"

@app.route("/")   # Default page for server
def home():    
    return render_template('home.html')    # Render_template - To show html template
@app.route("/contact") 

def contact():    
    return render_template('contact.html')    
@app.route("/dashboard")  


def dashboard():    
    return render_template('dashboard.html')
    
@app.route("/data")   
def data():   
    if "user" in  session:
        cur = con.cursor() 
        cur.execute("select * from employee")
        result = cur.fetchall()
        return render_template('data.html',result=result) 
    else:
        return render_template("login.html")

@app.route("/login",methods=["POST","GET"]) 
def login():
    if request.method == "POST":
        email =  request.form.get("email")
        password =  request.form.get("password")
        cur = con.cursor()
        query = "select * from employee where email = %s and password = %s"
        values = (email,password)
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

@app.route("/services")   
def services():    
    return render_template('services.html') 

@app.route("/signup",methods=["POST","GET"])   
def signup():    

    if request.method == "POST":
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        password = request.form.get("password")
        location = request.form.get("location")
        zipcode = request.form.get("zipcode")
        mobileno = request.form.get("mobileno")
        cur = con.cursor()
        query = """insert into employee(firstname,lastname,email,password,location,zipcode,mobileno) values(%s,%s,%s,%s,%s,%s,%s)"""
        values = (firstname,lastname,email,password,location,zipcode,mobileno)
        cur.execute(query,values)
        con.commit()
        return redirect(url_for('login')) 
    return render_template('signup.html')

@app.route("/update/<int:id>/",methods=["POST","GET"])
def update(id):
    cur = con.cursor()
    cur.execute("select * from employee where id = %s",(id,))
    result = cur.fetchone()
    if request.method == "POST":
            firstname = request.form.get("firstname")
            lastname = request.form.get("lastname")
            email = request.form.get("email")
            password = request.form.get("password")
            location = request.form.get("location")
            zipcode = request.form.get("zipcode")
            mobileno = request.form.get("mobileno")
            cur = con.cursor()
            query = """update employee set firstname = %s, lastname = %s, email = %s, password = %s,
                    location = %s, zipcode = %s, mobileno = %s where id = %s"""
            values = (firstname,lastname,email,password,location,zipcode,mobileno,id)
            cur.execute(query,values)
            con.commit()
            return redirect(url_for('data'))
    con.commit()
    return render_template('update.html',result=result)

@app.route("/delete/<int:id>/",methods=["POST","GET"])
def delete(id):
    cur = con.cursor()
    cur.execute("delete from employee where id = %s", (id,))
    con.commit()
    return redirect(url_for('data'))

@app.route("/hashing1")
def hashing1():
    data = "hello1234"
    result = generate_password_hash(data)
    if check_password_hash(result,"hello1234"):
        return "Both Are Same"
    else:
        return "Both Are Not Same"

@app.route("/hashing2")
def hashing2():
    data = "hello1234"
    data = data.encode() # Convert the data into bytes
    salt = bcrypt.gensalt()  # Generating the salt
    result = bcrypt.hashpw(data,salt)
    if bcrypt.checkpw("hello1234".encode(),result):
        return "Both are same"
    else:
        return "Both are not same"

@app.route("/encrypt")
def encryption():
    data = "hello1234"
    key = Fernet.generate_key() # step 1: Generating key
    data = data.encode() # step 2: Convert Data into Bytes
    f1 = Fernet(key) # step 3: Creating object for fernet class using key
    encrypted_data = f1.encrypt(data) # step 4: Encryption
    decrypted_data = f1.decrypt(encrypted_data) # step 5: Decryption
    return decrypted_data
    

if __name__ == "__main__":
    app.run(debug=True,port=12000,host="localhost")
