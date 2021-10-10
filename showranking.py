from data import pricerank
from data import f


def showrankingfood():
    food = f
    for item in food:
        print('')
        print(item[1])
        print(f'Type: {item[3]}')
        print(f'Food Rating: {item[0]}/5')
        print(f'Price Rating: {item[2]}/5')
        print(f'Address: {item[4]}')
        print('')


def showrankingprice():
    price = pricerank()
    for item in price:
        print('')
        print(item[1])
        print(f'Type: {item[3]}')
        print(f'Price Rating: {item[0]}/5')
        print(f'Food Rating: {item[3]}/5')
        print(f'Address: {item[4]}')
        print('')
