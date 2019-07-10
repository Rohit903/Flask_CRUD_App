from flask import Flask,render_template,request,redirect,make_response,jsonify

#creating the flask app

Data = {"1":{"Name":"ROhith","Salary":"55555","Design":"SD"},
            "2":{"Name":"ROhith","Salary":"33333","Design":"SD"},
            "3":{"Name":"ROhith","Salary":"77777","Design":"SD"}}

app = Flask(__name__)

#add function 
@app.route("/add",methods=['POST','GET'])
def add():
    if request.method == "POST":
        try:
            Id= request.form['Id']
            Name = request.form['Name']
            Salary = request.form['Salary']
            Designation = request.form['Desig']
            Data.update({Id :{"Name":Name,"Salary":Salary,"Design":Designation}})
        except Exception as e:
            return "there is a problem with the fileds you are sendings"
        return jsonify(data = Data)
    else:
        return jsonify(data = "U made a get request")
       
    

#delete task
@app.route("/delete",methods = ['POST','GET'])
def delf():
    if request.method == "POST":
        try:
            Id=request.form['Id']
            try:
                print(Data.pop(Id))
            except KeyError:
                return "Id not found in the dictionary"
        except Exception as e:
            return "Deletion not possible,check if the fields are sent properly"
        return jsonify(data = Data)
    else:
        return jsonify(data = "You made a get request,Please make sure to do a POST request with ID parameter")
        
#update task
@app.route("/update",methods = ['POST','GET'])
def updat():
    if request.method == "POST":
        try:
            Id=request.form['Id']
            Field=request.form['Field']
            Value=request.form['Value']
            try:
                dat=Data.get(Id)
                dat[Field] = Value
            except TypeError:
                return "ID not found in the Dictionary"
        except Exception as e:
            return "Updation not possible because fields might have not sent properly"
        return jsonify(data =Data)
    else:
        return jsonify(data = "Please Use POST request and Send relevant data for updating.")
#welcome        
@app.route("/",methods = ['GET','POST'])
def welcome():
    return jsonify(data = Data)
#running the app

if __name__ =='__main__':
    app.run(host='127.0.0.1',port=5001,debug=True)
