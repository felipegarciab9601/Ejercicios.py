import random


def run():
    print("Hola!!! Bienvenido al juego de adivinar un numero /n Las reglas son sencillas")
    number = int(input('Ingresa un numero cualquiera：'))
    number_found = False
    random_number = random.randint(0, number)

    while not number_found:
        number = int(input('Intenta adivinar ahora el numero oculto!：'))

        if number == random_number:
            print('Felicidades. Encontraste el número')
            number_found = True
        elif number > random_number:
            print('El número es más pequeño')
        else:
            print('El número es más grande')


if __name__ == '__main__':
    run()