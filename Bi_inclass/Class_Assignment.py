# 1. Planting Grapevines

# A vineyard owner is planting several new rows of grapevines, and needs to know how many grapevines to plant in each row. She has determined that after measuring the length of a future row, she can use the following formula to calculate the number of vines that will fit in the row, along with the trellis end-post assemblies that will need to be constructed at each end of the row:



# The terms in the formula are:

# V is the number of grapevines that will fit in the row.
# R is the length of the row, in feet.
# E is the amount of space, in feet, used by an end-post assembly.
# S is the space between vines, in feet.
# Write a program that makes the calculation for the vineyard owner. The program should ask the user to input the following:
r = float(input('Enter the length of the row, in feet: '))
e = float(input('Enter the amount of space, in feet, used by an end-post assembly: '))
s = float(input('Enter the space between vines, in feet: '))
v = (r - 2*e) / s
print('There are', v,'grapevines in each row')

# The length of the row, in feet
# The amount of space used by an end-post assembly, in feet
# The amount of space between the vines, in feet
# Once the input data has been entered, the program should calculate and display the number of grapevines that will fit in the row.

# 2. Age Classifier

# Write a program that asks the user to enter a person’s age. 
# The program should display a message indicating whether the person is an 
# infant, a child, a teenager, or an adult. Following are the guidelines:

# age = int(input("Please enter person's age: "))

if age > 18:
    print('They are an adult')
elif age > 12 and age < 18:
    print('They are a teenager')
    if age > 6 and age < 13:
        print('They are a child')
else:
    print('They are an infant')


# If the person is 1 year old or less, he or she is an infant.
# If the person is older than 1 year, but younger than 13 years, he or she is a child.
# If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
# If the person is at least 20 years old, he or she is an adult.
# 3. Write a program with a loop that asks the user to enter a series of positive numbers. 
# The user should enter a negative number to signal the end of the series.
#  After all the positive numbers have been entered, the program should display their sum
list = []
x = 1
sum = 0
while x > 0:
    x = float(input('Enter a positive integer: '))
    sum+= x
    if x<0:
        print(sum(list)):
        break
    list.append(x)
print(list)
# 4. Write a program that calculates the amount of money a person would earn over a period of time 
# if his or her salary is one penny the first day, two pennies the second day, and continues to double each day.
#  The program should ask the user for the number of days. Display a table showing what the salary was for each 
# day, then show the total pay at the end of the period. The output should be displayed in a dollar amount,
# not the number of pennies.

sal = 0.01
total = 0
days= int(input('Enter number of days: '))
for x in range(days):
    total += sal
    print(x+1, '$',sal)
    sal*= 2
print(round(total,2))
# 5. Write a program that uses nested loops to collect data and calculate the average rainfall 
# over a period of years. The program should first ask for the number of years. The outer loop will 
# iterate once for each year. The inner loop will iterate twelve times, once for each month. 
# Each iteration of the inner loop will ask the user for the inches of rainfall for that month. 
# After all iterations, the program should display the number of months, the total inches of rainfall,
#  and the average rainfall per month for the entire period.

years = int(input('Enter number of years: '))
months = 12
total = 0
for x in range(years):
    for y in range(months):
        rain = float(input('Enter rainfall in inches: ' + str(y+1)))
        total += rain 

print( ' No. of months: ', years*months)
print('Total inches of rainfall: ', total)
print('Average of total rainfall', total/(years*months))
