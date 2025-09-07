from modelos.escuela import Escuela

class EscuelaService:
    def __init__(self, dao):
        self.dao = dao

    def crear(self, nombre):
        escuela = Escuela(nombre=nombre)
        return self.dao.operar("I", escuela)

    def listar(self):
        return self.dao.listar()