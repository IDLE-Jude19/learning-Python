# Error Handling Syntaxes are:
#  - try
#  - except
#  - pass
#  - raise
#  - finally

#--------------------------------------------------------------

# error handling incorporating functions that takes a user input 
# and check if it is odd or even

# def main():
    
#     isOdd_Even = int(input("Give me a number to check its parity: "))
#     error_handler(isOdd_Even) # error handling upon user prompt if entered is an integer
    
    
# def error_handler(n):
    
#     while True:
#         try:
#             if n % 1 == 0:
#                 return parity_checker(n)
#         except ValueError:
#                 print("Input an integer!\n")
                   
            
# def parity_checker(parity):
    
#     if parity % 2 == 0:
#         print(f"The number {parity} is Even.\n")
#     else:
#         print(f"The nubmer {parity} is Odd.\n")
        

#--------------------------------------------------------------

# Chat GPT's begginer exercis: Division of two flaoting value with error handling

# while True:
#     try:
#         num1 = float(input("What is the first number? "))
#         if num1 != 0:
#             break
#         else:
#             print("Zero is not accepted!\n")   
#     except ValueError: 
#         print("First input is non-numeric\n")
    

# while True:
#     try:
#         num2 = float(input("What is the second number? "))
#         if num2 != 0:
#             break
#         else:
#             print("Zero is not accepted!\n")
#     except ValueError:
#         print("Second input is non-numeric\n")
    
# result = num1 / num2
# print(f"Result: {result:.2f}\n")

#--------------------------------------------------------------

# Guessing Game activity

# import random

# randomizer = random.randint(1, 10)


# while True:
#         try:    
#             guess = int(input("Guess the number generated between (1-10): "))
#         except ValueError:
#             print("You have inputted a non-integer!\n")
#         else:
#             if guess != randomizer:
#                 if guess < randomizer:
#                     print("Your guess is lower! Try again.\n")
#                 else:
#                     print("Your guess is higher! Try again. \n")
#             else:
#                 print("You have guessed the number. Yehey!\n")
#                 break       
       

#--------------------------------------------------------------

# Error handling using dict instead of match function - Day of the Week Activity

# days_of_the_week = {1: "Sunday", 
#                     2: "Monday",
#                     3: "Tuesday",
#                     4: "Wednesday",
#                     5: "Thursday",
#                     6: "Friday",
#                     7: "Saturday"}

# print("\nLegend:\nSunday = 1\nMonday = 2\nTuesday = 3\nWednesday = 4\nThursday = 5\nFriday = 6\nSaturday = 7\n")

# while True:
#     try:
#         day_num_input = int(input("What is the number of the day in a week: "))
#     except ValueError: 
#         print("Only input an integer assigned based on the Legend!\n")
#     else:
#         if day_num_input == 0:
#             print("Zero is not a valid representation of a day in a week!\n")
#             continue
#         else:
#             break
        
# print(f"Today is {days_of_the_week[day_num_input]}!\n")

#--------------------------------------------------------------


# Division calculator error handling utilizing functions

# def main():
#     while True:
#         try:
#             num1 = float(input("Enter Numerator: "))
#         except ValueError:
#             print("Value Error: Enter an integer!\n")
#         else:
#             if num1 == 0:
#                     print("Zero value is not acceptable! Retry.\n")
#             else:
#                 break
      
#     while True:
#         try:
#             num2 = float(input("Enter Denominator: "))
#         except ValueError:
#             print("Value Error: Enter an integer!\n")
#         else:
#             if num2 == 0:
#                     print("Zero value is not acceptable! Retry.\n")
#             else:
#                 break     
#     operation(num1, num2)    
    
# def operation(numerator, denominator):
    
#     result = numerator / denominator
    
#     if result % 1 == 0:
#         print(f"Result: {int(result)}")
#     else:
#         print(f"Result: {result:.2f}")
        
# main()

#--------------------------------------------------------------- 