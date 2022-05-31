# Collection of useful functions


def num_only():
    try:
        num = float(input('Enter a number: \n'))
        return num
    except:
        print('Not a number!')
        num_only()


# ----------------------------------------------------------------------------------------------------------------------


line_num = 0


def lineprint(*args):
    global line_num
    line_num += 1
    line = str(args)[1:-1]
    if len(line) > 0 and line[-1] == ',':
        line = line[:-1]
    print(f'{line_num:02}) {line}')

# ----------------------------------------------------------------------------------------------------------------------
