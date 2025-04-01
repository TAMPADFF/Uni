# Inicializamos la agenda como un diccionario vacío
agenda = {}

while True:
    dia = input("\nDime el día de la semana (o escribe 'salir' para terminar): ").strip().lower()

    if dia == "salir":
        break

    # Verificamos si el día ya está en la agenda
    if dia not in agenda:
        agenda[dia] = []  # Creamos una lista vacía si el día no tiene tareas

    # Mostramos la cantidad de tareas pendientes
    num_tareas = len(agenda[dia])
    print(f"\nTienes {num_tareas} tareas pendientes.\n")

    # Mostramos las tareas si existen
    if num_tareas > 0:
        for i, tarea in enumerate(agenda[dia], start=1):
            print(f"{i}. {tarea}\n")

    # Preguntamos por una nueva tarea
    nueva_tarea = input("¿Qué anotamos? (Enter para no añadir nada): ").strip()
    if nueva_tarea:
        agenda[dia].append(nueva_tarea)
        print("Tarea añadida con éxito.")
