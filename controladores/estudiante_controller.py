# controladores/estudiante_controller.py
from flask import render_template, request, redirect, url_for, flash
from servicios.estudiante_service import EstudianteService
from dao.estudiante_dao import EstudianteDAO
from dao.escuela_dao import EscuelaDAO # <-- IMPORTANTE: para obtener las escuelas
from conexion import Conexion

class EstudianteController:
    def __init__(self):
        self.conexion = Conexion()
        self.estudiante_dao = EstudianteDAO(self.conexion)
        self.estudiante_service = EstudianteService(self.estudiante_dao)
        self.escuela_dao = EscuelaDAO(self.conexion) # <-- Necesitamos un DAO de escuela

    def mostrar_estudiantes(self):
        estudiantes = self.estudiante_service.listar()
        escuelas = self.escuela_dao.listar() # <-- Obtenemos la lista de escuelas
        return render_template('estudiantes.html', estudiantes=estudiantes, escuelas=escuelas)

    def agregar_estudiante(self):
        if request.method == 'POST':
            nombres = request.form['nombres']
            apellidos = request.form['apellidos']
            correo = request.form['correo']
            id_escuela = request.form['id_escuela']
            
            resultado = self.estudiante_service.crear(nombres, apellidos, correo, id_escuela)
            mensaje_db = resultado[0]
            
            if mensaje_db['estado'] == 'CORRECTO':
                flash(mensaje_db['mensaje'], 'success')
            else:
                flash(mensaje_db['mensaje'], 'danger')
        
        return redirect(url_for('mostrar_estudiantes'))

    def editar_estudiante(self, id):
        if request.method == 'POST':
            nombres = request.form['nombres']
            apellidos = request.form['apellidos']
            correo = request.form['correo']
            id_escuela = request.form['id_escuela']
            
            resultado = self.estudiante_service.actualizar(id, nombres, apellidos, correo, id_escuela)
            mensaje_db = resultado[0]
            
            if mensaje_db['estado'] == 'CORRECTO':
                flash(mensaje_db['mensaje'], 'success')
            else:
                flash(mensaje_db['mensaje'], 'danger')

        return redirect(url_for('mostrar_estudiantes'))

    def eliminar_estudiante(self, id):
        if request.method == 'POST':
            resultado = self.estudiante_service.eliminar(id)
            mensaje_db = resultado[0]
            
            if mensaje_db['estado'] == 'CORRECTO':
                flash(mensaje_db['mensaje'], 'success')
            else:
                flash(mensaje_db['mensaje'], 'danger')
        
        return redirect(url_for('mostrar_estudiantes'))
    
    def cerrar(self):
        self.conexion.cerrar()