
def crear_reserva(cliente, personas):
    if not isinstance(cliente, str) or not cliente.strip():
        return {"error": "El nombre del cliente es obligatorio"}

    if not isinstance(personas, int) or isinstance(personas, bool) or personas <= 0:
        return {"error": "La cantidad de personas debe ser un entero mayor a cero"}

    return {
        "mensaje": "Reserva creada correctamente",
        "cliente": cliente.strip(),
        "personas": personas
    }


def crear_pedido(producto, cantidad):
    if not isinstance(producto, str) or not producto.strip():
        return {"error": "El producto es obligatorio"}

    if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
        return {"error": "La cantidad debe ser un entero mayor a cero"}

    return {
        "mensaje": "Pedido creado correctamente",
        "producto": producto.strip(),
        "cantidad": cantidad
    }
