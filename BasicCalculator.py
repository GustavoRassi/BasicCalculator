# Program: Basic calculator with python
# Description: Inputs user name and performs basic arithmetic calculation given by the user.
# IDE: PyCharm
# Developed by: Gustavo Rassi (student)
#===================================================
# Input name for the user
name = input("Please enter your name: ")
print("Hello", name + ", welcome to PyCharm IDE!")
#===================================================
# Function to perform the calculation
# Parameters: Tow integer numbers and an operator.
# Returns: The value after operation or sentinel value.
def calculator(number_1, number_2, op):
    if op == "+": # Add operator
        return number_1 + number_2
    elif op == "-": # Subtract operator
        return number_1 - number_2
    elif op == "*": # Multiplication operator
        return number_1 * number_2
    elif op == "/": # Division operator
        return number_1 / number_2
    else: # No existent operator: return sentinel value
        return -1

# Program proceeds if user says 'yes'
answer = input("Do you want to proceed with the program? ")
while answer == "Yes" or answer == "yes":

    # Variables for the integer values
    number_1 = int(input("Please enter a number: "))
    number_2 = int(input("Please enter a second number: "))

    # Variable for the operator
    op = input("Please enter an operator (+, -, * or /): ")

    # Check if operator does not exist
    if calculator(number_1, number_2, op) == -1:
        print("Operator", op, "does not exist.")
    else:
        # Operator exist, so perform calculation
        print(number_1, op, number_2, "=", calculator(number_1, number_2, op))

    # Repeat how many times you'd like until answer is 'no'
    answer = input("Do you want to perform another calculation? ")

# Exists the program
if answer == "No" or answer == "no":
    print("\nThank you for using this program,", name + "!")