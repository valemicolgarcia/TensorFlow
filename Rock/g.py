from typing import Literal
from random import choice

Hand = Literal["R", "P", "S", ""]

# Contadores de transiciones
transition_counts = {
    "R": {"R": 0, "P": 0, "S": 0},
    "P": {"R": 0, "P": 0, "S": 0},
    "S": {"R": 0, "P": 0, "S": 0}
}

def player(prev_play: Hand, opponent_history: list[Hand] = []) -> Hand:
    # Inicializar la elección aleatoria si es el primer movimiento
    if prev_play == "":
        return choice(["R", "P", "S"])
    
    # Agregar el movimiento previo a la historia del oponente
    opponent_history.append(prev_play)
    
    # Si hay menos de 2 movimientos, elegir aleatoriamente
    if len(opponent_history) < 3:
        return choice(["R", "P", "S"])
    
    # Contar el movimiento después del movimiento previo
    previous_move = opponent_history[-2]
    current_move = opponent_history[-1]
    
    # Verificar que los movimientos sean válidos antes de actualizar los contadores
    if previous_move in transition_counts and current_move in transition_counts[previous_move]:
        transition_counts[previous_move][current_move] += 1
    
    # Encontrar el movimiento más frecuente después del movimiento previo
    if previous_move in transition_counts:
        most_frequent_move = max(transition_counts[previous_move], key=transition_counts[previous_move].get)
    else:
        # En caso de que no se haya registrado ninguna transición, elegir aleatoriamente
        most_frequent_move = choice(["R", "P", "S"])
    
    # Elegir la respuesta que gana contra el movimiento más frecuente
    response = {
        "R": "P",
        "P": "S",
        "S": "R"
    }
    
    return response.get(most_frequent_move, choice(["R", "P", "S"]))


    #-----------------------------

    #guess = "R"
    #if len(opponent_history) > 2:
     #   guess = opponent_history[-2]

    #return guess
