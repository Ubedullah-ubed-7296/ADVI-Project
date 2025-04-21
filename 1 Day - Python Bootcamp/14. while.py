n = int(input("Enter a number: "))

i = 1
while i <= 5:
    print(i, "How are u")
    i += 1
    if i == n:
        break
else:
    print("from else")

#output:
# Enter a number: 3
# 1 How are u
# 2 How are u

# Enter a number: 5
# 1 How are u
# 2 How are u
# 3 How are u
# 4 How are u
# 5 How are u
# from else


i = 1
while i <= 10:
    i += 1
    if i < 5:
        continue
    print(i, "How are u")
else:
    print("from else")