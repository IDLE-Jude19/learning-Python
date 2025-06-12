#--------------------------------------------------------------
#iteration of list, turning a string into an integer to be the range 

# friends = ["Jude", "Johanna", "Paul", "Rhianzel"]


# for friend in range(len(friends)):
#     print(friend +1, friends[friend], sep=". ")


#--------------------------------------------------------------

#Chat GPT's given beginner "Grocery list" activity with append and remove

# inputtedgrocery = []

# def userinput():
#     number_of_append_limit = 5
    
#     for _ in range(number_of_append_limit):
#         isulod = input("Input Grocery Item to add to cart: ").strip().title()
#         inputtedgrocery.append(isulod)
        
#         if isulod in inputtedgrocery:
#             print("Item successfully Addded to Cart!")
#         else:
#             print("Item unsuccessfully Added!")
    
#     return main()
    
    
# def printer():
#     print("\nItems added to Cart:\n")
    
#     for i in range(len(inputtedgrocery)):
#         print(i+1,inputtedgrocery[i], sep=". ")
    
#     return main()


# def remover():
#     remove_item = input("\nWhat item will you remove from your cart? ").strip().title()
    
    
#     if remove_item in inputtedgrocery:
#             inputtedgrocery.remove(remove_item)
#             print("Item successfully deleted!")
#     else: 
#             print("Item unsuccessfully deleted!")
    
#     return main()
            
            
# def main():
    
#     print("\nMy Grocery List:")
#     print("1. Add Items\n2. Print Added Items\n3. Delete Added Item\n")
#     slctnum = int(input("Enter selection: "))
    
#     while (slctnum != 0):
#         match slctnum:
#             case 1: userinput()
#             case 2: printer()
#             case 3: remover()
#             case _: print("Invalid Input!"); return main()
            
# main()
    
#--------------------------------------------------------------