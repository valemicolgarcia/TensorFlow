# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play) #si prev_play no es una cadena vacia se agrega al historial
    else:
        opponent_history.clear()

    counter = { 'R': 'P', 'P': 'S', 'S': 'R' } #diccionario con las jugadas ganadoras
    guess = "S" #se inicializa la salida 

    if len(opponent_history) >= 4: #si el historial es mayor a 4

        #se crea una lista que tiene secuencias de 4 jugadas consecutivas del oponente y las pasa a texto
        play_order = [ ''.join(opponent_history[k:k+4]) for k, v in enumerate(opponent_history[:-3]) ]

        #se crea una lista en donde se guardan las ultimas 3 jugadas del oponente
        #cada secuencia agrega una jugada posible para predecir que podria jugar el oponente
        potential_play = [ ''.join([ *opponent_history[-3:], v ]) for v in ['S', 'R', 'P'] ]

        #se crea un diccionario para contar cuantas veces aparecen las secuencias posibles en play order
        sub_order = { k: play_order.count(k) for k in potential_play }

        #elige la secuencia que tiene mayor frecuencia (la sec mas comun) y se toma el ultimo caracter (prox jugda del oponente)
        prediction = max(sub_order, key=sub_order.get)[-1]

        #selecciona la jugada que vence al proximo
        guess = counter[prediction]

    return guess
