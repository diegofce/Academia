from controllers.estudiante_controller import EstudianteController 
from mysql.connector import IntegrityError

def menu_principal(db):
    estudiante_controller = EstudianteController(db)

    while True:    
        # Mostrar el menú de opciones
        print("\n=== *********** ===")
        print("Bienvenido al sistema de gestión de estudiantes")
        print("1. Registrar estudiante")
        print("2. Listar estudiantes")
        print("3. Obtener estudiante por ID")
        print("4. Actualizar estudiante")
        print("5. Eliminar estudiante")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_estudiante(estudiante_controller)
        elif opcion == '2':
            listar_estudiantes(estudiante_controller)
        elif opcion == '3':
            obtener_estudiante_por_id(estudiante_controller)
        elif opcion == '4':
            actualizar_estudiante(estudiante_controller)
        elif opcion == '5':
            eliminar_estudiante(estudiante_controller)
        elif opcion == '6':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def registrar_estudiante(estudiante_controller):
    print("=== ** Registro de estudiante ** ===")
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    correo_electronico = input("Ingrese el correo del estudiante: ")
    telefono = input("Ingrese el teléfono del estudiante: ")
    
    try:
        estudiante_controller.registrar_estudiante(nombre, apellido, correo_electronico, telefono)
        print("Estudiante registrado exitosamente.")
    except IntegrityError as e:
        print(f"Alerta ! Error de integridad: {e.msg}")
    except Exception as e:
        print(f"Error al registrar el estudiante: {str(e)}")

def listar_estudiantes(estudiante_controller):
    print("=== ** Listado de estudiantes ** ===")
    try:
        estudiantes = estudiante_controller.listar_estudiantes()
        if estudiantes:
            print("ID\tNombre\tApellido\tCorreo\tTeléfono")
            for e in estudiantes:
                print(f"{e.id_estudiante} | {e.nombre} | {e.apellido} | {e.correo_electronico} | {e.telefono}")
        else:
            print("No hay estudiantes registrados.")
    except Exception as e:
        print(f"Error al listar los estudiantes: {str(e)}")
        
    
def obtener_estudiante_por_id(estudiante_controller):
    print("=== ** Obtener estudiante por ID ** ===")
    id_estudiante = int(input("Ingrese el ID del estudiante: "))
    try:
        estudiante = estudiante_controller.obtener_estudiante_por_id(id_estudiante)
        if estudiante:
            print(f"ID: {estudiante.id_estudiante}")
            print(f"Nombre: {estudiante.nombre}")
            print(f"Apellido: {estudiante.apellido}")
            print(f"Correo: {estudiante.correo_electronico}")
            print(f"Teléfono: {estudiante.telefono}")
    except Exception as e:
        print(f"Error al obtener el estudiante: {str(e)}")
            
def actualizar_estudiante(estudiante_controller):
    print("=== ** Actualizar estudiante ** ===")
    id_estudiante = int(input("Ingrese el ID del estudiante: "))
    nombre = input("Ingrese el nuevo nombre del estudiante: ")
    apellido = input("Ingrese el nuevo apellido del estudiante: ")
    correo_electronico = input("Ingrese el nuevo correo del estudiante: ")
    telefono = input("Ingrese el nuevo teléfono del estudiante: ")
    
    try:
        estudiante_controller.actualizar_estudiante(id_estudiante, nombre, apellido, correo_electronico, telefono)
        print("Estudiante actualizado exitosamente.")
    except Exception as e:
        print(f"Error al actualizar el estudiante: {str(e)}")
        
def eliminar_estudiante(estudiante_controller):
    print("=== ** Eliminar estudiante ** ===")
    id_estudiante = int(input("Ingrese el ID del estudiante: "))
    try:
        estudiante_controller.eliminar_estudiante(id_estudiante)
        print("Estudiante eliminado exitosamente.")
    except Exception as e:
        print(f"Error al eliminar el estudiante: {str(e)}")
