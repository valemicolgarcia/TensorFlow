# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    #prev_play is a string describing the last move of the opponent (R,P,S)
    #opponent history last movements of the opponent --> i will use this to predict the next move and who is the opponent

    #the first time, prev_play is " " --> there is no previous play

    #MULTIPLE STRATEGIES depending on the oponent

    if prev_play != "":
        opponent_history.append(prev_play)

    guess = "R" 

    #QUINCY PATTERN --> solo detecta un caso
    #detecto el patron de quincy y en base a eso defino mi estrategia
    quincy_pattern = ['R','R','P','P','S'] #sigue siempre ese patron quincy
    if len(opponent_history) >= len(quincy_pattern):
        last_5 = opponent_history[-5:]
    
    if last_5 == quincy_pattern: 
        guess = 'P' #
    else:
        guess = 'R'

    
    #MRUGESH
    #guarda las ultimas 10 jugadas del oponente, busca la mas frecuente y en base a eso responde con la jugada que ganaria a esa opcion
    
    #estrategia: tirar piedra 10 veces, cuando llego a la 10 el oponente va a tirar P entonces yo tiro S
    #luego tiro S 10 veces , luego R 10 veces


    #KRIS
    #la primera vez saco R
    #KRIS devuelve lo que venceria a la ultima jugada del oponente
    # va a devolver P
    #entonces yo tengo que devolver S
    #va a devolver R
    #SIGUE ESTE PATRON -- P,R,S


    #ABBEY
    #SU ESTRATEGIA: detecta patrones de a dos, RS:1, RP: 2, RR: 3, como predice que voy a sacar R me devuelve P
    #yo deberia sacar S para vencerlo
    #detecta RS, 
    #en las frecuencias hay empate PR, PP, la funcion max toma el primero que aparece 
    #despues de la P estan todas en 0 entonces devuelve R (PRIMERA) yo devuelvo P

    




    if len(opponent_history) > 2:
        guess = opponent_history[-2]

    return guess
    #guess should return the next move for it to play
