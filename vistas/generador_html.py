class GeneradorHTML:
    def generar_escuela_html(self, datos):
        if not datos:
            return "<h2>Escuela no encontrada</h2>"

        escuela = datos[0]  # Asumiendo que el procedimiento devuelve una lista de dicts
        html = f"""
        <html>
        <head><title>Detalle de Escuela</title></head>
        <body>
            <h1>Escuela Profesional</h1>
            <p><strong>ID:</strong> {escuela['id_escuela']}</p>
            <p><strong>Nombre:</strong> {escuela['nombre']}</p>
        </body>
        </html>
        """
        return html