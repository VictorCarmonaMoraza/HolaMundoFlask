

from flask import Flask, request, render_template,url_for,jsonify, session
from werkzeug.utils import redirect
from werkzeug.exceptions import abort

app = Flask(__name__)

app.secret_key= 'Mi_llave_secreta'

#GET
#http://localhost:5000
@app.route('/')
def inicio():
    if 'username' in session:
        return 'El usuario ya ha hecho login'
    return '<h1>No ha hecho login</h1>'

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')


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

#REST Representational state transfer
#Acepta metodo de tipo GET y de tipo POST
@app.route('/api/mostrar/<nombre>', methods=['GET','POST'])
def mostrar_json(nombre):
    #Agregamos al dicionario el nombre y el tipo de metodo
    valores ={'nombre':nombre, 'metodo_http':request.method}
    #Transforma la respuesta en un diccionario de tipo json
    return jsonify(valores)

#Acepta metodo solo de tipo GET
@app.route('/api/mostrar1/<nombre>')
def mostrar_json1(nombre):
    #Agregamos al dicionario el nombre y el tipo de metodo
    valores ={'nombre':nombre, 'metodo_http':request.method}
    #Transforma la respuesta en un diccionario de tipo json
    return jsonify(valores)