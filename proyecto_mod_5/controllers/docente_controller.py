from config.database import Database
from models.docente import Docente

class DocenteController:
    def __init__(self, db):
        self.db = db
        
    def registrar_docente(self, nombre, apellido, correo_electronico, telefono, especialidad):
        sql = """ INSERT INTO docentes (nombre, apellido, correo_electronico, telefono, especialidad) VALUES (%s, %s, %s, %s, %s) """
        params = (nombre, apellido, correo_electronico, telefono, especialidad)
        self.db.execute_query(sql, params)
        
    def listar_docentes(self):
        sql = """ SELECT id_docente, nombre, apellido, correo_electronico, telefono, especialidad FROM docentes """
        resultados = self.db.execute_select(sql)
        return [Docente(*resultado) for resultado in resultado]
    
    def obtener_docente_por_id(self, id_docente):
        sql = """ SELECT id_docente, nombre, apellido, correo_electronico, telefono, especialidad FROM docentes WHERE id_docente = %s """
        params = (id_docente,)
        resultado = self.db.execute_select(sql, params)
        return Docente(*resultado[0]) if resultado else None
    
    def actualizar_docente(self, id_docente, nombre, apellido, correo_electronico, telefono, especialidad):
        sql = """ UPDATE docentes SET nombre = %s, apellido = %s, correo_electronico = %s, telefono = %s, especialidad = %s WHERE id_docente = %s """
        params = (nombre, apellido, correo_electronico, telefono, especialidad, id_docente)
        self.db.execute_query(sql, params)
        
    def eliminar_docente(self, id_docente):
        sql = """ DELETE FROM docentes WHERE id_docente = %s """
        params = (id_docente,)
        self.db.execute_query(sql, params)
