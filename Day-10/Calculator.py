
# calculative functions
def add(num1, num2):
    return num1+num2


def subtract(num1, num2):
    return num1-num2


def multiply(num1, num2):
    return num1*num2


def divide(num1, num2):
    return num1/num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
cont = True
num1 = int(input("Enter the number: "))
for symbol in operations:
    print(symbol)
while cont:
    operator = input("Enter the operations you want to perform: ")
    num2 = int(input("Enter the number: "))
    operation = operations[operator]
    answer = operation(num1, num2)
    print(f"{num1} {operator} {num2} = {answer}")
    if input("Type 'y' to continue operating, or type 'n' to stop : ") == 'y':
        num1 = answer
    else:
        cont = False