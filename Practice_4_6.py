def calcute_lcm():
    global lcm
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if a <= 0 or b<=0:
        print("a and b cannot be zero or negative. Try again ")
        calcute_lcm()
    if a > b:
        Min = b
    else:
        Min = a
    for i in range(1, Min + 1):
        if (a % i == 0) & (b % i == 0):
            lcm = (a * b) / i
    print("lcm:", int(lcm))
    e = input("If you want to continue, enter, 'yes', otherwise enter 'no' :")
    if e == "yes":
        calcute_lcm()
    if e == "no":
        exit()
calcute_lcm()
