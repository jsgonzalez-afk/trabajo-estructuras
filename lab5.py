# ==========================================================
# LAB 5 · "Agenda de contactos"
# ==========================================================

agenda = {}

print("=" * 40)
print(" AGENDA DE CONTACTOS")
print("=" * 40)

while True:
    print("\n1. Agregar  2. Consultar  3. Borrar  4. Listar  5. Salir")
    opcion = input("> ").strip()

    match opcion:
        case "1":  # Agregar
            nombre = input("Nombre: ").strip().lower()
            telefono = input("Teléfono: ").strip()
            if nombre in agenda:
                print(f"'{nombre}' ya existe con el número {agenda[nombre]}.")
                reemplazar = input("¿Reemplazarlo? (s/n): ").strip().lower()
                if reemplazar == "s":
                    agenda[nombre] = telefono
                    print("Contacto actualizado.")
                else:
                    print("No se hizo ningún cambio.")
            else:
                agenda[nombre] = telefono
                print(f"'{nombre}' agregado a la agenda.")

        case "2":  # Consultar
            nombre = input("¿A quién buscas?: ").strip().lower()
            telefono = agenda.get(
                nombre,
                f"No encontré a '{nombre}'. Se esperaba un nombre ya "
                f"registrado; usa la opción 1 para agregarlo."
            )
            print(telefono)

        case "3":  # Borrar
            nombre = input("¿A quién eliminas?: ").strip().lower()
            if nombre in agenda:
                numero = agenda.pop(nombre)
                print(f"Eliminado: {nombre} ({numero})")
            else:
                print(f"'{nombre}' no está en la agenda.")

        case "4":  # Listar
            if len(agenda) == 0:
                print("La agenda está vacía todavía.")
            else:
                for numero, (nombre, telefono) in enumerate(agenda.items(), start=1):
                    print(f"{numero}. {nombre:<15} {telefono}")
                print(f"\n{len(agenda)} contactos registrados.")

        case "5":
            print("Cerrando la agenda. ¡Hasta luego!")
            break

        case _:
            print("Esa opción no existe. Escribe un número del 1 al 5.")

# Respuesta escrita: si no normalizáramos los nombres, "Ana" y "ana" (o
# "Ana " con espacio) contarían como contactos distintos. Podrías terminar
# con el mismo contacto duplicado bajo variantes de mayúsculas/espacios,
# y buscarlo o borrarlo fallaría en silencio si escribes la variante
# "equivocada" — el programa diría que no existe aunque sí esté guardado.
