from views.menu import menu_principal
from views.menu_docente import menu_principal_docente
from views.menu_curso import menu_principal_curso
from config.database import Database


if __name__ == "__main__":
    db = Database()
    try:
        # Iniciar el menú principal
        # menu_principal(db) #Menu de estudiantes
        # menu_principal_docente(db) #Menu de docentes
        menu_principal_curso(db) #Menu de cursos
    finally:
        # Asegurarse de cerrar la conexión a la base de datos al finalizar
        db.close()