# Importa render_template, request, redirect y url_for de Flask
from flask import render_template, request, redirect, url_for
from servicios.escuela_service import EscuelaService
from dao.escuela_dao import EscuelaDAO
from conexion import Conexion

class EscuelaController:
    def __init__(self):
        self.conexion = Conexion()
        self.dao = EscuelaDAO(self.conexion)
        self.servicio = EscuelaService(self.dao)
        # El generador de HTML ya no es necesario aquí
        # self.vista = GeneradorHTML() 

    # RUTA PRINCIPAL: Muestra la lista y el formulario
    def mostrar_escuelas(self):
        # Revisa si hay un parámetro 'q' en la URL (ej: /?q=sistemas)
        query = request.args.get('q')
        
        if query:
            # Si hay una búsqueda, llama al servicio de búsqueda
            datos = self.servicio.buscar_por_nombre(query)
        else:
            # Si no, lista todas las escuelas
            datos = self.servicio.listar()
            
        # Pasamos tanto los datos como el término de búsqueda a la plantilla
        return render_template('escuelas.html', escuelas=datos, search_query=query)

    # RUTA PARA AGREGAR
    def agregar_escuela(self):
        if request.method == 'POST':
            nombre = request.form['nombre']
            self.servicio.crear(nombre)
        # Redirigimos al usuario a la página principal
        return redirect(url_for('mostrar_escuelas'))

    # RUTA PARA EDITAR
    def editar_escuela(self, id):
        if request.method == 'POST':
            nombre = request.form['nombre']
            self.servicio.actualizar(id, nombre)
        return redirect(url_for('mostrar_escuelas'))

    # RUTA PARA ELIMINAR
    def eliminar_escuela(self, id):
        if request.method == 'POST':
            self.servicio.eliminar(id)
        return redirect(url_for('mostrar_escuelas'))

    def cerrar(self):
        self.conexion.cerrar()