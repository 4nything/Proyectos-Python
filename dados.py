# Importamos la libreria de seleccion al azar
import random
import msvcrt

# Definimos la funcion que hara la mezcla de los dados
def tirarDados():
    print("Tirando dados...") # Impresion para atractivo visual
    valores = [1, 2, 3, 4, 5, 6] # Definimos los valores que poseen los dados
    dado1 = random.choice(valores) # Definimos el valor del dado 1 con la seleccion al azar del array de valores con la libreria random y la funcion choice
    dado2 = random.choice(valores) # Definimos el valor del dado 2 al igual que el dado 1

    dadoSuma = dado1 + dado2 # Sumamos los valores de los 2 dados

    print("Valor de dado1: "+ str(dado1)+                       # Imprimimos el valor del dado 1
            "\nValor de dado2: "+ str(dado2)+                   # Imprimimos el valor del dado 2
            "\nLa suma de los dados es de: "+ str(dadoSuma))    # Imprimimos el valor de la suma
    return dadoSuma # Retornamos el valor de la suma de los dados


jugar = tirarDados() # Invocamos la funcion de mezcla para tirar dados y almacenamos el valor de la suma en una variable "Jugar"

while jugar: # Indicamos una iteracion para definir que hacer segun cada valor de los dados
    if jugar == 4:                                                          # Si la suma de dados es igual a 4,
        print("Usted ha ganado la mano")                                    # le decimos al usuario que ha ganado
        print("Toque una tecla para seguir jugando o presione "+            # y le damos 2 opciones, seguir jugando o no jugar
        "'ESC' para finalizar")                                             
        key = msvcrt.getch()                                                # Inicializamos la variable de la tecla como vacia
        if key == b'\x1b':                                                  # Si la tecla es 'ESC',
            print("El juego ha finalizado. Usted ha ganado!")               # entonces finalizamos el juego
            break
        else:                                                           
            print("Volviendo a mezclar...")                                 # Si no es 'ESC' entonces volvemos a tirar los dados
            jugar = tirarDados()
    elif jugar < 4:                                                         # Si la suma de los dados es menor a 4,
        print("Has perdido! \nJuego terminado")                             # le decimos al jugador que perdio y finalizamos el juego
        break
    elif jugar > 4:                                                         # Si la suma de los dados es mayor a 4,
        print("Volviendo a mezclar...")                                     # volvemos a tirar los dados
        jugar = tirarDados()
    