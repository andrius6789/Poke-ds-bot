class Locacion:
    def __init__(self, nombre, nombres):
        self.nombre = nombre
        self.nombres = nombres
        self.lista_encuentros = []

# Lista para almacenar objetos Locacion
locaciones = []

# Variables para mantener el estado mientras leemos el archivo
nombre_locacion_actual = None
nombres_actuales = []

# Leer el archivo de texto
with open('spawns.txt', 'r') as spawns_file:
    for line in spawns_file:
        line = line.strip()
        if line:
            if nombre_locacion_actual is None:
                nombre_locacion_actual = line
            else:
                nombres_actuales.append(line)
        else:
            if nombre_locacion_actual is not None and nombres_actuales:
                locaciones.append(Locacion(nombre_locacion_actual, nombres_actuales))
                nombre_locacion_actual = None
                nombres_actuales = []

# Agregar la última locación
if nombre_locacion_actual is not None and nombres_actuales:
    locaciones.append(Locacion(nombre_locacion_actual, nombres_actuales))

# Imprimir la información de cada locación
for locacion in locaciones:
    """
    Para cada locacion en la lista de Locaciones
    """
    locacion.nombre = locacion.nombre.replace(":","").lower()
    
    for nombre in locacion.nombres:
        """
        Para cada tipo de encuentro en una locacion
        tipo siendo: common, uncommon, rare, very rare, extremely rare y sus pokemones
        """
        rareza, pokemones = nombre.split(':')
        rareza = rareza.lower()
        pokemones = pokemones.split(',')
        pokemones = [pokemon.replace(" ","").lower() for pokemon in pokemones] # Elimina los espacios en blanco de los pokemones
        pokemones_2 = []


        for pokemon in pokemones:
            """
            Recorre todos los pokemones dentro de la lista pokemones y los aisla,
            quitandole el espacio en blanco inicial
            """
            if str(pokemon)[0] == '':
                pokemon = pokemon[1:]
            else:
                pokemon = pokemon

            pokemones_2.append(pokemon)
        encuentros = (rareza, pokemones_2)
        locacion.lista_encuentros.append(encuentros)



