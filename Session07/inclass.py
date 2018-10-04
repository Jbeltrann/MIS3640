result = 0

# for i in range(10):
#     print ('current number to be added', i +1)
#     result = result + i + 1
#     print ('New result after this iteration:', result)




# for i in range(1,1001):
#     # print('current number to be added', i)
#     result = result + i
#     # print('New result after this iteration:', result)

# # print('The final result:', result)


# for i in range (1,1001):
#     if i % 2 == 1:
#         result = result + i
# print( 'The sum of the odd numbers is:', result)


# result = 0

# for i in range ( 1, 1000, 2):
#     result = result + i 

# print(result)

# result = 1

# for i in range(1, 11):
#     result = result * i
# print (result)

# import time

# def countdown(n):
#     while n > 0:
#         print (n)
#         time.sleep(1)
#         n = n-1
#     print ('Blastoff')

# countdown(5)

# counter = 0

# while counter < 10:
#     print (r"Here's Johnny!")
#     counter += 1

# message = 'Jonathan'
# for letter in message:
#     print(letter)

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)

print('Done')
