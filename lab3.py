# ==========================================================
# LAB 3 · "Informe de notas 2.0"
# ==========================================================

# 1. Pedir cuántas notas y llenarlas
cantidad_texto = input("¿Cuántas notas vas a registrar? ").strip()
while not cantidad_texto.isdigit():
    print("Necesito solo dígitos, sin letras ni comas. Ejemplo: 5")
    cantidad_texto = input("¿Cuántas notas vas a registrar? ").strip()
cantidad = int(cantidad_texto)

notas = []
for i in range(cantidad):
    nota_texto = input(f"Nota {i + 1}: ").strip()
    notas.append(float(nota_texto))

# 2. Listado numerado
print("\nListado de notas:")
for numero, nota in enumerate(notas, start=1):
    print(f"{numero}. {nota}")

# 3. Promedio, mejor y peor, protegiendo el caso de cero notas
if len(notas) > 0:
    promedio = sum(notas) / len(notas)
    print(f"\nPromedio: {promedio:.2f}")
    print(f"Mejor nota: {max(notas)}")
    print(f"Peor nota: {min(notas)}")
else:
    print("\nNo hay notas registradas, no se puede calcular nada.")

# 4. aprobadas y perdidas, con bucle largo
MINIMA = 3.0
aprobadas = []
perdidas = []
for nota in notas:
    if nota >= MINIMA:
        aprobadas.append(nota)
    else:
        perdidas.append(nota)
print(f"\nAprobadas: {len(aprobadas)} · Perdidas: {len(perdidas)}")

# 5. Lo mismo con comprensiones (debe dar idéntico)
aprobadas_c = [n for n in notas if n >= MINIMA]
perdidas_c = [n for n in notas if n < MINIMA]
print("Coinciden con el bucle largo:",
      aprobadas == aprobadas_c and perdidas == perdidas_c)

# 6. Ranking de mayor a menor sin destruir el orden original
ranking = sorted(notas, reverse=True)
print("\nOrden de ingreso (intacto):", notas)
print("Ranking (mayor a menor):", ranking)

# Reflexión pedida por el laboratorio:
# La comprensión resultó más clara en el punto 5 (filtrar es una sola idea:
# "quédate con lo que cumple"). El bucle largo se sintió más cómodo en el
# punto 1, porque ahí no solo se acumula: también se valida y se convierte
# el texto a número, y eso son varias instrucciones por vuelta.
