import mysql.connector

class Conexion:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="systemowner",
            database="sistema_academico"
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def ejecutar(self, procedimiento, parametros):
        self.cursor.callproc(procedimiento, parametros)
        resultados = []
        for result in self.cursor.stored_results():
            resultados.extend(result.fetchall())
        self.conn.commit()
        return resultados

    def cerrar(self):
        self.cursor.close()
        self.conn.close()

    def ejecutarsinparametros(self, procedimiento):
        self.cursor.callproc(procedimiento)
        resultados = []
        for result in self.cursor.stored_results():
            resultados.extend(result.fetchall())
        self.conn.commit()
        return resultados