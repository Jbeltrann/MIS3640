L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']    
]
# print(L[-2])

# AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
# # numbers = [42, 123]
# empty = []
# print(AFC_east, numbers, empty)

# for team in AFC_east:
    # print(team)

# numbers = [2, 0, 1, 6, 9]

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
    
# print(numbers)

# my_list = ['spam', 1, ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Giants'], 
#             [1, 2, 3]]
# print(len(my_list))


# def capitalize_all(t):
#     res = []
#     for s in t:
#         res.append(s.capitalize())
#     return res

# t = [1, 2, 3]
# print(sum(t))

def histogram(s):
    d = dict()
    for letter in s:
        d[letter] = d.get(letter, 0) + 1
    return d 

print(histogram('hahahaha'))

grades = {}

import random

for name in roster:
    if name[0] == 'A':
        grades[name] = random.randint(60, 90)
    grades[name] = random.randint(90, 100)
