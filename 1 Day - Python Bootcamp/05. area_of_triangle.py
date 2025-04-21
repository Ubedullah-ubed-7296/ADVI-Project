import math

a = eval(input("Enter base of triangle: "))
b = eval(input("Enter height of triangle: "))
c = eval(input("Enter side of triangle: "))

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
perimeter = a + b + c
print("Area of triangle is: ", area)
print("Perimeter of triangle is: ", perimeter)