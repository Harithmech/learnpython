# decorators
# adding a function to store common details

def about(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("I am from Bangalore")
        print("I study at ", args[0])
        print("My phone number is: ", args[1])
        print("-------------------")
    return wrapper


@about
def hari(col, *args):
    print("Harith is my name")


@about
def harshi(col, *args):
    print("Harshith is my name")


hari("Mvjce", 7835549)
harshi("alvas", 123467)
