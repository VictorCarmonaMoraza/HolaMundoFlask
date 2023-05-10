from flask import Flask, request
app = Flask(__name__)

#http://localhost:5000
@app.route('/')
def inicio():
    app.logger.info(f'Entramos al path {request.path}')
    return '<h1>Hello Mundo desde Flask2!</h1>'