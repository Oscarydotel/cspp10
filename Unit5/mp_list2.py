#Worked With Cecilia  
number_list = []


while True:
    user_input = input("Enter\nNumber\nSum\nClear\nPrint\nLength\nor Exit Please:  ").lower()
    if user_input == "clear":
        number_list = []
        print(number_list)
    elif user_input == "print":
        print(number_list)
    elif user_input == "length":
        print(len(number_list))
    elif user_input == "sum":
        print(sum(number_list))
    else:
        number_list.append(int(user_input))

