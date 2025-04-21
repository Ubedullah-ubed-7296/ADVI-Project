java = int(input("Enter Java marks: "))
python = int(input("Enter Python marks: "))
c = int(input("Enter C marks: "))

total = java + python + c
average = total / 3

print("Total marks: ", total)
print("Average marks: ", average)

if (average >= 70):
    print("Distinction")
if(average >= 60 and average < 70):
    print("First Div")
if(average >= 50 and average < 60):
    print("Second Div")
if(average >= 40 and average < 50):
    print("Third Div")
if(average < 40):
    print("Failed")