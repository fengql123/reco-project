from catchoice import catchoice
from makechoice import makechoice
from if_n import if_n


def recommendation():
    print('Welcome to the restaurant recommendation program!')
    choice = input(
        'Would you like to have a view of the categories of the restaurants?(y/n)')
    if choice == 'y':
        choice2 = catchoice()
        makechoice(choice2)
    else:
        if_n()


recommendation()
