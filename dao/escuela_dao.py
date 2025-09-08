from modelos.escuela import Escuela

class EscuelaDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def operar(self, accion, escuela: Escuela):
        return self.conexion.ejecutar("sp_escuela", [accion, escuela.id, escuela.nombre])
    
    def listar(self): 
        return self.conexion.ejecutarsinparametros("sp_listar_escuela")
    
    # === NUEVO MÉTODO PARA BUSCAR ===
    def buscar_por_nombre(self, nombre):
        # Llama al nuevo procedimiento almacenado con un solo parámetro
        return self.conexion.ejecutar("sp_buscar_escuela_por_nombre", [nombre])