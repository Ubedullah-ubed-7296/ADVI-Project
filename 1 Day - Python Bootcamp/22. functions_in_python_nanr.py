# syntax
# def function_name(parameters):
#     statements

# 1. function with no argument and no return value

def display():
    for i in range(5):
        print("Hello")

display() # function call


def display():
    for i in range(5):
        print("Hello")

print("Start")
display()
print("End")




def sum():
    a = 10
    b = 20
    c = a + b
    print("Sum = ", c)

sum()


def sum():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a + b
    print("Sum = ", c)

sum()