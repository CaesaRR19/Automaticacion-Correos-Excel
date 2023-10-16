def quitar_tildes(texto):
    # Definir un diccionario de reemplazo para las vocales con tildes
    reemplazo = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'Á': 'A',
        'É': 'E',
        'Í': 'I',
        'Ó': 'O',
        'Ú': 'U'
    }
    
    # Utilizar la función translate para reemplazar las vocales con tildes
    texto_sin_tildes = texto.translate(str.maketrans(reemplazo))
    
    return texto_sin_tildes