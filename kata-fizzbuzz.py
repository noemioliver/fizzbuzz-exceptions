# En esta kata, se solicita al usuario un numero, si este es:
# - Divisible entre 3, el programa debe imprimir "Fizz"
# - Divisible entre 5, el programa debe imprimit "Buzz"
# - Divisible entre 3 y entre 5, el programa debe imprimir "FizzBuzz"
# - Si no es divisible ni entre 3 ni entre 5, debe imprimir el número

def fizzbuzz(i) -> str:
    if i % 15 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return str(i)

if __name__ == "__main__":
    try:
        i = int(input("dame un numero: "))
        print(fizzbuzz(i))
    except ValueError:
        print("Error solo se aceptan numeros")
