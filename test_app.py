
from App import crear_reserva, crear_pedido


def test_crear_reserva_correctamente():
    resultado = crear_reserva("Carlos", 4)

    assert resultado["mensaje"] == "Reserva creada correctamente"
    assert resultado["cliente"] == "Carlos"
    assert resultado["personas"] == 4


def test_reserva_sin_cliente():
    resultado = crear_reserva("", 4)
    assert "error" in resultado


def test_reserva_con_personas_invalidas():
    resultado = crear_reserva("Carlos", 0)
    assert "error" in resultado


def test_crear_pedido_correctamente():
    resultado = crear_pedido("Hamburguesa", 2)

    assert resultado["mensaje"] == "Pedido creado correctamente"
    assert resultado["producto"] == "Hamburguesa"
    assert resultado["cantidad"] == 2


def test_pedido_con_cantidad_invalida():
    resultado = crear_pedido("Pizza", 0)
    assert "error" in resultado


def test_reserva_con_cliente_solo_espacios():
    resultado = crear_reserva("   ", 2)
    assert "error" in resultado


def test_reserva_con_personas_texto():
    resultado = crear_reserva("Ana", "dos")
    assert "error" in resultado


def test_pedido_con_producto_solo_espacios():
    resultado = crear_pedido("   ", 1)
    assert "error" in resultado


def test_pedido_con_cantidad_texto():
    resultado = crear_pedido("Pizza", "dos")
    assert "error" in resultado
