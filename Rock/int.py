def player(prev_play, opponent_history=[]):
    #prev_play is a string describing the last move of the opponent (R,P,S)
    #opponent history last movements of the opponent --> i will use this to predict the next move and who is the opponent
    #the first time, prev_play is " " --> there is no previous play

    if prev_play != "":
        opponent_history.append(prev_play)

    #MULTIPLE STRATEGIES depending on the oponent

    OPONENT = 'nan' #no lo sabemos todavia

    #kris
    if(len(opponent_history) >= 4):
        last_3 = opponent_history[-3:] #dejo pasar el primero que es aletorio
        kris_pattern = ['P','R','S']
        if last_3 == kris_pattern:
            choices = ['S','P','R']
    
    #QUINCY
    if (len(opponent_history) >= 5):
        counter=[0]
        quincy_pattern = ['R','R','P','P','S']
        last_5 = opponent_history[-5:]
        if (last_5 == quincy_pattern): 
            choices = ['P','P','S','S','R']
            return choices [counter[0]%len(choices)]

    #MRUGESH
    if (len(opponent_history)>10):
        mrugesh_pattern = ['R','S','S','P','P','P','R','R','R','R']
        letters = ['P','R','S']
        if opponent_history[-10:] == mrugesh_pattern:
            for i in letters:
                #INCREMENTAR UN CONTADOR E IR DEVOLVIENDOOOOOOOOOO
    
    #ABBEY
    

            #no encuentro el patron todavia


    #guess = "R" 

    
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
