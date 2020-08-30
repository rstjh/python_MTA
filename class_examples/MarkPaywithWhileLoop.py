def get_input():
    inp_hr = input('Enter Hours: ')
    inp_rate = input('Enter Rate: ')
    global hours
    hours = float(inp_hr)
    global rate
    rate = float(inp_rate)


def calc_gross_pay():
    get_input()
    if hours <= 40:
        pay = hours * rate
    else:
        pay = (40 * rate) + ((hours - 40) * rate + 1.5)
        print('Pay:', pay)
        print('')


calculatePay = 'yes'
while calculatePay == 'yes':
    inp_question = input('would you like to calculate the Pay, Yes or No?')
    if inp_question == 'yes' or inp_question == 'y' or inp_question == 'Yes' or inp_question == 'Y':
        calculatePay = 'yes'
        calc_gross_pay()
    else:
        calculatePay = "No"
