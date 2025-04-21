#loop
# while loop
# for loop
# while else
# for else

i = 1
while i <= 5:
    print(i, "How are u")
    i += 1
print("_________________")

i = 1
while i <= 5:
    print(i, "How are u")
    i += 1
else:
    print("from else")
print("_________________")


i = 1
while i <= 5:
    print(i, "How are u")
    i += 1
    if i == 3:
        break
else:
    print("from else")