from models.curso import Curso

class CursoController:
    def __init__(self, db):
        self.db = db

    def registrar_curso(self, nombre, descripcion, duracion_horas, docente_id):
        sql = """ INSERT INTO cursos (nombre, descripcion, duracion_horas, docente_id) VALUES (%s, %s, %s, %s) """
        params = (nombre, descripcion, duracion_horas, docente_id)
        self.db.execute_query(sql, params)
        
    def listar_cursos(self):
        sql = """ SELECT id_curso, nombre, descripcion, duracion_horas, docente_id FROM cursos """
        resultados = self.db.execute_select(sql)
        return [Curso(*resultado) for resultado in resultados]
    
    def actualizar_curso(self, id_curso, nombre, descripcion, duracion_horas, docente_id):
        sql = """ UPDATE cursos SET nombre = %s, descripcion = %s, duracion_horas = %s, docente_id = %s WHERE id_curso = %s """
        params = (nombre, descripcion, duracion_horas, docente_id, id_curso)
        self.db.execute_query(sql, params)
        
    def eliminar_curso(self, id_curso):
        sql = """ DELETE FROM cursos WHERE id_curso = %s """
        params = (id_curso,)
        self.db.execute_query(sql, params)