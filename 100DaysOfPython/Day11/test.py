x = input("Enter y or n: ")


def func():
    if x == "y":
        go = True
    elif x == "n":
        go = False

    while go:
        print("went")
        func()


func()
