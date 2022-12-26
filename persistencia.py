def guardar_pedido(nombre, apellidos):
  usuario = {"nom":nombre, "ape":apellidos}
  with open("pedidos.txt", "a", encoding="utf-8") as file:
    file.write (usuario["nom"] + " " + usuario["ape"] + "\n")
    file.close()
