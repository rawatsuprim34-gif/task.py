# 1. Write a program that prompts the user to input a series of numbers until they 
# input a duplicate number. Use a while loop to check for duplicates. 

# numbers = []

# while True:
#     num = int(input("Enter a number: "))

#     if num in numbers:
#         print("Duplicate number entered:", num)
#         break

#     numbers.append(num)


# 2. Write a program that prompts the user to enter a positive integer. It then 
# calculates and prints the factorial of that number using a while loop. 

# num = int(input("Enter a positive integer: "))

# factorial = 1
# i = 1

# while i <= num:
#     factorial = factorial * i
#     i += 1

# print("Factorial of", num, "is", factorial)

# 3.  Write a program that accepts a number from the user and calculates the sum of 
# all numbers from 1 up to that number.

# num = int(input("Enter a number: "))

# total = 0
# i = 1

# while i <= num:
#     total = total + i
#     i += 1

# print("Sum of numbers from 1 to", num, "is", total)

# 4. Given a list of numbers, use a loop to count how many times a specific number for 
# example 10 appears. 

# numbers = [10, 5, 10, 8, 3, 10, 7]
# target = 10
# count = 0
# i = 0

# while i < len(numbers):
#     if numbers[i] == target:
#         count += 1
#     i += 1

# print(target, "appears", count, "times.")

# 5. Write a program that counts the total number of vowels and consonants in a given 
# sentence, ignoring spaces and special characters. 

# sentence = input("Enter a sentence: ")

# vowels = 0
# consonants = 0

# for ch in sentence.lower():
#     if ch.isalpha():  # Check if character is a letter
#         if ch in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)

# 6. Write a program to count the total number of digits in a given integer.
# num = int(input("Enter an integer: "))

# count = 0

# while num != 0:
#     num = num // 10
#     count += 1

# print("Total digits:", count)
# 7. Generate a sequence until it reaches 1. If you start with any positive integer n, and 
# if n is even, divide it by 2; if n is odd, multiply it by 3 and add 1. Repeat the process. 
# The sequence will always eventually reach 1. Write a program to print this 
# sequence for a given number. 
# given input: n = 6 
# expected output: 6, 3, 10, 5, 16, 8, 4, 2, 1 
# n = int(input("Enter a positive integer: "))

# while n != 1:
#     print(n, end=", ")

#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = 3 * n + 1

# print(1)

# 8. Print alphabet Series from A–Z 
# i = 65

# while i <= 90:
#     print(chr(i), end=" ")
#     i += 1
# 9. Write a program that prompts the user for a starting integer and an ending integer. 
# Use a while loop to print all numbers between them, inclusive.
# start = int(input("Enter the starting integer: "))
# end = int(input("Enter the ending integer: "))

# while start <= end:
#     print(start, end=" ")
#     start += 1     
# 10. Write a program that prints all odd numbers between 1 and 50 in descending 
# order from 49 down to 1 using a while loop.

# i = 49
# while i >= 1:
#     print(i, end=" ")
#     i -= 2

# 11. Write a program that prints all multiples of 7 between 1 and 100.
# i = 7
# while i <= 100: 
#     print(i, end=" ")
#     i += 7          

# 13. Write a program that asks a user to enter their age. If the input is less than 0 or 
# greater than 120, print invalid age and prompt them again. The loop should 
# repeat until a valid age is provided. 
# while True:     
#     age = int(input("Enter your age: "))

#     if 0 <= age <= 120:
#         print("Valid age entered:", age)
#         break
#     else:
#         print("Invalid age. Please try again.")
# 14. Write a program that allows a teacher to input student scores one by one. The loop 
# ends when the teacher types -1. The program should then calculate and display 
# the average score.
# total = 0
# count = 0

# while True:
#     score = int(input("Enter a student score (or -1 to finish): "))
    
#     if score == -1:
#         break
    
#     total += score
#     count += 1

# if count > 0:
#     average = total / count
#     print("Average score:", average)
# else:
#     print("No scores entered.")

# 15. Write a program that simulates a login screen. Give the user a maximum of 3 
# attempts to type the correct password for example secret123. If they fail 3 times, 
# print access denied, if they succeed early, print access granted and exit the loop.
# correct_password = "secret123"    
# attempts = 0

# while attempts < 3:
#     password = input("Enter the password: ")
#     if password == correct_password:
#         print("Access granted.")
#         break
#     else:
#         print("Invalid password.")
#         attempts += 1
# else:
#     print("Access denied.")
# 16. Write a program that takes an integer input and constructs a new integer that is 
# the exact reverse of the input for example input is 582 outputs the actual integer 
# 285
# n = int(input("Enter an integer: "))
# reversed_num = 0
# while n != 0:
#     digit = n % 10
#     reversed_num = reversed_num * 10 + digit
#     n = n // 10
# print("Reversed integer:", reversed_num)

# 17. Write a program that uses a while loop to print the first n terms of the Fibonacci 
# sequence 0, 1, 1, 2, 3, 5, 8 where n is provided by the user.
# n = int(input("Enter the number of terms: "))
# a, b = 0, 1
# count = 0
# while count < n:
#     print(a, end=" ")
#     a, b = b, a + b
#     count += 1

# 18. Write a program that loops through a string using a while loop and prints a new 
# version of the string with all the vowels removed.

# input_string = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# result_string = ""
# i = 0
# while i < len(input_string):
#     if input_string[i] not in vowels:
#         result_string += input_string[i]
#     i += 1
# print("String with vowels removed:", result_string)

# 19. Write a program that scans a string using a while loop index to count how many 
# times the specific two-character substring hi appears. 


# input_string = input("Enter a string: ")
# substring = "hi"
# count = 0
# i = 0
# while i < len(input_string) - 1:
#     if input_string[i:i+2] == substring:
#         count += 1
#     i += 1
# print("Number of occurrences of 'hi':", count)

# 20. Write a program to find and print all numbers in the list that are multiples of 5. 
# numbers = [12, 25, 7, 30, 18, 40, 55, 9] 
# i = 0
# while i < len(numbers):
#     if numbers[i] % 5 == 0:
#         print(numbers[i])
#     i += 1

# 21. Write a program that processes a string character by character using a while loop, 
# converting all lowercase letters to uppercase and vice versa.
# input_string = input("Enter a string: ")
# result_string = ""
# i = 0
# while i < len(input_string):
#     if input_string[i].islower():
#         result_string += input_string[i].upper()
#     else:
#         result_string += input_string[i].lower()
#     i += 1
# print("String with cases swapped:", result_string)


# 22. For every single increment of the outer loop i, how many times does the inner loop j run?
# i= 1
# while i <= 2:
# j = 1
# while j <= 2:
# print(f'({i}, {j})', end=' ')
# j += 1
# i += 1


# i = 1
# while i <= 2:
#     j = 1
#     while j <= 2:
#         print(f'({i}, {j})', end=' ')
#         j += 1
#     i += 1


# 23. Why does this code print only two stars instead of six? What mistake was made
# with variable j?
# i = 1
# j= 1
# while i <= 3:
# while j <= 2:
# print('*', end='')
# j += 1
# i += 1

# i = 1
# j = 1

# while i <= 3:
#     while j <= 2:
#         print('*', end='')
#         j += 1
#     i += 1

# 24. Which is the first integer whose square is strictly greater than 20?
# found = False

# X = 1
# while not found:
# if x * x > 20:
# found = True
# else:

# x += 1
# print(x)

# found = False

# x = 1
# while not found:
#     if x * x > 20:
#         found = True
#     else:
#         x += 1

# print(x)


# 25. If the user inputs 4, 7, -1, and 10 in sequence, is the -1 added to the total? What is 
# the final printed total?
# total = 0
# user_input = 0
# while user_input != -1:
# total += user_input
# user_input = int(input('enter: '))
# print(total)


# total = 0
# user_input = 0

# while user_input != -1:
#     total += user_input
#     user_input = int(input('enter: '))

# print(total)

# 26. How many times does the word loop print? What is the final value of x?
# x = 10
# while x < 5:
# x += 1
# print('loop')
# print(x)

# x = 10

# while x < 5:
#     x += 1
#     print('loop')

# print(x)

# 27. In many languages, an integer can act as a Boolean expression. At what point does
# x evaluate to False?
# x = 3
# while x:
# print(x, end=' ')
# -= 1

# x

# x = 3

# while x:
#     print(x, end=' ')
#     x -= 1

# print(x)

# 28. What famous mathematical number sequence is generated by this loop's variable
# updating logic?
# a, b = 0, 1
# while a < 10:
# print(a, end=' ' )
# a, b = b, a + b


# a, b = 0, 1

# while a < 10:
#     print(a, end=' ')
#     a, b = b, a + b

# 29. Write a Python function that accepts a string and counts the number of upper and
# lower case letters.
# sample string : 'The quick Brow Fox'
# expected output :
# No. of upper case characters : 3
# No. of lower case characters : 12 

# def count_case(s):
#     upper = 0
#     lower = 0

#     for ch in s:
#         if ch.isupper():
#             upper += 1
#         elif ch.islower():
#             lower += 1

#     print("No. of upper case characters :", upper)
#     print("No. of lower case characters :", lower)

# # Sample string
# count_case("The quick Brow Fox")

# 30. Write a program that displays the following menu repeatedly until the user 
# chooses to exit: 
# 1. Add two numbers 
# 2. Subtract two numbers 
# 3. Multiply two numbers 
# 4. Exit

# while True:
#     print("\nMenu")
#     print("1. Add two numbers")
#     print("2. Subtract two numbers")
#     print("3. Multiply two numbers")
#     print("4. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 4:
#         print("Exiting program...")
#         break

#     elif choice in (1, 2, 3):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == 1:
#             print("Result =", num1 + num2)

#         elif choice == 2:
#             print("Result =", num1 - num2)

#         elif choice == 3:
#             print("Result =", num1 * num2)

#     else:
#         print("Invalid choice. Please try again.")

# 31. Write a program that repeatedly asks the user to enter numbers until they enter 
# 0. Count how many positive and negative numbers were entered exclude 0. 
# while True:
#     print("\nMenu")
#     print("1. Add two numbers")
#     print("2. Subtract two numbers")
#     print("3. Multiply two numbers")
#     print("4. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 4:
#         print("Exiting program...")
#         break

#     elif choice in (1, 2, 3):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == 1:
#             print("Result =", num1 + num2)

#         elif choice == 2:
#             print("Result =", num1 - num2)

#         elif choice == 3:
#             print("Result =", num1 * num2)

#     else:
#         print("Invalid choice. Please try again.")


# 32. Print all prime numbers between start and end using while loops

# start = int(input('Enter start: '))
# end = int(input('Enter end: '))

# num = start
# while num <= end:
#     if num > 1:
#         i = 2
#         is_prime = True
#         while i < num:
#             if num % i == 0:
#                 is_prime = False
#                 break
#             i += 1
#         if is_prime:
#             print(num, end=' ')
#     num += 1


# # 33. Find numbers below 20 in the list

# numbers = [12, 40, 21, 31, 10, 7, 5]

# i = 0
# while i < len(numbers):
#     if numbers[i] < 20:
#         print(numbers[i], end=' ')
#     i += 1


# # 34. Replace all numbers greater than 50 with 0

# numbers = [45, 60, 12, 75, 30, 55, 8, 90]

# i = 0
# while i < len(numbers):
#     if numbers[i] > 50:
#         numbers[i] = 0
#     i += 1

# print(numbers)


# # 35. Count numbers divisible by both 3 and 5

# numbers = [15, 25, 30, 45, 60, 12, 90, 7]

# count = 0
# i = 0

# while i < len(numbers):
#     if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
#         count += 1
#     i += 1

# print('Count =', count)


# # 36. Check whether list is sorted in ascending order

# numbers = [10, 15, 25, 30, 45]

# i = 0
# sorted_list = True

# while i < len(numbers) - 1:
#     if numbers[i] > numbers[i + 1]:
#         sorted_list = False
#         break
#     i += 1

# if sorted_list:
#     print('Sorted')
# else:
#     print('Not Sorted')


# # 37. Print alphabet series a to z

# ch = ord('a')

# while ch <= ord('z'):
#     print(chr(ch), end=' ')
#     ch += 1


# # 38. Print chapter page counts

# pages = [45, 30, 50, 40]

# i = 0
# chapter = 1

# while i < len(pages):
#     print('Chapter', chapter, 'has', pages[i], 'pages')
#     chapter += 1
#     i += 1


# # 39. Find common numbers in two lists

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# i = 0

# while i < len(list1):
#     if list1[i] in list2:
#         print(list1[i], end=' ')
#     i += 1


# # 40. Print multiplication tables of 2, 4, 6, 7, 8

# tables = [2, 4, 6, 7, 8]

# i = 0
# while i < len(tables):
#     j = 1
#     print('\nTable of', tables[i])

#     while j <= 10:
#         print(tables[i], 'x', j, '=', tables[i] * j)
#         j += 1

#     i += 1


# # 41. Check whether list contains duplicates

# numbers = [1, 2, 3, 4, 2]

# i = 0
# duplicate = False

# while i < len(numbers):
#     j = i + 1

#     while j < len(numbers):
#         if numbers[i] == numbers[j]:
#             duplicate = True
#             break
#         j += 1

#     if duplicate:
#         break

#     i += 1

# if duplicate:
#     print('Has Duplicates')
# else:
#     print('No Duplicates')