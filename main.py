from  flask import Flask,render_template,request
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config["MYSQL_HOST"]="shilpadb1.chktnc8hi8cd.us-east-1.rds.amazonaws.com"
app.config["MYSQL_USER"]="admin"
app.config["MYSQL_PASSWORD"]="Bhuvi0501"
app.config["MYSQL_DB"]="shilpadb1"
mysql=MySQL(app)
@app.route("/")
def home():
    return render_template("result.html")
@app.route("/detail",methods=["GET","POST"])
def result():
    if request.method=="POST":
        n1=int(request.form["num1"])
        n2 = int(request.form["num2"])
        result=n1+n2
        cur=mysql.connection.cursor()
        cur.execute("insert into record(num1,num2,total) values(%s,%s,%s)",(n1,n2,result))
        cur.connection.commit()
        cur.close()
        return render_template('result.html',result=result)
if __name__=="__main__":
    app.run()