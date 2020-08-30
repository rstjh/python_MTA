# name = input("Who are You? ")
# print("Welcome", name)

inp_num = input("Europe Floor?")
us_floor = int(inp_num) + 1
print("US Floor", us_floor)


if us_floor < 5:
    print("thats the cheap floors")
elif us_floor > 5:
    print("thats the expensive floors")
else:
    print(f"Its not 5 its: {us_floor}")

print("Goodbye")
