import math
def Equation(a, b, c):
    delta = math.sqrt(abs(b ** 2 - (4 * a * c)))
    x1 = round(((-b + delta) / (2 * a)), 2)
    x2 = round(((-b - delta) / (2 * a)), 2)
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