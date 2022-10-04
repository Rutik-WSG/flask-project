from flask import Flask ,redirect,request,render_template

from database import addata ,fetchdata ,specificdata , updatedata , deletedata
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home1.html")

@app.route("/infolink")
def info():
    return render_template("info.html")

@app.route("/home1")
def home1():
    return render_template("home1.html")

@app.route("/savelink",methods=["POST"])
def save():
    name=request.form["uname"]
    password=request.form["pass"]
    email=request.form["email"]
    city=request.form["city"]
    t=(name,password,email,city)
    addata(t)
    return redirect("infolink")

@app.route("/show")
def showfun():
    datalist=fetchdata()
    return render_template("show.html",data=datalist)

@app.route("/editlink/<int:id>")
def displayforupdate(id):
    datalist=specificdata(id)
    return render_template("edit.html",data=datalist)

@app.route("/updatelink/<int:id>",methods=["POST"])
def updatefun(id):
    name=request.form["uname"]
    password=request.form["pass"]
    city=request.form["city"]
    email=request.form["email"]
    t=(name,password,city,email,id)
    updatedata(t)
    return redirect("/show")

@app.route("/deletelink/<int:id>")
def deletefun(id):
    deletedata(id)
    return redirect("/show") 


if __name__=='__main__':
    app.run(debug=True)