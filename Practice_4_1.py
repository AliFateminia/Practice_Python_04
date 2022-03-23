m = int(input("enter m : "))
n = int(input("enter n : "))
for i in range(m):
    for j in range(0, n, 2):
        if i % 2 == 0:
            print("*" + "#", end="")
        if i % 2 != 0:
            print("#" + "*", end="")
    print("")



