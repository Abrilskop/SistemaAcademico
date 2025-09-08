# servicios/estudiante_service.py
from modelos.estudiante import Estudiante

class EstudianteService:
    def __init__(self, dao):
        self.dao = dao

    def listar(self):
        return self.dao.listar()

    def crear(self, nombres, apellidos, correo, id_escuela):
        estudiante = Estudiante(nombres=nombres, apellidos=apellidos, correo=correo, id_escuela=id_escuela)
        return self.dao.operar("I", estudiante)

    def actualizar(self, id, nombres, apellidos, correo, id_escuela):
        estudiante = Estudiante(id=id, nombres=nombres, apellidos=apellidos, correo=correo, id_escuela=id_escuela)
        return self.dao.operar("U", estudiante)

    def eliminar(self, id):
        estudiante = Estudiante(id=id)
        return self.dao.operar("D", estudiante)