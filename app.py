"""
Flask app
"""

from flask import Flask, request, redirect, Response

from persistencia import guardar_pedido

app = Flask(__name__)

@app.route("/pizza", methods=["POST"])
def pizza():
    """
    Function to save requests
    """
    v_nombre = request.form.get("p_nombre")
    v_apellidos = request.form.get("p_apellidos")
    print(v_nombre)
    print(v_apellidos)
    print("Nombre Completo: " + v_nombre + " " + v_apellidos)
    guardar_pedido(v_nombre, v_apellidos)
    return redirect("http://localhost/solicita_pedido.html", code=302)


@app.route("/checksize",methods=['POST'])
def checksize():
    """
    Comprueba disponibilidad de un tamaño de pizza.
    """
    # Aquí va el código Python. Debe capturar el parámetro "size" de la request. Debe
    # retornar siempre "Disponible", excepto para el tamaño "S" que debe retornar "No
    # disponible" y se debe asignar en mensaje, así mensaje = "Lo que corresponda"

    v_size = request.form.get("size")
    if v_size == "S":
        mensaje = "No Disponible"
    else:
        mensaje = "Disponible"

    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
