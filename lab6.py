# ==========================================================
# LAB 6 · "Base de datos de películas"
# ==========================================================

peliculas = [
    {"titulo": "Dune Parte 2", "director": "Denis Villeneuve",
     "anio": 2024, "generos": ["ciencia ficción", "aventura"]},
    {"titulo": "Coco", "director": "Lee Unkrich",
     "anio": 2017, "generos": ["animación", "fantasía"]},
    {"titulo": "Interstellar", "director": "Christopher Nolan",
     "anio": 2014, "generos": ["ciencia ficción", "drama"]},
    {"titulo": "Oppenheimer", "director": "Christopher Nolan",
     "anio": 2023, "generos": ["drama", "historia"]},
    {"titulo": "El Padrino", "director": "Francis Ford Coppola",
     "anio": 1972, "generos": ["drama", "crimen"]},
]

# 1 y 2. Catálogo completo, alineado y numerado
print(f"{'#':<3}{'TÍTULO':<18}{'DIRECTOR':<22}{'AÑO':<6}{'GÉNEROS'}")
print("-" * 65)
for i, peli in enumerate(peliculas, start=1):
    print(f"{i:<3}{peli['titulo']:<18}{peli['director']:<22}"
          f"{peli['anio']:<6}{', '.join(peli['generos'])}")

# 3. Pedir un año y mostrar solo las posteriores
anio_texto = input("\nMostrar películas posteriores a qué año: ").strip()
if anio_texto.isdigit():
    anio_limite = int(anio_texto)
    posteriores = [p for p in peliculas if p["anio"] > anio_limite]
    print(f"Películas después de {anio_limite}:")
    for p in posteriores:
        print(f"  · {p['titulo']} ({p['anio']})")
else:
    print("Eso no es un año válido.")

# 4. Año promedio y película más antigua
anio_promedio = sum(p["anio"] for p in peliculas) / len(peliculas)
mas_antigua = None
for p in peliculas:
    if mas_antigua is None or p["anio"] < mas_antigua["anio"]:
        mas_antigua = p
print(f"\nAño promedio del catálogo: {anio_promedio:.1f}")
print(f"Más antigua: {mas_antigua['titulo']} ({mas_antigua['anio']})")

# 5. Contar películas por género (bucle anidado + contador con diccionario)
conteo_generos = {}
for p in peliculas:
    for genero in p["generos"]:
        conteo_generos[genero] = conteo_generos.get(genero, 0) + 1

print("\nPelículas por género:")
for genero, cuantas in conteo_generos.items():
    print(f"  {genero:<16} {'#' * cuantas} ({cuantas})")

# 6. Catálogo ordenado por año descendente
por_anio = sorted(peliculas, key=lambda p: p["anio"], reverse=True)
print("\nOrdenado del más nuevo al más antiguo:")
for p in por_anio:
    print(f"  {p['anio']} — {p['titulo']}")

# Nota sobre el punto de entrega ("dibuja la estructura en papel"):
# peliculas es una LISTA de fichas; cada ficha es un DICCIONARIO con
# cuatro campos (titulo, director, anio, generos); el campo 'generos'
# es a su vez una LISTA de textos. Es exactamente el patrón "lista de
# diccionarios" del nivel 6, con una lista anidada dentro de cada ficha.
