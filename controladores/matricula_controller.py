# controladores/matricula_controller.py
from flask import render_template, request, redirect, url_for, flash
from servicios.matricula_service import MatriculaService
from dao.matricula_dao import MatriculaDAO
# Importamos los DAOs necesarios para obtener las listas
from dao.estudiante_dao import EstudianteDAO
from dao.curso_dao import CursoDAO
from conexion import Conexion

class MatriculaController:
    def __init__(self):
        self.conexion = Conexion()
        self.matricula_dao = MatriculaDAO(self.conexion)
        self.matricula_service = MatriculaService(self.matricula_dao)
        # Instanciamos los otros DAOs para usarlos
        self.estudiante_dao = EstudianteDAO(self.conexion)
        self.curso_dao = CursoDAO(self.conexion)

    def mostrar_matriculas(self):
        # Obtenemos las tres listas de datos
        matriculas = self.matricula_service.listar()
        estudiantes = self.estudiante_dao.listar()
        cursos = self.curso_dao.listar()
        # Pasamos las tres listas a la plantilla
        return render_template('matriculas.html', matriculas=matriculas, estudiantes=estudiantes, cursos=cursos)

    def agregar_matricula(self):
        if request.method == 'POST':
            id_estudiante = request.form['id_estudiante']
            id_curso = request.form['id_curso']
            ciclo = request.form['ciclo']
            
            resultado = self.matricula_service.crear(id_estudiante, id_curso, ciclo)
            mensaje_db = resultado[0]
            
            if mensaje_db['estado'] == 'CORRECTO':
                flash('Matrícula registrada exitosamente.', 'success')
            else:
                flash(mensaje_db['mensaje'], 'danger')
        
        return redirect(url_for('mostrar_matriculas'))

    def editar_matricula(self, id):
        if request.method == 'POST':
            id_estudiante = request.form['id_estudiante']
            id_curso = request.form['id_curso']
            ciclo = request.form['ciclo']

            resultado = self.matricula_service.actualizar(id, id_estudiante, id_curso, ciclo)
            mensaje_db = resultado[0]
            
            if mensaje_db['estado'] == 'CORRECTO':
                flash('Matrícula actualizada exitosamente.', 'success')
            else:
                flash(mensaje_db['mensaje'], 'danger')

        return redirect(url_for('mostrar_matriculas'))

    def eliminar_matricula(self, id):
        if request.method == 'POST':
            resultado = self.matricula_service.eliminar(id)
            mensaje_db = resultado[0]
            
            if mensaje_db['estado'] == 'CORRECTO':
                flash('Matrícula eliminada exitosamente.', 'success')
            else:
                flash(mensaje_db['mensaje'], 'danger')
        
        return redirect(url_for('mostrar_matriculas'))
    
    def cerrar(self):
        self.conexion.cerrar()