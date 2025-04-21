n = int(input("Enter a number: "))
temp = n
sum = 0

while n > 0:
    res = n % 10
    sum += res ** 3
    n = n // 10

if (sum == temp):
    print(temp, "Armstrong number")
else:   
    print(temp, "Not an Armstrong number")