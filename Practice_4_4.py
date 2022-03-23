def counter():
    Input = str(input("Enter your sentence:"))
    # Input = "python is a powerful programming language" >>> count = 6
    count = Input.split()
    print("count: ", len(count))
    counter()
counter()