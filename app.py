from flask import Flask,request,render_template,jsonify
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/",methods=["POST"])
def math_opretion():
    operation = request.form.get("Operation")
    n1 = request.form.get("Number1")
    n2 = request.form.get("Number2")
    
    if operation=="Addition":
        result = int(n1)+int(n2)
    elif operation=="Subtraction":
        result = int(n1)-int(n2)
    elif operation=="Multiplication":
        result = int(n1)*int(n2)
    elif operation=="Division":
        result = int(n1)/int(n2)
        
    return render_template("index.html", result=result)


if __name__=="__main__":
    app.run(debug=True)