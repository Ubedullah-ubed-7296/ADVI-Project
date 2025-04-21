# 3. function with argument and with return type

def sum(a, b):
    c = a + b
    return c

res = sum(10, 20)
print("Sum = ", res)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
res = sum(x, y)
print("Sum = ", res)




def max(a, b):
    if a > b:
        return a
    else:
        return b
    
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
res = max(x, y)
print("Max = ", res)





def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
res = isprime(n)
if res == True:
    print(n, "is prime")
else:
    print(n, "is not prime")




def addsub(a, b):
    c = a + b
    d = a - b
    return c, d

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
res1, res2 = addsub(x, y)
print("Sum = ", res1)
print("Sub = ", res2)
