x = 0
anio = 1990
# positivo
if x > 0:
    print (x, 'es positivo')
# negativo
if x < 0:
    print (x, 'es negativo')
# cero
if 0 == x:
    print (x, 'es cero')
#Numero par
if x%2 == 0:
    print (x, 'es un numero par')
else:
    print (x, 'es un numero impar')
#numero primo
if x > 1:

    for i in range(2, x):
        if (x % i) == 0:
            print(x, "no es un numero primo")
            break
    else:
        print(x, "es un numero primo")
else:
    print(x, "no es un nuero primo")
#anio biciesto
if anio%4 == 0:
    if anio%100 == 0:
        if anio%400==0:
            print (anio, 'es un año biciesto')
        else:
            print (anio, 'no es un año biciesto')
    else:
        print (anio, 'es un año biciesto')
else:
    print (anio, 'no es un año biciesto')


def funcion ():
    x = input('introduce un numero: ')
    x = int(x)
    anio = input('introduce un año:')
    anio =int(anio)
    if x > 0:
        print(x, 'es positivo')
    # negativo
    if x < 0:
        print(x, 'es negativo')
    # cero
    if 0 == x:
        print(x, 'es cero')
    # Numero par
    if x % 2 == 0:
        print(x, 'es un numero par')
    else:
        print(x, 'es un numero impar')
    # numero primo
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                print(x, "no es un numero primo")
                break
        else:
            print(x, "es un numero primo")
    else:
        print(x, "no es un nuero primo")
    # anio biciesto
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                print(anio, 'es un año biciesto')
            else:
                print(anio, 'no es un año biciesto')
        else:
            print(anio, 'es un año biciesto')
    else:
        print(anio, 'no es un año biciesto')

funcion()
date
