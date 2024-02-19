from calcular_puntuacion import calcular_puntuacion

# Función para imprimir con color
def imprimir_resultado_test(test_name, passed):
    mensaje = f"{test_name} pasado" if passed else f"{test_name} fallado"
    color = '\x1b[32m' if passed else '\x1b[31m'  # verde si pasa, rojo si falla
    print(f"{color}{mensaje}\x1b[0m")

# Casos de prueba
def test1():
    result = calcular_puntuacion("20x1")
    imprimir_resultado_test("Test 1", result == 20)

def test2():
    result = calcular_puntuacion("20x0")
    imprimir_resultado_test("Test 2", result == 0)

def test3():
    result = calcular_puntuacion("10x3 & 10x0")
    imprimir_resultado_test("Test 3", result == 30)

def test4():
    result = calcular_puntuacion("5 & 5 & 3 & 17x0")
    imprimir_resultado_test("Test 4", result == 16)

def test5():
    result = calcular_puntuacion("0 & 5 & 5 & 3 & 16x0")
    imprimir_resultado_test("Test 5", result == 13)

def test6():
    result = calcular_puntuacion("5 & 5 & 3 & 17x1")
    imprimir_resultado_test("Test 6", result == 33)

def test7():
    result = calcular_puntuacion("10 & 3 & 2 & 16x0")
    imprimir_resultado_test("Test 7", result == 20)

def test8():
    result = calcular_puntuacion("0 & 10 & 3 & 2 & 16x0")
    imprimir_resultado_test("Test 8", result == 18)

def test9():
    result = calcular_puntuacion("10 & 3 & 2 & 16x1")
    imprimir_resultado_test("Test 9", result == 36)

def test10():
    result = calcular_puntuacion("18x0 & 10 & 1 & 1")
    imprimir_resultado_test("Test 10", result == 12)

def test11():
    result = calcular_puntuacion("18x0 & 5 & 5 & 1")
    imprimir_resultado_test("Test 11", result == 11)

def test12():
    result = calcular_puntuacion("12x10")
    imprimir_resultado_test("Test 12", result == 300)

# Ejecución de los tests
test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
test9()
test10()
test11()
test12()
