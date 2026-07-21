def new_copy_error():
    while True:
        try:
            new_copies = int(input("How many copies of it are you donating? "))
            break
        except ValueError:
            print("Please do not enter anything here except for numbers")
    return new_copies