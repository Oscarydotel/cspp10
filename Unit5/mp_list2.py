#Worked With Cecilia  
number_list = []
user_input = input("Enter\nNumber\nSum\nClear\nPrint\nLenght\nor Exit\nPlease:  ")
print(user_input)
while user_input != "Exit" or user_input != "exit":
    if user_input == "Clear":
        number_list = []
        print(number_list)
    elif user_input == "Print":
        print(number_list)
    elif user_input == "Length":
        print(len(number_list))
    elif user_input == "Sum":
        print(sum(user_input))
    else:
        user_input = int(user_input)
        number_list.append(user_input)


