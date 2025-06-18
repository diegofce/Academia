from views.menu import menu_principal
from config.database import Database

if __name__ == "__main__":
    db = Database()
    try:
        # Iniciar el menú principal
        menu_principal(db)
    finally:
        # Asegurarse de cerrar la conexión a la base de datos al finalizar
        db.close()