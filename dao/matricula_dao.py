# dao/matricula_dao.py
from modelos.matricula import Matricula

class MatriculaDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def listar(self):
        return self.conexion.ejecutarsinparametros("sp_listar_matriculas")

    def operar(self, accion, matricula: Matricula):
        parametros = [
            accion,
            matricula.id,
            matricula.id_estudiante,
            matricula.id_curso,
            matricula.ciclo
        ]
        return self.conexion.ejecutar("sp_matricula", parametros)