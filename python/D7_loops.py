#--------------------------------------------------------------

# using while loop = printing repeated word

# using "<"

# i = 0

# while i < 5:
#     print("Jude Gwapo")
#     i = i + 1
    
#--------------------------------------------------------------

# using "!="
# i = 5 

# while i != 0:
#     print("Jude Gwapo")
#     i = i - 1

#--------------------------------------------------------------

#--------------------------------------------------------------

# using "<="

# i = 1

# while i <= 5:
#     print("Jude Gwapo")
#     i = i + 1
    
#--------------------------------------------------------------

# For loops = printing repeated words

#using list or array

# for i in [0, 1, 2, 3, 4]:
#     print("Jude gwapo!")
    

#--------------------------------------------------------------

# using range 

# for i in range (5):
#     print("Jude gwapo!")

#--------------------------------------------------------------

# iteration of repeated word without using loop syntaxes "while and for"

# print("Jude gwapo\n" *3 ,end="")

# end = "" is used here to default or cancel out the escape sequece
# "\n" at the last line

#--------------------------------------------------------------

#looping a word using functions and conditionals

# in the main is where we ask user input:("word" and "iteration times")
# then we check if the iteration is not equivalent to 0 or negative
# then outside the while loop we pass the parameters iterate_this and
# iteration as argument to wordlooper. Then in the world looper is where
# iteration of the inputed word will happen.

# def main():
#     iterate_this = input("Give me a word to iterate: ").strip().title()
#     iteration = int(input("How many times will I iterate the word? "))
    
#     while True:
#         if iteration < 1:
#             continue
#         else:
#             break

#     wordlooper(iterate_this, iteration) 
    
    
# def wordlooper(word, times):
#     for _ in range(times):
#         print(word)
        
        
# main() 

#--------------------------------------------------------------
# making a right triangle using for loop

# character_to_iterate = input("Give me any character to be iterated into a right triange:")
# iteration = int(input("Give me a number of lines of the right triangle: "))

# for i in range(1, iteration + 1):
#     print(character_to_iterate * i)

#--------------------------------------------------------------