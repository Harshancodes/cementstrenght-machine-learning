from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_mail import Mail, Message




#application= Flask(_name_)
app=Flask(__name__)
model=pickle.load(open('models/cement.pkl','rb'))
local_server=True
app.secret_key="harshan"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/payment'  # For SQLite
# or for a PostgreSQL database:
#Example configuration for SQLAlchemy with MySQL Connector/Python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/payment'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/your-database'

db=SQLAlchemy(app)
class Cem(db.Model):
    q=db.Column(db.Integer,primary_key=True)
    s=db.Column(db.Integer)
    t=db.Column(db.Integer)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'harshan4098415@gmail.com'  # Use your actual Gmail address
app.config['MAIL_PASSWORD'] = 'ydvsdroczscrzanu'     # Use your generated App Password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

# @app.route("/email")
# def index():
#     msg = Message(
#         subject='Hello from the other side!', 
#         sender='your_email@gmail.com',  # Ensure this matches MAIL_USERNAME
#         recipients=['sharanyae.shada@gmail.com']  # Replace with actual recipient's email
#     )
#     msg.body = "Hey, sending you this email from my Flask app, let me know if it works."
#     mail.send(msg)
#     return "Message sent!"
@app.route("/")
def welcome():
    #a=Cem.query.all()
    #print(a)
    return render_template("w.html")
@app.route("/home")
def homeb():
    return render_template("home.html")
@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method=="POST":
        username=request.form.get('username')
        email=request.form.get("email")
        password=request.form.get("password")
        print(username,email,password)
    return render_template("signup.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/knm")
def knm():
    return render_template("knm.html")
@app.route("/feedback")
def feedback():
    return render_template("feedback.html")
@app.route("/predict",methods=["GET","POST"])
def hello_world():
    if request.method=='POST':
        Cement=float(request.form.get('Cement'))
        BlastFurnaceSlag=float(request.form.get('BlastFurnaceSlag'))
        FlyAsh=float(request.form.get('FlyAsh'))
        Water=float(request.form.get('Water'))
        Superplasticizer=float(request.form.get('Superplasticizer'))
        Coarse=float(request.form.get('Coarse'))
        FineAggregate=float(request.form.get('FineAggregate'))
        Age=float(request.form.get('Age'))
        result=model.predict([[ Cement, BlastFurnaceSlag,FlyAsh,Water,Superplasticizer, Coarse,FineAggregate,Age]])
        if(result<0):
           result=-result
        return render_template('index.html',results=result[0])

    # else:
    return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5001,debug=True)