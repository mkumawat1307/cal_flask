from flask import Flask,request,render_template
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Flask"

@app.rroute("Calculator", method =["GET","POST"])
def math_opretion():
    operation = request.json["operation"]
    n1 = request.json["number1"]
    n2 = request.json["number2"]
    
    if operation=="add":
        result = n1+n2
    elif operation=="multiply":
        result = n1*n2
    elif operation=="division":
        result = n1/n2
    else:
        result = n1-n2
        
    return result


if __name__=="__main__":
    app.run(debug=True)