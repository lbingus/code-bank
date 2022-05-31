import time

class cup():
    __content = str()  # milk, tea, coffee...
    __volume = float()  # in mL
    __filled = float()  # in %

    def __init__(cup, c, v, f):
        cup.__content = c
        cup.__volume = v
        cup.__filled = f

    def output(cup):
        print(f'Your cup contains {cup.__content}. It holds {cup.__volume} mL and is {cup.__filled}% full.')
        time.sleep(1)

    def drink(cup):    # allows you to drink from the cup
        cup.__volume -= 20
        cup.__filled = (cup.__volume / 500) * 100
        print(f'After drinking, you have {cup.__volume} mL of {cup.__content} left. That is {cup.__filled}% of'
              f' the original amount. ')
        time.sleep(0.5)
        if cup.__filled == 0:
            cup.full_refill()
        else:
            resp = input(f'Do you want to keep drinking {cup.__content}?\n'
                         'Y/N/Other drink?\n')
            if resp.lower() == 'y':
                time.sleep(0.5)
                cup.drink()
            elif resp.lower() == 'other drink':
                cup.other_drink()
            else:
                return cup, print('Hope you enjoyed your drink!')

    def full_refill(cup):  # allows you to refill your drink; redirects to sippy()
        resp = input('Your cup is empty. Do you want to refill your cup completely?\n'
                     'Y/N?\n')
        if resp.lower() == 'y':
            sippy()
            return cup
        else:
            return cup, print(f'You decided not to refill your cup.')

    def other_drink(cup):  # allows you to change your drink
        time.sleep(0.5)
        resp1 = input('Do you want to drink something else?\n'
                      'Y/N?\n')
        if resp1.lower() == 'y':
            time.sleep(0.5)
            resp2 = input('For this you need to empty your cup and refill manually. Is that okay??\n'
                          'Y/N?\n')
            if resp2.lower() == 'y':
                cup.__content = None
                print('Emptying cup...')
                time.sleep(5)
                cup.full_refill()
                return cup.__content
            else:
                print('Enjoy your drink!')
        else:
            print('Enjoy your drink!')


# ======================================================================================================================


def sippy():
    bev = input('What do you want to fill your cup with?\n')
    print(f'Filling your cup with {bev}...')
    time.sleep(5)
    bev = cup(bev, 500, 100)
    cup.output(bev)
    return bev, cup.drink(bev)


# ----------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    sippy()