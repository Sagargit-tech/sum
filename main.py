from  flask import Flask,render_template,request
from flask_mysqldb import MySQL
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("result.html")
@app.route("/detail",methods=["GET","POST"])
def result():
    if request.method=="POST":
        n1=int(request.form["num1"])
        n2 = int(request.form["num2"])
        result=n1+n2
        return render_template('result.html',result=result)
if __name__=="__main__":
    app.run()
