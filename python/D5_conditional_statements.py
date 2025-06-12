#--------------------------------------------------------------

# odd or even checker

# number = int(input("Enter a number to check if(odd/even): "))

# if number % 2 == 0:
#     print("The number is even.\n")
# else:
#     print("The number is odd.\n")    
    
#--------------------------------------------------------------

# odd or even checker using defined function

# def even_odd_checker(check_n):
#     if check_n % 2 == 0:
#         return True
#     else:
#         return False
    
# def main():
#     number = int(input("Enter a number: "))
    
#     pass_to_checker = even_odd_checker(number)
    
    # You can do "if pass_to_checker == True" "if pass_to_checker== 1" 
    # or even just the variable name because when
    # a variable is equal to one (bool True == 1 and False == 0) 
    # automatically the compiler will assume the value 
    # of the variable is true
    
#     if pass_to_checker:
#         print("Number is even!")
#     else:
#         print("Number is odd!")
    
# main()

#--------------------------------------------------------------

# odd or even checker using defined function shortened return value

# def even_odd_checker(check_n):
#     return True if check_n % 2 == 0 else False
    
# def main():
#     number = int(input("Enter a number: "))
    
#     if even_odd_checker(number):
#         print("Number is even!")
#     else:
#         print("Number is odd!")
    
# main()

#--------------------------------------------------------------

#--------------------------------------------------------------

# odd or even checker using defined function much shorter return value

# def even_odd_checker(check_n):
#     return check_n % 2 == 0 
    
# def main():
#     number = int(input("Enter a number: "))
    
#     if even_odd_checker(number):
#         print("Number is even!")
#     else:
#         print("Number is odd!")
    
# main()

#--------------------------------------------------------------

# Grade checker 

# grade = int(input("Enter Grade(number): "))

# if grade >= 90:
#     print("Grade Equivalent: A\n")
# elif grade >= 81 and grade != 90: 
#     print("Grade Equivalent: B\n")
# elif grade >= 75 and grade != 81:
#     print("Grade Equivalent: C\n")
# else:
#     print("Grade Equivalent: F\n")

#--------------------------------------------------------------

# conditional statement using AND operator
#Vo2max performance checker

# distance = int(input("Enter running distance in 12mins (in meters): "))
# age = int(input("Enter your age: "))
# print("\n")


# Vo2Max = (distance - 504.9)/44.73 # Copper's Vo2Max formula

# Vo2Maxresult = round(Vo2Max) # avoid having a float result

# if age >= 18 and age <= 25:
#     if Vo2Max > 60:
#         print(f"Your Vo2Max is {Vo2Maxresult}")
#         print("Remark: Excellent!\n")
#     elif Vo2Max > 51 and Vo2Max <= 60:
#         print(f"Your Vo2Max is {Vo2Maxresult}")
#         print("Remark: Good!\n")
#     elif Vo2Max > 46 and Vo2Max <= 51:
#         print(f"Your Vo2Max is {Vo2Maxresult}")
#         print("Remark: Above Average!\n")
#     elif Vo2Max > 41 and Vo2Max <= 46:
#         print(f"Your Vo2Max is {Vo2Maxresult}")
#         print("Remark: Average!\n")
#     elif Vo2Max >= 36 and Vo2Max <= 41:
#         print(f"Your Vo2Max is {Vo2Maxresult}")
#         print("Remark: Below Average!\n")
#     else:
#         print(f"Your Vo2Max is {Vo2Maxresult}")
#         print("Remark: Poor!\n")

# remarks are based on this "Vo2Max Remarks" image inside folder

#--------------------------------------------------------------