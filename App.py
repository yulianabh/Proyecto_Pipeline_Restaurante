def crear_reserva(cliente, personas):
    if not cliente:
        return {"error": "El nombre del cliente es obligatorio"}

    if personas <= 0:
        return {"error": "La cantidad de personas debe ser mayor a cero"}

    return {
        "mensaje": "Reserva creada correctamente",
        "cliente": cliente,
        "personas": personas
    }


def crear_pedido(producto, cantidad):
    if not producto:
        return {"error": "El producto es obligatorio"}

    if cantidad <= 0:
        return {"error": "La cantidad debe ser mayor a cero"}

    return {
        "mensaje": "Pedido creado correctamente",
        "producto": producto,
        "cantidad": cantidad
    }
