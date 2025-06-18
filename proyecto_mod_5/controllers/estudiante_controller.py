#LLamamos la configuracion
from config.database import Database
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
        return [Estudiante(*resultado) for resultado in resultados]  