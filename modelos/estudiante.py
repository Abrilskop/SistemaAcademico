# modelos/estudiante.py
class Estudiante:
    def __init__(self, id=None, nombres=None, apellidos=None, correo=None, id_escuela=None):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo
        self.id_escuela = id_escuela