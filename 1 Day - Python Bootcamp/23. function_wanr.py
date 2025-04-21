# 2. function with argument and no return value
def display(n):
    print("n = ", n)

display(10)
display(23.5)
display("Sachin")



def display(n):
    print("n = ", n, "Type = ", type(n))

display(10)
display(23.5)
display("Sachin")




def sum(a, b):
    c = a + b
    print("Sum = ", c)

sum(10, 20)
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
sum(x, y)