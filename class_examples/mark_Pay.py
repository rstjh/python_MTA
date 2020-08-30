def get_input():
    inp_hr = input('Enter Hours: ')
    inp_rate = input('Enter Rate: ')
    global hours
    hours = float(inp_hr)
    global rate
    rate = float(inp_rate)

def calc_gross_pay(h, r):
    if h <= 40:
        pay = h * r
    else:
        pay = (40 * r) + ((h - 40) * r + 1.5)
        print('Pay:', pay)

get_input()
calc_gross_pay(hours, rate)


