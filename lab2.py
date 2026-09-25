# ==========================================================
# LAB 2 · "Lista de compras que funciona"
# ==========================================================

# 1. Cuatro productos con append
compras = []
for producto in ["pan", "leche", "huevos", "arroz"]:
    compras.append(producto)

# 2. Insertar urgente al principio
compras.insert(0, "urgente: pilas")
print("Lista inicial:", compras)

# 3. Agregar un producto solo si no está
nuevo = input("\nProducto a agregar: ").strip().lower()
if nuevo in compras:
    print(f"Aviso: '{nuevo}' ya estaba en la lista. Se esperaba un producto "
          f"nuevo. Prueba con otro nombre o revisa la lista impresa arriba.")
else:
    compras.append(nuevo)
    print(f"'{nuevo}' agregado. Lista: {compras}")

# 4. Eliminar un producto protegido con in
quitar = input("\nProducto a eliminar: ").strip().lower()
if quitar in compras:
    compras.remove(quitar)
    print(f"'{quitar}' eliminado. Lista: {compras}")
else:
    print(f"'{quitar}' no está en la lista, no se elimina nada. "
          f"El programa sigue sin romperse.")

# 5. Mostrar ordenada sin modificar, y luego la original
print("\nOrdenada (sorted, no toca la original):", sorted(compras))
print("Original (sigue en su orden de siempre):", compras)

# 6. El desastre del alias
respaldo = compras          # <- esto NO copia, solo le pone otro nombre
compras.clear()
print("\nrespaldo tras vaciar 'compras':", respaldo)
# Explicación: 'respaldo' no es una copia independiente, es un segundo
# nombre para la MISMA lista. Al hacer compras.clear() se vació la única
# caja que existe, así que 'respaldo' también quedó vacío.
# El arreglo correcto es usar una copia real:
#     respaldo = compras.copy()
