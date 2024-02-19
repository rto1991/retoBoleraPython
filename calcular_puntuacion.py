def calcular_puntuacion(input):
    tiradas = input.split(' & ')
    puntuacion = 0
    ronda = 1
    tirada = 1

    for tirada_actual in tiradas:
        if 'x' in tirada_actual:
            cantidad, bolo = tirada_actual.split('x')
            puntuacion += int(cantidad) * int(bolo)
            break
        else:
            bolos = tirada_actual.split()
            suma = 0
            for i, bolo in enumerate(bolos):
                if bolo == '/':
                    suma += 10 - int(bolos[i - 1])
                elif bolo == '10':
                    if ronda != len(tiradas) and '10' in tiradas[tiradas.index(tirada_actual) + 1]:
                        suma += 10 + int(tiradas[tiradas.index(tirada_actual) + 1][0])
                    else:
                        suma += 10 + int(tiradas[tiradas.index(tirada_actual) + 1])
                else:
                    suma += int(bolo)
            puntuacion += suma

        if tirada == 2:
            ronda += 1
            tirada = 1
        else:
            tirada += 1

    return puntuacion
