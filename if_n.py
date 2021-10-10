from showranking import showrankingfood
from showranking import showrankingprice


def if_n():
    choice3 = input(
        'We grouped the restaurants according to their rating as well! Please choose the type of rating you want to see...(price/food)')
    if choice3 == 'food':
        showrankingfood()
    elif choice3 == 'price':
        showrankingprice()
    else:
        print('Please type price or food...(NO CAPS)')
        print('Try again...')
        if_n()
    choice4 = input(
        'Would you like to see the ranking of ratings again?y/n')
    if choice4 == 'y':
        if_n()
    elif choice4 == 'n':
        print('Thank you for using the program!')
