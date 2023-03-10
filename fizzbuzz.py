#"Escriba un programa que imprima los números desde 1 hasta 100. 
# Pero en cada número que sea múltiplo de 3 se deberá imprimir "Fizz" en el lugar del número, 
# en  caso que  los números que sean múltiplos de 5 se debera imprimir "Buzz". 
# y por cada número que sea múltiplo de 3 y 5 se deberá imprimir FizzBuzz"


for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0:
        print("Buzz")

    else:
        print(i)
    