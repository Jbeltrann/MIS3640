# Define a function called hotel_cost with one argument days as user input.
#  The hotel costs $140 per day. So, the function hotel_cost should return 140 * days.
price= 0
days= 0
def hotel_cost(days):
    days= int(input('Enter amount of days: '))
    price = 140 * days
    return price
print(hotel_cost(0))

# Define a function called plane_ride_cost that takes a string, city, as user input. 
# The function should return a different price depending on the location, similar to the code example above. 
#  Below are the valid destinations and their corresponding round-trip prices.
# "Charlotte": 183 "Tampa": 220 "Pittsburgh": 222 "Los Angeles": 475


def plane_ride_cost (city):
    city = str(input('Enter city: '))
    price = 0
    if city == 'Charlotte':
        print(183)
    elif city == 'Tampa':
        print(220)
    elif city == 'Pittsburgh':
        print(222)
    elif city == 'Los Angeles':
        print(475)
    else:
        print('Not a valid destination')

print(plane_ride_cost('Tampa'))

#  Below your existing code, define a function called rental_car_cost with an argument called days. 
# Calculate the cost of renting the car: Every day you rent the car costs $40.(cost=40*days)
# if you rent the car for 7 or more days, you get $50 off your total(cost-=50).
# Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total. 
# You cannot get both of the above discounts. Return that cost.

price = 0
days = 0
def rental_car_cost (days):
    days = int(input('Enter number of days for rental: '))
    price = days * 40
    if days >= 7:
        price -= 50
    elif days >= 3:
        price-=20
    else:
        print('You cannot get both of the above discounts. However, your total is $',price)
    return price
print(rental_car_cost(0))


# Then, define a function called trip_cost that takes two arguments, city and days.
# Like the example above, have your function print the sum of calling the 
# rental_car_cost(days), hotel_cost(days), and plane_ride_cost(city) functions.

def trip_cost(city, days, spending_money):
  price = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
  return price
print(trip_cost('Tampa', 3, 500)
    
# Modify your trip_cost function definition. Add a third argument, spending_money (also a user input). Modify what the trip_cost function does. Add the variable `spending_money to the sum that it prints.
# Finally, execute trip_cost function to print the total cost of your trip.