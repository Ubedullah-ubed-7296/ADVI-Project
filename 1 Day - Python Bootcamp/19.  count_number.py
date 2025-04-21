n = int(input("Enter a number: "))
count = 0

while n > 0:
    count += 1
    n = n // 10

print("Number of digits in the number is", count)


n = int(input("Enter a number: "))
sum = 0

while n > 0:
    res = n % 10
    sum += res
    n = n // 10

print("Sum of digits in the number is", sum)


n = int(input("Enter a number: "))
sum = 0

while n > 0:
    res = n % 10
    sum += res * res
    n = n // 10

print("Sum of square of the digits in the number is", sum)


n = int(input("Enter a number: "))
sum = 0

while n > 0:
    res = n % 10
    sum += res * res * res
    n = n // 10

print("Sum of cube of the digits in the number is", sum)