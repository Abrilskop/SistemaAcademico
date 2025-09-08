from flask import Flask
from controladores.escuela_controller import EscuelaController
from controladores.estudiante_controller import EstudianteController

app = Flask(__name__)

# Esta clave se usa para firmar las sesiones y los mensajes flash.
app.secret_key = 'dev-sistema-academico-2025'

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

# === RUTAS PARA ESTUDIANTES ===
@app.route('/estudiantes')
def mostrar_estudiantes():
    controlador = EstudianteController()
    response = controlador.mostrar_estudiantes()
    controlador.cerrar()
    return response

@app.route('/estudiante/agregar', methods=['POST'])
def agregar_estudiante():
    controlador = EstudianteController()
    response = controlador.agregar_estudiante()
    controlador.cerrar()
    return response

@app.route('/estudiante/editar/<int:id>', methods=['POST'])
def editar_estudiante(id):
    controlador = EstudianteController()
    response = controlador.editar_estudiante(id)
    controlador.cerrar()
    return response

@app.route('/estudiante/eliminar/<int:id>', methods=['POST'])
def eliminar_estudiante(id):
    controlador = EstudianteController()
    response = controlador.eliminar_estudiante(id)
    controlador.cerrar()
    return response

if __name__ == '__main__':
    app.run(debug=True)