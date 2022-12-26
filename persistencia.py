""" Module persistencia"""

def guardar_pedido(nombre, apellidos):
    """Procedure guardar_pedido to save data in a file"""
    usuario = {"nom":nombre, "ape":apellidos}
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write (usuario["nom"] + " " + usuario["ape"] + "\n")
        file.close()
