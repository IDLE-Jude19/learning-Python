#--------------------------------------------------------------
# a list with dictionaries? What?

# student = [
#     {"Name": "Jude", "Id": "12432", 
#      "Address": "Gk Rotary Tambulilid, Ormoc City"},
#     {"Name": "Joel", "Id": "00736", 
#      "Address": "Can-Untog, Ormoc City"},
#     {"Name": "Elvira", "Id": "16254", 
#      "Address": "San Juan, Ormoc City"}
# ]
# print("Records:\n")

# for student_records in student:
#     print(f'Name: {student_records["Name"]}\nID: {student_records["Id"]}\nAddress: {student_records["Address"]}\n')
    
#--------------------------------------------------------------
# printing values from the dictionary both the keys and the value
# without inputting without using for loop

# global_dict = {
#     "Name": "Jude", 
#     "Mobile": "09772723615",
#     "Address": "Santo Nino" 
# }


# print(list(global_dict.keys())[0], global_dict["Name"], sep=": ")
# print(list(global_dict.keys())[1],global_dict["Mobile"], sep=": ")
# print(list(global_dict.keys())[2],global_dict["Address"], sep=": ")


#--------------------------------------------------------------
# Create Read using dictionary 

# Refined by chat gpt need further understanding on this code

employee_records = []

def add_employee():
    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    role = input("Enter Employee Role: ")

    employee = {
        "Name": name,
        "Age": age,
        "Role": role
    }
    employee_records.append(employee)
    print("Employee successfully added!\n")

def view_employees():
    if not employee_records:
        print("No employee records found.\n")
        return

    print("\n--- Employee Records ---")
    for i, emp in enumerate(employee_records, start=1):
        print(f"{i}. Name: {emp['Name']}, Age: {emp['Age']}, Role: {emp['Role']}")
    print()

def main():
    while True:
        print("Jude's Tech Company")
        print("1. Add Employee to record")
        print("2. View Employee records")
        print("0. Exit")

        try:
            choice = int(input("Enter selected option: "))
        except ValueError:
            print("Invalid input! Please enter a number.\n")
            continue

        match choice:
            case 1:
                add_employee()
            case 2:
                view_employees()
            case 0:
                print("Exiting program. Goodbye!")
                break
            case _:
                print("Invalid option! Please choose again.\n")

main()

#--------------------------------------------------------------
