from flask import Flask,render_template,request,redirect,make_response,jsonify
from demo_memcache import add,delete1,update1,read,clear_memcache

#creating the flask app
 
app = Flask(__name__)
keys = set()

#add function 
@app.route("/add",methods=['POST','GET'])
def add1():
    if request.method == "POST":
        try:
            Id1= request.form['Id']
            keys.add(Id1)
            Name1 = request.form['Name']
            Salary1 = request.form['Salary']
            Designation = request.form['Desig']
            #Data.update({Id :{"Name":Name,"Salary":Salary,"Design":Designation}})
            try:
                da=add(Id1,{"Name":Name1,"Salary":Salary1,"Design":Designation},keys)
            except Exception as ee:
                return "cannot add  " + str(ee)
        except Exception as e:
            return "missing fields  " + str(e)
        return jsonify(data = da)

    return jsonify(data = "U made a get request")
       
    

#delete task
@app.route("/delete",methods = ['POST','GET'])
def delf():
    if request.method == "POST":
        try:
            Id=request.form['Id']
            try:
                keys.remove(Id)
                ddata=delete1(Id,keys)
            except Exception as k:
                return "Deletion not possible,Id does not exist  " + str(k)
        except Exception as e:
            return "check the field  " + str(e)
        return jsonify(data = ddata)
    
    return jsonify(data = "You made a get request,Please make sure to do a POST request with ID parameter")
        
#update task
@app.route("/update",methods = ['POST','GET'])
def updat():
    if request.method == "POST":
        try:
            Id=request.form['Id']
            Name1= request.form['Name']
            Design1= request.form['Desig']
            Salary1 = request.form['Salary']
            try:    
                udata=update1(Id,Name1,Salary1,Design1,keys)
            except Exception as t:
                return "cannot update,ID not found  " + str(t)
        except Exception as e:
            return "missing field  " + str(e)
        return jsonify(data =udata)
    
    return jsonify(data = "Please Use POST request and Send relevant data for updating.")

@app.route("/read",methods = ['GET','POST'])
def read1():
    return jsonify(data=read(keys))

#welcome        
@app.route("/",methods = ['GET','POST'])
def welcome():
    status = clear_memcache()
    if status == True:
        return jsonify(data = "Welcome to the CRUD App")
    else:
        return jsonify(data = "There is a problem flushing the memcache ,App is down")
#running the app

# if __name__ =='__main__':
#     app.run(host='127.0.0.1',port=5001,debug=True)
