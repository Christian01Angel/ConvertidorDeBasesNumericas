def transformar_a_base_menor(base2, entero, resultado):
    if entero >= base2:
        resultado += str(round(entero % base2))
        if (entero // base2) < base2:
            resultado += str(entero // base2)
            resultado = resultado[::-1]
            print(resultado)
            return int(resultado)
        else:
            transformar_a_base_menor(base2, (entero // base2), resultado)


def transformar_a_base_mayor(baseActual, baseNueva, numero, resultado):
    # Primero cambio a base 10 y luego aplico, si es necesario, un cambio ala base solicitada
    numero_str = str(numero)
    largo = len(numero_str)
    resultado = 0
    for x in numero_str:
        largo = largo - 1
        resultado += int(x)*(baseActual ** largo)
    print(resultado)
    return resultado


def reintentar():
    decision = input('Desea ingresar otro número? (S para Si /N para No) ')
    if decision in 'Ss':
        return True
    elif decision in 'Nn':
        return False
    else:
        print('Valor ingresado no valido, por favor intente nuevamente')
        return None


print('Aplicacion para convertir números de una base a otra')

condicion = True
while condicion:
    base1 = int(input('Cual es la base del número a ingresar?  '))
    base2 = int(input('A que base desea transformarlo?  '))
    numero = int(input(f'Escriba el número a transformar a base {base2}:  '))
    resultado = ""
    print(f'Número elegido: {numero}')
    if base1 > base2:
        resultado = transformar_a_base_menor(base2, numero, resultado)
        print(f'Resultado del número (en base {base1}) convertido a base {base2}: {resultado}')
    elif base2 > base1:
        resultado = transformar_a_base_mayor(base1, base2, numero, resultado)
        print(f'Resultado del número (en base {base1}) convertido a base {base2}: {resultado}')
    cond_reintentar = True
    condicion = reintentar()
    while condicion == None:
        condicion = reintentar()