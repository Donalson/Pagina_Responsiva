#Importacion de flask para crear y ejecutar sitio web, renderizar plantillas
from flask import Flask, render_template

#Instanciacion de flask dentro de la variable app
app = Flask(__name__)

#Creacion de la ruta principal del sitio web
@app.route('/')
def Inicio():
    return render_template('Index.html')

@app.route("/Productos")
def Productos():
    return render_template('Productos.html')

@app.route("/ServicioTecnico")
def Servicios():
    return render_template('Servicios.html')

@app.route("/Contactanos")
def Contactanos():
    return render_template('Contactanos.html')

#Inializacion del sitio web para correr(modo debug encendido para detectar cambios)
if __name__ == '__main__':
    app.run(debug=True)