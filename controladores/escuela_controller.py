from servicios.escuela_service import EscuelaService
from dao.escuela_dao import EscuelaDAO
from conexion import Conexion
from vistas.generador_html import GeneradorHTML

class EscuelaController:
    def __init__(self):
        self.conexion = Conexion()
        self.dao = EscuelaDAO(self.conexion)
        self.servicio = EscuelaService(self.dao)
        self.vista = GeneradorHTML()

    def mostrar_escuela(self):
        datos = self.servicio.listar()
        html = self.vista.generar_escuela_html(datos)
        return html

    def cerrar(self):
        self.conexion.cerrar()