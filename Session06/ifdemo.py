# age = input('pleas enter your age: ')

# if int(age) >= 18:
#     print('Adult')
# elif int(age) >=12:
#     print('Teenager')
# else:
#     print('Child')
#
# 


# def calculate_bmi(weight, height):
#     bmi = 703 * weight/(height * height)
#     if bmi >=30:
#         print('You are obese, change diet and go to the gym')
#     elif bmi >= 25:
#         print('Overweight')
#     else:
#         if 18.5 < bmi <=25:
#             print('Normal weight')
#         else:
#             print('Underweight')

# calculate_bmi(100, 60)

def compare(varA, varB):
    if isinstance(varA, str) or isinstance(varB, str):
        print ('string involved')        
    else:
        if varA > varB:
            print('Bigger')
        elif varA == varB:
            print('Equal')
        else:
            print('smaller')


# compare('hello', 3)

def print_n(s, n):
    if n <= 0:
        return n
    print(s)
    print_n(s, n-1)
