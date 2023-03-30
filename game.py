from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()

correctos=0
incorrectos=0

print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    operator = choice(operators)
    if (operator == "/"):
        number_2 = randrange(1,10)
    else:
        number_2 = randrange(10)
    
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    ingreso = float(input())
    match operator:
        case "/":
            result = number_1 / number_2
        case "*":
            result = number_1 * number_2
        case "+":
            result = number_1 + number_2
        case "-":
            result = number_1 - number_2
    if ingreso == result:
        print("El resultado ingresado es correcto")
        correctos+=1
    else:
        print("El resultado ingresado es incorrecto")
        incorrectos+=1
print("Cantidad de resultados correctos: ", correctos)
print("Cantidad de resultados incorrectos: ", incorrectos)


# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
