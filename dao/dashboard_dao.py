# dao/dashboard_dao.py
class DashboardDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def get_counts(self):
        return self.conexion.ejecutarsinparametros("sp_dashboard_counts")

    def get_estudiantes_por_escuela(self):
        return self.conexion.ejecutarsinparametros("sp_dashboard_estudiantes_por_escuela")

    def get_ultimas_matriculas(self):
        return self.conexion.ejecutarsinparametros("sp_dashboard_ultimas_matriculas")