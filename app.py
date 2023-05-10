from flask import Flask
app = Flask(__name__)

#http://localhost:5000
@app.route('/')
def inicio():
    return '<h1>Hello Mundo desde Flask2!</h1>'