import math
num = int(input("Enter your number: "))
w = True
x = 1
while w:
    f = math.factorial(x)
    if f == num:
        print("yes")
        print("x!: ", x)
        break
    if num > f:
        x += 1
    else:
        print("no")
        break





