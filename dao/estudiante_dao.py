# dao/estudiante_dao.py
from modelos.estudiante import Estudiante

class EstudianteDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def listar(self):
        return self.conexion.ejecutarsinparametros("sp_listar_estudiante")

    def operar(self, accion, estudiante: Estudiante):
        parametros = [
            accion,
            estudiante.id,
            estudiante.nombres,
            estudiante.apellidos,
            estudiante.correo,
            estudiante.id_escuela
        ]
        return self.conexion.ejecutar("sp_estudiante", parametros)