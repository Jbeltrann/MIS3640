# 1. You walk into a store where each item is priced according to the letters in its name:
# 'a' costs $1, 'b' is $2, and so on. Write a program that prints a receipt for this wacky store:

# bananas $52
# rice $35
# paprika $72
# potato chips $78
# ------------------------
# Total $237


groceries = ['bananas', 'rice', 'paprika', 'potato chips']

def receipt(groceries):
    sum = 0
    max_length = len(max(groceries, key=len)) + 10
    for item in groceries:
        price = 0
        for letter in item:
            price += ord(letter)-96
        print('{} ${}'.format(item, price))
        sum += price
        price_string = '${}'.format(price)
        num_of_spaces = max_length - len(item) - len(price_string)
        item_string = item + ' ' * num_of_spaces + price_string
        print(item_string)

    print('-' * max_length)
    total_price_string = '${}'.format(price)
    num_of_spaces = max_length - len('Total') - len(total_price_string)
    print('Total' + ' ' * num_of_spaces + total_price_string)

receipt(groceries)

# Hint: the built-in function ord and chr may be useful.

# 2. Modify your solution to Part 1 to align the prices and add cents. 
# You may assume that "potato chips" is the longest item name.

# bananas               $52.00
# rice                  $35.00
# paprika               $72.00
# potato chips          $78.00
# ----------------------------
# Total                $237.00


# 3. Modify your Part 2 solution to adapt to the length of the longest name. For example, if you removed potato chips from the list of items, it might print:

# bananas          $52.00
# rice             $35.00
# paprika          $72.00
# ------------------------
# Total           $237.00