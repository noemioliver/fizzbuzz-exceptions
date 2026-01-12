<<<<<<< HEAD
<<<<<<< HEAD
for i in range(1, 101):
=======
for i in range(1, 100):
>>>>>>> 7f47ca22403aa6b77c308e5f366b09e052ac4325
=======
# En esta kata, se solicita al usuario un numero, si este es:
# - Divisible entre 3, el programa debe imprimir "Fizz"
# - Divisible entre 5, el programa debe imprimit "Buzz"
# - Divisible entre 3 y entre 5, el programa debe imprimir "FizzBuzz"
# - Si no es divisible ni entre 3 ni entre 5, debe imprimir el número

for i in range(1, 100):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
>>>>>>> 607fb222f8a62b5a54e64fb95bca9c3bb9b716fd
