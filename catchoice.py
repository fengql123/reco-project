from data import types


def catchoice():
    for cat in types:
        print(cat)
    v = input(
        'Please choose your favorite types of food!(Please separate your choices by spaces.)')
    choices = v.split()
    return choices
