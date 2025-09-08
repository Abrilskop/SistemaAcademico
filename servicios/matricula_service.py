# servicios/matricula_service.py
from modelos.matricula import Matricula

class MatriculaService:
    def __init__(self, dao):
        self.dao = dao

    def listar(self):
        return self.dao.listar()

    def crear(self, id_estudiante, id_curso, ciclo):
        matricula = Matricula(id_estudiante=id_estudiante, id_curso=id_curso, ciclo=ciclo)
        return self.dao.operar("I", matricula)

    def actualizar(self, id, id_estudiante, id_curso, ciclo):
        matricula = Matricula(id=id, id_estudiante=id_estudiante, id_curso=id_curso, ciclo=ciclo)
        return self.dao.operar("U", matricula)

    def eliminar(self, id):
        matricula = Matricula(id=id)
        return self.dao.operar("D", matricula)