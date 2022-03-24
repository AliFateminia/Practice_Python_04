import math
def Equation(a, b, c):
    delta = (b ** 2 - (4 * a * c))
    if delta < 0:
        print("The equation has no answer in real numbers")
        Input()
    else:
        Sqrt = math.sqrt(delta)
    x1 = round(((-b + Sqrt) / (2 * a)), 2)
    x2 = round(((-b - Sqrt) / (2 * a)), 2)
    print("x1: ", x1, "    x2: ", x2)
    Input()
def Input():
    a = int(input("Enter a:"))
    if a == 0:
        print("a can not be zero. Try again ")
        Input()
    b = int(input("Enter b:"))
    c = int(input("Enter c:"))
    Equation(a, b, c)
Input()