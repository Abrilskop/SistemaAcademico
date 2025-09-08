from flask import Flask
from controladores.escuela_controller import EscuelaController
from controladores.estudiante_controller import EstudianteController
from controladores.curso_controller import CursoController
from controladores.matricula_controller import MatriculaController

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

# === RUTAS PARA CURSOS ===
@app.route('/cursos')
def mostrar_cursos():
    controlador = CursoController()
    response = controlador.mostrar_cursos()
    controlador.cerrar()
    return response

@app.route('/curso/agregar', methods=['POST'])
def agregar_curso():
    controlador = CursoController()
    response = controlador.agregar_curso()
    controlador.cerrar()
    return response

@app.route('/curso/editar/<int:id>', methods=['POST'])
def editar_curso(id):
    controlador = CursoController()
    response = controlador.editar_curso(id)
    controlador.cerrar()
    return response

@app.route('/curso/eliminar/<int:id>', methods=['POST'])
def eliminar_curso(id):
    controlador = CursoController()
    response = controlador.eliminar_curso(id)
    controlador.cerrar()
    return response

# === RUTAS PARA MATRÍCULAS ===
@app.route('/matriculas')
def mostrar_matriculas():
    controlador = MatriculaController()
    response = controlador.mostrar_matriculas()
    controlador.cerrar()
    return response

@app.route('/matricula/agregar', methods=['POST'])
def agregar_matricula():
    controlador = MatriculaController()
    response = controlador.agregar_matricula()
    controlador.cerrar()
    return response

@app.route('/matricula/editar/<int:id>', methods=['POST'])
def editar_matricula(id):
    controlador = MatriculaController()
    response = controlador.editar_matricula(id)
    controlador.cerrar()
    return response

@app.route('/matricula/eliminar/<int:id>', methods=['POST'])
def eliminar_matricula(id):
    controlador = MatriculaController()
    response = controlador.eliminar_matricula(id)
    controlador.cerrar()
    return response

if __name__ == '__main__':
    app.run(debug=True)