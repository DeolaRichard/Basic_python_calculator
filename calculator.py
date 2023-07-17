def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))


def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))


def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))


def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))


print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")

choice = input("input your choice: ")

if choice == "a" or choice =="A":
    print("Addition")
    a = int(input("Enter first number"))
