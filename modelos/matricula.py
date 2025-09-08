# modelos/matricula.py
class Matricula:
    def __init__(self, id=None, id_estudiante=None, id_curso=None, ciclo=None):
        self.id = id
        self.id_estudiante = id_estudiante
        self.id_curso = id_curso
        self.ciclo = ciclo