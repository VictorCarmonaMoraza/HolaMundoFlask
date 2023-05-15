

from flask import Flask, request, render_template,url_for
from werkzeug.utils import redirect
from werkzeug.exceptions import abort

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

#POST AND GET
@app.route('/mostrar/<valor_nombre>', methods=['GET','POST'])
def mostrar_nombre(valor_nombre):
    # La variable que se utiliza en el template es nombre
    return render_template('mostrar.html',nombre=valor_nombre)


#GET
#@app.route('/redireccionar')
#def redireccionar():
    #Redireccionamos a la funcion de inicio
    #return  redirect(url_for('inicio'))

#GET Opcion 2
@app.route('/redireccionar')
def redireccionar():
    #Redireccionamos a la funcion de mostrar_nombre
    return redirect(url_for('mostrar_nombre', valor_nombre='Victor'))

@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return (render_template('error404.html', error=error), 404)
