# controladores/dashboard_controller.py
from flask import render_template
from servicios.dashboard_service import DashboardService
from dao.dashboard_dao import DashboardDAO
from conexion import Conexion

class DashboardController:
    def __init__(self):
        self.conexion = Conexion()
        self.dashboard_dao = DashboardDAO(self.conexion)
        self.dashboard_service = DashboardService(self.dashboard_dao)

    def mostrar_dashboard(self):
        dashboard_data = self.dashboard_service.get_all_data()
        return render_template('dashboard.html', data=dashboard_data)
    
    def cerrar(self):
        self.conexion.cerrar()