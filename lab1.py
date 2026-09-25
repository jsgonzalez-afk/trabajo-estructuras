# ==========================================================
# LAB 1 · "Tu primera caja"
# ==========================================================

# 1. Cinco títulos vistos este año
peliculas = ["Dune 2", "Coco", "Interstellar", "Oppenheimer", "Wall-E"]

# 2. Primera y última, sin contar cuántas hay (índice negativo)
print("Primera:", peliculas[0])
print("Última:", peliculas[-1])

# 3. len() y el error a propósito
print("Cantidad de películas:", len(peliculas))
# peliculas[len(peliculas)]  # <- IndexError: list index out of range
# Explicación: len(peliculas) vale 5, pero los índices válidos van de 0 a 4.
# La casilla número 5 no existe: pedirla revienta el programa con IndexError.

# 4. Rebanada con las tres del medio
medio = peliculas[1:4]
print("Las tres del medio:", medio)

# 5. favoritas = las dos primeras + una nueva
favoritas = peliculas[:2] + ["Otra más"]
print("Favoritas:", favoritas)

# 6. Comprobar que peliculas no cambió (unir crea una lista nueva)
print("Original intacta:", peliculas)

# 7. ¿"Otra más" in peliculas?
resultado = "Otra más" in peliculas
print('"Otra más" in peliculas ->', resultado)
# Es False: "Otra más" solo existe dentro de 'favoritas', una lista NUEVA
# creada con el operador +. El operador + nunca modifica las listas
# originales, así que 'peliculas' nunca se enteró de ese elemento.
