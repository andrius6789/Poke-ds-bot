from spawns import locaciones


def handle_response(message):
    
    primeros = message[:6]
    print(primeros)
    if message.startswith('!solo'):
        message = message[6:]
        print(message)
        lugares_solos = []    

        for locacion in locaciones:
            #search for every location in the list of locations and search inside the locacion.lista_encuentros[2] for the pokemon

            for rareza_encuentro in locacion.lista_encuentros:
                # print(rareza_encuentro)
                if len(rareza_encuentro[1]) != 1:
                    continue
                else:
                    if message == rareza_encuentro[1][0]:
                        print(f"Se encuentra aqui en {locacion.nombre}")
                        lugares_solos.append(locacion.nombre)
                    else:
                        print(f"No esta")
                        continue
    
        if len(lugares_solos) == 0:
            return (f"Error: {message} no se encuentra solo en ninguna locación")

        else:
            return (f"{message} se encuentra solo en las siguientes locaciones: {lugares_solos}")
    
    else:
        return (f"Error: {message} not valid")
