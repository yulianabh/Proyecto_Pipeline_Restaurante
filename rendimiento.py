
import timeit
from App import crear_reserva, crear_pedido

tiempo_reservas = timeit.timeit(
    lambda: crear_reserva("Carlos", 4),
    number=100000
)

tiempo_pedidos = timeit.timeit(
    lambda: crear_pedido("Hamburguesa", 2),
    number=100000
)

print("RESULTADOS DE RENDIMIENTO")
print(f"Reservas (100.000 ejecuciones): {tiempo_reservas:.4f} segundos")
print(f"Pedidos (100.000 ejecuciones): {tiempo_pedidos:.4f} segundos")
