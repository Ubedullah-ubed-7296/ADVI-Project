a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > c:
    if a > b:
        print(a)
    else:
        print(b)
else:
    if c > b:
        print(c)
    else:
        print(b)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    if b > c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b > c:
    if a > c:
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if a > b:
        print(c, a, b)
    else:
        print(c, b, a)