# servicios/curso_service.py
from modelos.curso import Curso

class CursoService:
    def __init__(self, dao):
        self.dao = dao

    def listar(self):
        return self.dao.listar()

    def crear(self, nombre, creditos):
        curso = Curso(nombre=nombre, creditos=creditos)
        return self.dao.operar("I", curso)

    def actualizar(self, id, nombre, creditos):
        curso = Curso(id=id, nombre=nombre, creditos=creditos)
        return self.dao.operar("U", curso)

    def eliminar(self, id):
        curso = Curso(id=id)
        return self.dao.operar("D", curso)