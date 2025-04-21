java = int(input("Enter Java marks: "))
python = int(input("Enter Python marks: "))
c = int(input("Enter C marks: "))

total = java + python + c
average = total / 3

print("Total marks: ", total)
print("Average marks: ", average)

if (average >= 70):
    print("Distinction")
elif(average >= 60 and average < 70):
    print("First Div")
elif(average >= 50 and average < 60):
    print("Second Div")
elif(average >= 40 and average < 50):
    print("Third Div")
else:
    print("Failed")