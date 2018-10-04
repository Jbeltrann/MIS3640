"""
Question 1:
If the number, n, is divisible by 4, return True; return False otherwise. Return False if n is divisible by 100 (for example, 1900); the only exception is when n is divisible by 400(for example, 2000), return True.
"""


def is_special(n):
#     """
#     If the number, n, is divisible by 4 (for example, 2020),
#      return True. Return False if n is divisible by 100 (for example, 300);
#      the only exception is when n is divisible by 400(for example, 2400),
#       return True.
#     """
    if n % 4 == 0:
        return  True
    else:
        if n % 100 == 0:
            return False
        elif n % 400 == 0:
                return True
        else:
            return False

# print(is_special(2020))
# print(is_special(300))
# print(is_special(2018))
# print(is_special(2000))


# When you've completed your function, uncomment the
# following lines and run this file to test!


# print(is_special(2020))
# print(is_special(300))
# print(is_special(2018))
# print(is_special(2000))


"""
-----------------------------------------------------------------------
Question 2:
"""


# def detect(a, b, n):
#     """
#     Returns True if either a or b is n, or if the sum or 
#     difference or product of a and b is n. 
#     """
    if a or b == n:
        return True
    elif (a+b) or (a-b) or (a*b) == n:
        return True
    else:
        return False


# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(detect(2018, 9, 2018))
# print(detect(2017, 1, 2018))
# print(detect(1009, 2, 2018))
# print(detect(2020, 2, 2018))
# print(detect(2017, 3, 2018))

"""
-----------------------------------------------------------------------
Question 3:
Write a function with loops that computes
 the sum of all cubes of all the odd numbers
  between 1(inclusive) and n (inclusive if n is not even).
"""
import math


def sum_cubes_of_odd_numbers(n):
    sum = 0
    n = 0
    for i in range(0, n) : 
        sum +=  n**2*(2*n**2 - 1)
   


# When you've completed your function, uncomment the
# following lines and run this file to test!

print(sum_cubes_of_odd_numbers(1))
print(sum_cubes_of_odd_numbers(10))