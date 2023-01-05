from flask import Flask, render_template
import math

app = Flask(__name__)

@app.route("/")
def hello_monty():
    return "Hello Monty!"

@app.route("/math")
def hello_math():
    equation = math.floor(15 * 20 / .33)
    return str(equation)

@app.route("/business")
def html_business():
    return render_template("business.html")