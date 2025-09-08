# controladores/curso_controller.py
from flask import render_template, request, redirect, url_for, flash
from servicios.curso_service import CursoService
from dao.curso_dao import CursoDAO
from conexion import Conexion

class CursoController:
    def __init__(self):
        self.conexion = Conexion()
        self.curso_dao = CursoDAO(self.conexion)
        self.curso_service = CursoService(self.curso_dao)

    def mostrar_cursos(self):
        cursos = self.curso_service.listar()
        return render_template('cursos.html', cursos=cursos)

    def agregar_curso(self):
        if request.method == 'POST':
            nombre = request.form['nombre']
            creditos = request.form['creditos']
            
            resultado = self.curso_service.crear(nombre, creditos)
            mensaje_db = resultado[0]
            
            if mensaje_db['estado'] == 'CORRECTO':
                flash(mensaje_db['mensaje'], 'success')
            else:
                flash(mensaje_db['mensaje'], 'danger')
        
        return redirect(url_for('mostrar_cursos'))

    def editar_curso(self, id):
        if request.method == 'POST':
            nombre = request.form['nombre']
            creditos = request.form['creditos']
            
            resultado = self.curso_service.actualizar(id, nombre, creditos)
            mensaje_db = resultado[0]
            
            if mensaje_db['estado'] == 'CORRECTO':
                flash(mensaje_db['mensaje'], 'success')
            else:
                flash(mensaje_db['mensaje'], 'danger')

        return redirect(url_for('mostrar_cursos'))

    def eliminar_curso(self, id):
        if request.method == 'POST':
            resultado = self.curso_service.eliminar(id)
            mensaje_db = resultado[0]
            
            if mensaje_db['estado'] == 'CORRECTO':
                flash(mensaje_db['mensaje'], 'success')
            else:
                flash(mensaje_db['mensaje'], 'danger')
        
        return redirect(url_for('mostrar_cursos'))
    
    def cerrar(self):
        self.conexion.cerrar()