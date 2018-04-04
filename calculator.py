"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

# repeat forever:
while True:
    # get input
    user_input = raw_input("> ")
    # tokenize input
    tokens = user_input.split(" ")
    action = tokens[0]
    # if the first token is "q":
    if action == 'q':
        # quit
        break
    # else:
    else:
        # decide which math function to call based on first token
        # define num1 and convert to float
        num1 = float(tokens[1])

        # if only 1 number:
        if action in ['square', 'cube']:
            #if square then square()
            if action == 'square':
                print square(num1)
            #if cube then cube()
            if action == 'cube':
                print cube(num1)
        # if 2 or 3 numbers:
        elif action in ['+', '-', '*', '/', 
            'pow', 'mod', 'x+', 'cubes+']:
            num2 = float(tokens[2])
             # if + then add()
            if action == '+':
                print add(num1, num2)
             # if - then subtract()
            if action == '-':
                print subtract(num1, num2)
            # if * then multiply()
            if action == '*':
                print multiply(num1, num2)
           #  if / then divide()
            if action == '/':
                print divide(num1, num2)   
           #  if pow then pow()
            if action == 'pow':
                print power(num1, num2)
            # if mod then mod()
            if action == 'mod':
                print mod(num1, num2)
            # if x+ then add_mult()
            if action == 'x+':
                print add_mult(num1, num2, num3=float(tokens[3]))
            # if cubes+ then add_cubes()
            if action == 'cubes+':
                print add_cubes(num1, num2)
