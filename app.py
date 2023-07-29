from flask import Flask,request,render_template,jsonify
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Flask"

@app.route("/Calculator",methods=["GET", "POST"])
def math_opretion():
    operation = request.json["operation"]
    n1 = request.json["number1"]
    n2 = request.json["number2"]
    
    if operation=="add":
        result = int(n1)+int(n2)
    elif operation=="multiply":
        result = int(n1)*int(n2)
    elif operation=="division":
        result = int(n1)/int(n2)
    else:
        result = int(n1)-int(n2)
        
    return jsonify(result)


if __name__=="__main__":
    app.run(debug=True)