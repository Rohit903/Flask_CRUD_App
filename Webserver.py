from flask import Flask,render_template,request,redirect,make_response,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#creating the flask app

app = Flask(__name__)

#add function 
@app.route("/add",methods=['POST','GET'])
def add():
    if request.method == "POST":
        try:
            Emp_id = request.form['Id']
            Name = request.form['Name']
            Salary = request.form['Salary']
            Designation = request.form['Desig']
        except Exception as e:
            return "there is a problem with the fileds you are sendings"
        return jsonify(data = "data added")
       
    

#delete task
@app.route("/delete",methods = ['POST','GET'])
def delf():
    if request.method == "POST":
        try:
            Id=request.form['Id']
        except Exception as e:
            return "deletion not possible"
        return jsonify(data = "deleted the Id")
        
#update task
@app.route("/update",methods = ['POST','GET'])
def updat():
    if request.method == "POST":
        try:
            Id=request.form['Id']
            Field=request.form['Field']
            Val=request.form['Value']
        except Exception as e:
            return "updation not possible because fields might have not sent properly"
        return jsonify(data = "updated the details")
       

#running the app

if __name__ =='__main__':
    app.run(host='127.0.0.1',port=5001,debug=True)