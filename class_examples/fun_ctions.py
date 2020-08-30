def my_function(x, y, z):
    """ This function takes 3 parameters
        - prints the 3 parameters
        - returns the result of adding or concatenating 2 of the parameters"""
    print(x, y, z)
    return x + y


def add_two(x, y):
    """ This functions takes 2 numeric parameters
    adds them and returns teh sum """
    return x+y


def lumberjack():
    """This function takes no parameters, returns no values
    as its purpose is to print some text"""
    print("I'm a lumberjack and I'm ok")
    print("I'm a lumberjack and I'm ok")


returned_values = my_function("a", "b", "c")
print(returned_values)

print("This fruitful function returns its return value:", add_two(5,9))
print("This fruitless function returns nothing:", lumberjack())
