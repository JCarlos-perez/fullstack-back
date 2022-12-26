from flask import Flask, request, redirect
from persistencia import guardar_pedido

app = Flask(__name__)

@app.route("/pizza", methods=["POST"])
def pizza():
  v_nombre = request.form.get("p_nombre")
  v_apellidos = request.form.get("p_apellidos")
  print(v_nombre)
  print(v_apellidos)
  print("Nombre Completo: " + v_nombre + " " + v_apellidos)
  guardar_pedido(v_nombre, v_apellidos)
  return redirect("http://localhost/solicita_pedido.html", code=302)