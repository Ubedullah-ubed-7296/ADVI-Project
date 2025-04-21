n = int(input("Enter a number: "))
i = 1
count = 0
while i <= n:
    if n % i == 0:
        count += 1
    i += 1
if count == 2:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")



n = int(input("Enter a number: "))
i = 1
count = 0
while i <= n // 2:
    if n % i == 0:
        print(n, "is not a prime number")
        break
    i += 1
else:
    print(n, "is a prime number")