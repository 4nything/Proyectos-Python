import random

while True:
    number = random.randint(1, 10)
    respuesta = ""
    puntaje = 10
    jugarNuevamente = ""

    def firstHint(numberHint):
        if (numberHint % 2) == 0:
            print("El numero es par.")
        else:
            print("El numero es impar.")

    def secondHint(numberHint, answer):
        if numberHint > answer:
            print("El numero es mayor a su respuesta")
        elif numberHint < answer:
            print("El numbero es menor a su respuesta")

    def thirdHint(numberHint): 
        if (numberHint % 2) == 0:
            print("El numero es divisible por 2.")
        elif (numberHint % 3) == 0:
            print("El numero es divisible por 3.")
        elif (numberHint % 4) == 0:
            print("El numero es divisible por 4.")
        elif (numberHint % 5) == 0:
            print("El numero es divisible por 5.")
        else: 
            print("El numero es primo.")

    def fourthHint(numberHint):
        if (numberHint % 2) == 0:
            print("El numero es multiplo de 2.")
        elif (numberHint % 3) == 0:
            print("El numero es multiplo de 3.")
        elif (numberHint % 4) == 0:
            print("El numero es multiplo de 4.")
        elif (numberHint % 5) == 0:
            print("El numero es multiplo de 5.")
        else: 
            print("El numero es primo.")

    def fifthHint(numberHint, answer):
        if (numberHint % answer) == 0:
            print("El numero es divisible por su respuesta")
        else:
            print("El numero no es divisible por su respuesta")

    def ingresarNumero(resp):
        while resp == "":
            try:
                givenNumber = int(input())
                if (givenNumber >= 1) & (givenNumber <= 10):
                    resp = givenNumber
                else:
                    print("Por favor ingrese un numero entre (1-10): ", end="")
            except:
                (print("Numero invalido, por favor ingrese un numero valido: ", end=""))
        return resp

    print("Bienvenido a Number-Picker por 4nything")
    print("ESTE JUEGO SE BASA EN ADIVINAR EL NUMERO AL AZAR ELEJIDO POR LA COMPUTADORA.\n"+
            "EL NUMERO ES ELEGIDO ENTRE EL 1 Y EL 10\n"+
            "POR CADA VEZ QUE NO ACIERTE A LA RESPUESTA CORRECTA, SE LE DARA UNA PISTA.\n"+
            "EL JUEGO TERMINA UNA VEZ QUE ADIVINE EL NUMERO O SU PUNTAJE LLEGUE A 0.\n"+
            "SU PUNTAJE INICIAL SERA DE 10 Y CADA PISTA CUESTA 2 PUNTOS, POR LO TANTO TIENE 5 CHANCES.\n"+
            "HABIENDO EXPLICADO LAS REGLAS, COMENCEMOS!\n"+
            "INGRESE UN NUMERO (1-10): ", end="")

    respuesta = ingresarNumero(respuesta)

    while respuesta != number:
        if puntaje == 10:
            print("Usted no ha acertado!\nLe daremos una pista: ")
            firstHint(number)
            print("Ingrese un numero del 1-10: ")
            respuesta = ""
            respuesta = ingresarNumero(respuesta)
            puntaje -= 2
        elif puntaje == 8:
            print("Usted no ha acertado!\nLe daremos otra pista: ")
            secondHint(number, respuesta)
            print("Ingrese un numero del 1-10: ")
            respuesta = ""
            respuesta = ingresarNumero(respuesta)
            puntaje -= 2
        elif puntaje == 6:
            print("Usted no ha acertado!\nLe daremos otra pista: ")
            thirdHint(number)
            print("Ingrese un numero del 1-10: ")
            respuesta = ""
            respuesta = ingresarNumero(respuesta)
            puntaje -= 2
        elif puntaje == 4:
            print("Usted no ha acertado!\nLe daremos otra pista: ")
            fourthHint(number)
            print("Ingrese un numero del 1-10: ")
            respuesta = ""
            respuesta = ingresarNumero(respuesta)
            puntaje -= 2
        elif puntaje == 2:
            print("Usted no ha acertado!\nLe daremos otra pista: ")
            fifthHint(number, respuesta)
            print("Ingrese un numero del 1-10: ")
            respuesta = ""
            respuesta = ingresarNumero(respuesta)
            puntaje -= 2
        elif puntaje == 0:
            break
        
    if(respuesta == number):
        print("Usted ha ganado! ¿Desea jugar nuevamente? (si/no): ",end="")
        while jugarNuevamente == "":
            jugarNuevamente = str(input()).lower()
            if jugarNuevamente == "no":
                print("GRACIAS POR JUGAR A NUMBER-PICKER POR 4NYTHING!\n ADIOS.......")
                break
            elif (jugarNuevamente != "si") & (jugarNuevamente != "no"):
                print("Ingrese una respuesta valida (si/no): ", end="")
    elif puntaje == 0:
        print("Usted ha perdido! ¿Desea jugar nuevamente? (si/no): ",end="")
        while jugarNuevamente == "":
            jugarNuevamente = str(input()).lower()
            if jugarNuevamente == "no":
                print("GRACIAS POR JUGAR A NUMBER-PICKER POR 4NYTHING!\n ADIOS.......")
            elif (jugarNuevamente != "si") & (jugarNuevamente != "no"):
                print("Ingrese una respuesta valida (si/no): ", end="")

    if jugarNuevamente == "no":
        break
