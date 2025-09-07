from modelos.escuela import Escuela

class EscuelaDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def operar(self, accion, escuela: Escuela):
        return self.conexion.ejecutar("sp_escuela", [accion, escuela.id, escuela.nombre])
    
    
    def listar(self): 
        return self.conexion.ejecutarsinparametros("sp_listar_escuela")