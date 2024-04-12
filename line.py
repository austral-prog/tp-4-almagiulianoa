import math
def line():
    A = float (input ("Ingrese el coeficiente A: "))
    B = float (input ("Ingrese el coeficiente B: "))
    X1 = float (input ("Ingrese el coeficiente X1: "))
    X2 = float (input ("Ingrese el coeficiente X2: "))
    print (f"El coeficiente A de su ecuación de la recta es: {A}")
    print (f"El coeficiente B de su ecuación de la recta es: {B}")
    print (f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print (f"El coeficiente X2 de su ecuación de la recta es: {X2}")
    print ("\nPara la siguiente ecuación:")
    print (f"\tY = {A}X + {B}")
    Y1 = A*X1+B
    Y2 = A*X2+B
    print ("\nDados los siguientes puntos:")
    print (f"\tP1 ({X1}, {Y1})")
    print (f"\tP2 ({X2}, {Y2})")
    diferenciaX = (X2 - X1)
    diferenciaY = (Y2 - Y1)
    cuadrado1 = (diferenciaX)**2
    cuadrado2 = (diferenciaY)**2
    resultado1 = (cuadrado1 + cuadrado2)
    resultado2 = (math.sqrt(resultado1))
    print (f"\nLa distancia entre ellos es: {resultado2}")
