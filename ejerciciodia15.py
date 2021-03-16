from flask import Flask, jsonify
from flask import request
from random import randint
app = Flask(__name__)


@app.route('/random')
def random_number():
    first_num = int(request.args.get('first_num'))
    second_num = int(request.args.get('second_num'))
    pupil_name = request.args.get('pupil_name')
    print(f'{pupil_name} HA HECHO LA REQUEST')
    return str(randint(first_num, second_num))


@app.route('/order', methods=['POST'])
def order():
    data = request.json
    numbers = data.get('numbers')
    numbers = list(set(numbers))
    #numbers.sort(reverse=True)
    print(numbers)

    return jsonify(data)


app.run(host='0.0.0.0', port=80, debug=True)

# EJERCICIO

# POST -> localhost/order
# json -> {"numbers": [23, 432, 88, 90, 90, 70]} Números positivos del 1 al 1000, se pueden repetir.
# SIEMPRE SE RECIBE LISTA NUMERICA (no pasan strings, ni números negativos, y no se presupone que
# el usuario la va a liar.

# se pide:
# eliminar elementos repetidos
# ordenar de menor a mayor los restantes
# devolver en formato json:
# {"ordered_numbers" : [23, 70, 88, 90, 432]}