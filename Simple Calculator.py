#   Creating a simple add and subtract calculator with python

#       Defining the functions for addition and subtraction
def addition(x, y):
    return x + y
def subtraction(x, y):
    return x - y

#   Defining the main function of the calculator
#       Having 3 variables to store the selected numbers and operator using the input() function
#           Main will be using IF statements based on the operator sign
def main():
    print('Hello There, Welcome to my simple calculator powered by YOU:  ')

    first_choice_number = float(input("Please enter your first number: "))
    second_choice_number = float(input("Now please enter your second number: "))
    operator = input("Numbers are saved!!! Now please choose an operator (+ OR -): ")

    if operator == "+":
        print(first_choice_number, operator, second_choice_number, "=", addition(first_choice_number, second_choice_number))
    elif operator == "-":
        print(first_choice_number, operator, second_choice_number, "=", subtraction(first_choice_number, second_choice_number))
    else:
        print("Sorry but the Operator you chose does not exist")

#   Running main()
main()
