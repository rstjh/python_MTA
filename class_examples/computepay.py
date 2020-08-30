def get_input():
    while True:
        inp_hr = input('Enter Hours: ')
        inp_rate = input('Enter Rate: ')
        try:
            hours = float(inp_hr)
            rate = float(inp_rate)
        except ValueError:
            continue
        else:
            break

    return hours, rate


def calc_gross_pay(h, r):
    if h <= 40:
        pay = h * r
    else:
        pay = (40 * r) + ((h - 40) * r * 1.5)

    print('Pay:', pay)


tup_returned = get_input()
calc_gross_pay(tup_returned[0], tup_returned[1])

