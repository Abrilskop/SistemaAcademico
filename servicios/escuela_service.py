from modelos.escuela import Escuela

class EscuelaService:
    def __init__(self, dao):
        self.dao = dao

    # El método para crear ya existe, pero lo ajustamos si es necesario
    def crear(self, nombre):
        escuela = Escuela(nombre=nombre)
        return self.dao.operar("I", escuela)

    def listar(self):
        return self.dao.listar()

    # NUEVO: Método para actualizar
    def actualizar(self, id, nombre):
        escuela = Escuela(id=id, nombre=nombre)
        return self.dao.operar("U", escuela)

    # NUEVO: Método para eliminar
    def eliminar(self, id):
        escuela = Escuela(id=id) # Solo necesitamos el ID para eliminar
        return self.dao.operar("D", escuela)
    
    # === NUEVO MÉTODO PARA BUSCAR ===
    def buscar_por_nombre(self, nombre):
        return self.dao.buscar_por_nombre(nombre)