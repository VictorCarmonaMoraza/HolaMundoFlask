from flask import Flask, request
app = Flask(__name__)

#http://localhost:5000
@app.route('/')
def inicio():
    app.logger.info(f'Entramos al path {request.path}')
    return '<h1>Hello Mundo desde Flask2!</h1>'


@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre.upper()}'

@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
        if edad >25:
            return f'Tu edad es: {edad + 5}'
        else:
            return f'Tu edad es: {edad +1}'