astr = [1,2,3]

try:
    istr = int(astr)  # try this risky conversion to an int

except TypeError:
    istr = -1
    print("Error raised: Type is bad")

except ValueError:
    istr = -1
    print("Error raised: Value is bad")

except:
    istr = -1
    print("generic error")

else:
    print(f"I work when No Errors were raised, this is the else clause: {istr}")  # only runs when NO error have been raised

finally:
    print(f"I'm always working, this is the finally clause the istr value is:{istr}")  # ALWAYS runs

