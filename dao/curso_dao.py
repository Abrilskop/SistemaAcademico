# dao/curso_dao.py
from modelos.curso import Curso

class CursoDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def listar(self):
        return self.conexion.ejecutarsinparametros("sp_listar_cursos")

    def operar(self, accion, curso: Curso):
        parametros = [
            accion,
            curso.id,
            curso.nombre,
            curso.creditos
        ]
        return self.conexion.ejecutar("sp_curso", parametros)