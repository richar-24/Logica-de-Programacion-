import random

def elegir_palabra():
    palabras = ['psicologia', 'neurona', 'percepcion', 'neurociencia', 'comportamiento', 'comportamiento', 'sensacion', 'conciencia', 'memoria' , 'aprendizaje']
    return random.choice(palabras)

def mostrar_ahorcado(intentos):
    estados = [
        '''
           -----
           |   |
               |
               |
               |
               |
        =========''', '''
           -----
           |   |
           O   |
               |
               |
               |
        =========''', '''
           -----
           |   |
           O   |
           |   |
               |
               |
        =========''', '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========''', '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========''', '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========''', '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ========='''
    ]
    print(estados[intentos])

def jugar():
    print("¡Bienvenido al juego del ahorcado!")

    palabra_secreta = elegir_palabra()
    letras_adivinadas = []
    intentos = 0
    max_intentos = 6

    while intentos < max_intentos:
        # Mostrar el estado del ahorcado
        mostrar_ahorcado(intentos)

        # Mostrar la palabra con guiones para las letras no adivinadas
        palabra_mostrada = ''
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_mostrada += letra
            else:
                palabra_mostrada += '_'
        
        print(f"Palabra: {palabra_mostrada}")

        # Pedir al usuario que adivine una letra
        letra = input("Adivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        # Verificar si la letra está en la palabra
        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            print("¡Correcto!")
        else:
            intentos += 1
            print("Incorrecto. Te quedan", max_intentos - intentos, "intentos.")

        # Verificar si el jugador ha ganado
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print(f"¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
            break
    else:
        mostrar_ahorcado(intentos)
        print(f"¡Perdiste! La palabra era: {palabra_secreta}")

