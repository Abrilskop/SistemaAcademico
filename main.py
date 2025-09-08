from flask import Flask
from controladores.escuela_controller import EscuelaController

app = Flask(__name__)

# Ruta principal para mostrar todas las escuelas (GET)
@app.route('/')
def mostrar_escuelas():
    controlador = EscuelaController()
    response = controlador.mostrar_escuelas()
    controlador.cerrar()
    return response

# Ruta para agregar una nueva escuela (POST)
@app.route('/escuela/agregar', methods=['POST'])
def agregar_escuela():
    controlador = EscuelaController()
    response = controlador.agregar_escuela()
    controlador.cerrar()
    return response

# Ruta para editar una escuela (POST)
@app.route('/escuela/editar/<int:id>', methods=['POST'])
def editar_escuela(id):
    controlador = EscuelaController()
    response = controlador.editar_escuela(id)
    controlador.cerrar()
    return response

# Ruta para eliminar una escuela (POST)
@app.route('/escuela/eliminar/<int:id>', methods=['POST'])
def eliminar_escuela(id):
    controlador = EscuelaController()
    response = controlador.eliminar_escuela(id)
    controlador.cerrar()
    return response

if __name__ == '__main__':
    app.run(debug=True)