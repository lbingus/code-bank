import time
from tools import num_only

def bmi_calc():
    print('Hello! with this program you can calculate your body mass index (BMI). For this, we need'
          'some information from you: ')
    print('How much do you weigh in kilograms?')
    mass = num_only()
    print('How tall are you in metres?')
    height = num_only()
    bmi = round((mass / (height * 2)), 1)   # rounds result to one decimal place
    category = ''

    print('Thank you. Please wait while we calculate your BMI...')
    time.sleep(5)

    if 148 > bmi >= 30.0:
        category = 'Adipose'
        print(f'Thank you very much for your patience! Your BMI is {bmi} ({category}).')
    elif 29.9 >= bmi >= 25.0:
        category = 'Overweight'
        print(f'Thank you very much for your patience! Your BMI is {bmi} ({category}).')
    elif 24.9 >= bmi >= 18.5:
        category = 'Normal weight'
        print(f'Thank you very much for your patience! Your BMI is {bmi} ({category}).')
    elif 18.4 >= bmi >= 12.0:
        category = 'Underweight'
        print(f'Thank you very much for your patience! Your BMI is {bmi} ({category}). '
              f'You are in acute danger. Please see a doctor as soon as possible.')
    else:
        print(f'Thank you very much for your patience! Your BMI is {bmi}. You should not '
              f'actually be able to get this result. \nCongratulations! '
              f'You are (literally) impossible!')


# ----------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    bmi_calc()