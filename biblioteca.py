# ==========================================================
# BIBLIOTECA PERSONAL · Proyecto del tomo 3 + Reto final
# ==========================================================
# Incluye las mejoras del reto final:
#   - No permite títulos duplicados (opción 2)
#   - Opción 7: Pendientes, ordenados por páginas
#   - Opción 8: Eliminar, por número visto en el catálogo
# ==========================================================

GENEROS = ("novela", "ciencia", "historia", "comic")  # tupla: no cambia

libros = [
    {"titulo": "Rayuela", "autor": "Cortázar",
     "genero": "novela", "paginas": 600, "leido": True},
    {"titulo": "Cosmos", "autor": "Sagan",
     "genero": "ciencia", "paginas": 380, "leido": False},
]

print("=" * 46)
print(" BIBLIOTECA PERSONAL")
print("=" * 46)

while True:
    print("\n1. Ver catálogo      2. Agregar libro")
    print("3. Buscar            4. Marcar como leído")
    print("5. Estadísticas      6. Salir")
    print("7. Pendientes        8. Eliminar")
    opcion = input("> ").strip()

    match opcion:
        case "1":  # Ver catálogo
            if len(libros) == 0:
                print("Todavía no hay libros. Usa la opción 2 para agregar.")
                continue

            print(f"\n{'#':<3}{'TÍTULO':<22}{'AUTOR':<14}{'GÉNERO':<11}{'EST.'}")
            print("-" * 56)
            for i, libro in enumerate(libros, start=1):
                estado = "leído" if libro["leido"] else "pendiente"
                print(f"{i:<3}{libro['titulo']:<22}{libro['autor']:<14}"
                      f"{libro['genero']:<11}{estado}")

        case "2":  # Agregar libro (con protección contra duplicados)
            titulo = input("Título: ").strip()
            while titulo == "":
                print("El título no puede quedar vacío. Ejemplo: Cosmos")
                titulo = input("Título: ").strip()

            # Reto final: no permitir títulos duplicados
            ya_existe = any(l["titulo"].lower() == titulo.lower() for l in libros)
            if ya_existe:
                print(f"'{titulo}' ya está en la biblioteca. No se agregó de nuevo.")
                continue

            autor = input("Autor: ").strip()

            print(f"Géneros válidos: {', '.join(GENEROS)}")
            genero = input("Género: ").strip().lower()
            while genero not in GENEROS:
                print(f"Ese género no está en la lista. Escribe uno de: {', '.join(GENEROS)}")
                genero = input("Género: ").strip().lower()

            paginas_texto = input("Páginas: ").strip()
            while not paginas_texto.isdigit():
                print("Necesito solo dígitos, sin letras ni comas. Ejemplo: 380")
                paginas_texto = input("Páginas: ").strip()

            libros.append({"titulo": titulo, "autor": autor,
                            "genero": genero, "paginas": int(paginas_texto),
                            "leido": False})
            print(f"Listo: «{titulo}» agregado. Ahora tienes {len(libros)} libros.")

        case "3":  # Buscar
            texto = input("Buscar por título o autor: ").strip().lower()
            encontrados = []
            for libro in libros:
                if texto in libro["titulo"].lower() or texto in libro["autor"].lower():
                    encontrados.append(libro)

            if len(encontrados) == 0:
                print(f"No hay libros que contengan «{texto}». Prueba con menos letras.")
            else:
                for libro in encontrados:
                    print(f"· {libro['titulo']} — {libro['autor']} ({libro['paginas']} pág.)")

        case "4":  # Marcar como leído
            buscado = input("Título exacto del libro leído: ").strip().lower()
            for libro in libros:
                if libro["titulo"].lower() == buscado:
                    libro["leido"] = True
                    print(f"«{libro['titulo']}» marcado como leído.")
                    break
            else:
                print("No encontré ese título. Revisa el catálogo con la opción 1.")

        case "5":  # Estadísticas
            if len(libros) == 0:
                print("No hay datos para analizar todavía.")
                continue

            total_paginas = 0
            leidos = 0
            mas_largo = None
            por_genero = {}

            for libro in libros:
                total_paginas += libro["paginas"]
                if libro["leido"]:
                    leidos += 1
                if mas_largo is None or libro["paginas"] > mas_largo["paginas"]:
                    mas_largo = libro
                g = libro["genero"]
                por_genero[g] = por_genero.get(g, 0) + 1

            print(f"\nLibros registrados : {len(libros)}")
            print(f"Leídos              : {leidos} ({leidos / len(libros) * 100:.0f} %)")
            print(f"Páginas totales     : {total_paginas:,}")
            print(f"Promedio de páginas : {total_paginas / len(libros):.0f}")
            print(f"El más largo        : {mas_largo['titulo']} ({mas_largo['paginas']} pág.)")

            print("\nPor género:")
            for genero, cuantos in sorted(por_genero.items()):
                print(f"  {genero:<10} {'█' * cuantos} {cuantos}")

        case "6":  # Salir
            print("Cerrando la biblioteca. ¡Hasta la próxima!")
            break

        case "7":  # Reto final: Pendientes ordenados por páginas
            pendientes = [l for l in libros if not l["leido"]]
            if len(pendientes) == 0:
                print("No hay pendientes: ya leíste todo el catálogo.")
            else:
                pendientes_ordenados = sorted(pendientes, key=lambda l: l["paginas"])
                print("\nPendientes (del más corto al más largo):")
                for libro in pendientes_ordenados:
                    print(f"  {libro['titulo']:<22} {libro['paginas']} pág.")

        case "8":  # Reto final: Eliminar por número del catálogo
            if len(libros) == 0:
                print("No hay libros para eliminar.")
                continue
            numero_texto = input("Número del libro a eliminar (ver opción 1): ").strip()
            if not numero_texto.isdigit():
                print("Necesito un número, como el que aparece en el catálogo.")
                continue
            numero = int(numero_texto)
            if 1 <= numero <= len(libros):
                eliminado = libros.pop(numero - 1)  # el usuario ve desde 1
                print(f"Eliminado: «{eliminado['titulo']}»")
            else:
                print(f"No existe el libro número {numero}. Usa la opción 1 para ver el rango válido.")

        case _:
            print("Esa opción no existe. Escribe un número del 1 al 8.")
