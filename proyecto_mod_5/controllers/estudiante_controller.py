#LLamamos la configuracion
from models.estudiante import Estudiante
# Clase EstudianteController
class EstudianteController:

    def __init__(self, db):
        self.db = db

    def registrar_estudiante(self, nombre, apellido, correo_electronico, telefono):
        sql = """
        INSERT INTO estudiantes (nombre, apellido, correo_electronico, telefono) VALUES (%s, %s, %s, %s)
        """
        params = (nombre, apellido, correo_electronico, telefono)
        self.db.execute_query(sql, params)
        
    def listar_estudiantes(self):
        sql = """ SELECT id_estudiante, nombre, apellido, correo_electronico, telefono FROM estudiantes """
        resultados = self.db.execute_select(sql)
        print(resultados)
        return [Estudiante(*resultado) for resultado in resultados]

    def actualizar_estudiante(self, id_estudiante, nombre, apellido, correo_electronico, telefono):
        sql = """ UPDATE estudiantes SET nombre = %s, apellido = %s, correo_electronico = %s, telefono = %s WHERE id_estudiante = %s """
        params = (nombre, apellido, correo_electronico, telefono, id_estudiante)
        self.db.execute_query(sql, params)

    def eliminar_estudiante(self, id_estudiante):
        sql = """ DELETE FROM estudiantes WHERE id_estudiante = %s """
        params = (id_estudiante,)
        self.db.execute_query(sql, params)
        
    def obtener_estudiante_por_id(self, id_estudiante):
        sql = """ SELECT id_estudiante, nombre, apellido, correo_electronico, telefono FROM estudiantes WHERE id_estudiante = %s """
        params = (id_estudiante,)
        resultado = self.db.execute_select(sql, params)
        return Estudiante(*resultado[0]) if resultado else None
    
    def actualizar_estudiante(self, id_estudiante, nombre, apellido, correo_electronico, telefono):
        sql = """ UPDATE estudiantes SET nombre = %s, apellido = %s, correo_electronico = %s, telefono = %s WHERE id_estudiante = %s """
        params = (nombre, apellido, correo_electronico, telefono, id_estudiante)
        self.db.execute_query(sql, params)
        
    def eliminar_estudiante(self, id_estudiante):
        sql = """ DELETE FROM estudiantes WHERE id_estudiante = %s """
        params = (id_estudiante,)
        self.db.execute_query(sql, params)
        
