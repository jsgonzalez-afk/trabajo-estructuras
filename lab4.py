# ==========================================================
# LAB 4 · "Datos que no se tocan"
# ==========================================================

# 1. MESES como tupla; mes número 7 (índice 6)
MESES = ("enero", "febrero", "marzo", "abril", "mayo", "junio",
          "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
print("Mes número 7:", MESES[6])

# 2. Intentar modificarla
# MESES[0] = "Enero!"
# Traceback (most recent call last):
# TypeError: 'tuple' object does not support item assignment
# Explicación: las tuplas son inmutables, así que Python se niega a
# reasignar una casilla existente, aunque sí puede leerla sin problema.

# 3. Lista de tuplas (nombre, (r, g, b))
colores = [("rojo", (255, 0, 0)), ("verde", (0, 128, 0)), ("azul", (0, 0, 255))]
print()
for nombre, (r, g, b) in colores:
    print(f"{nombre} → R:{r} G:{g} B:{b}")

# 4. (5) frente a (5,)
t = (5)
t2 = (5,)
print("\ntype(t):", type(t))    # <class 'int'>  -> (5) es solo un número
print("type(t2):", type(t2))    # <class 'tuple'> -> la coma es la que crea la tupla
# Diferencia: lo que hace que algo sea una tupla es la COMA, no los
# paréntesis. (5) es un entero entre paréntesis; (5,) es una tupla de uno.

# 5. Tres datos propios, empaquetados y desempaquetados
mis_datos = ("jsg", "Colombia", "ingeniería de software")
nombre, pais, carrera = mis_datos
print(f"\n{nombre} está en {pais}, estudiando {carrera}.")

# 6. Convertir tupla a lista, modificar, volver a tupla
mi_tupla = (1, 2, 3)
como_lista = list(mi_tupla)
como_lista.append(4)
mi_tupla = tuple(como_lista)
print("\nTupla 'modificada' (en realidad, una nueva):", mi_tupla)
# No se cambió la tupla original: se construyó una lista aparte, se
# modificó esa lista (que sí es mutable) y se volvió a convertir en tupla.
# Así es como se "edita" algo inmutable: fabricando un reemplazo completo.
