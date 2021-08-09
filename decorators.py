# decorators
# adding a function to store common details

def about(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("I am from Bangalore")
        print("-------------------")
    return wrapper


@about
def hari():
    print("Harith is my name")


@about
def harshi():
    print("Harshith is my name")


hari()
harshi()
