from flask import Flask
from controladores.escuela_controller import EscuelaController

app = Flask(__name__)

@app.route('/')
def mostrar_escuela():
    controlador = EscuelaController()  # Crear una instancia de EscuelaController
    html = controlador.mostrar_escuela()  # Obtener el HTML generado por el controlador
    controlador.cerrar()  # Si tienes algún proceso de cierre, lo llamas aquí
    return html  # Devolver el HTML como respuesta

if __name__ == '__main__':
    app.run(debug=True)
