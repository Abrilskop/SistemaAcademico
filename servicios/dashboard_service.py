# servicios/dashboard_service.py
class DashboardService:
    def __init__(self, dao):
        self.dao = dao

    def get_all_data(self):
        counts = self.dao.get_counts()[0]  # Es una sola fila, la tomamos
        estudiantes_escuela = self.dao.get_estudiantes_por_escuela()
        ultimas_matriculas = self.dao.get_ultimas_matriculas()

        # Preparamos los datos para el gráfico
        chart_data = {
            'labels': [item['escuela_nombre'] for item in estudiantes_escuela],
            'data': [item['numero_estudiantes'] for item in estudiantes_escuela]
        }

        return {
            'counts': counts,
            'chart_data': chart_data,
            'ultimas_matriculas': ultimas_matriculas
        }