n = int(input("Enter a number: "))

factorial = 1
i = 1
while i <= n:
    factorial *= i
    print(i)
    i += 1
print("Factorial of", n, "is", factorial)

#output:
# Enter a number: 5
# 1
# 2
# 3
# 4
# 5
# Factorial of 5 is 120
