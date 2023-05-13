from flask import Flask, request, render_template

app = Flask(__name__)

#GET
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

#POST

@app.route('/mostrar/<valor_nombre>', methods=['GET','POST'])
def mostrar_nombre(valor_nombre):
    # La variable que se utiliza en el template es nombre
    return render_template('mostrar.html',nombre=valor_nombre)