from data import restaurant_data
from catchoice import catchoice


def makechoice(choice):
    for item in choice:
        for thing in restaurant_data:
            if item == thing[0]:
                print(thing[1])
                print(f'Price Rating: {thing[2]}/5')
                print(f'Food Rating: {thing[3]}/5')
                print(f'Address: {thing[4]}')
    choice2 = input('Would you like to choose categories again?y/n')
    if choice2 == 'y':
        c = catchoice()
        makechoice(c)
    if choice2 == 'n':
        return print('Thank you for using this program!')
