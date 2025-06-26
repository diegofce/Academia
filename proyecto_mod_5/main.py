from views.menu import menu_principal
from views.menu_docente import menu_principal_docente
from config.database import Database

if __name__ == "__main__":
    db = Database()
    try:
        # Iniciar el menú principal
        # menu_principal(db)
        menu_principal_docente(db)
    finally:
        # Asegurarse de cerrar la conexión a la base de datos al finalizar
        db.close()