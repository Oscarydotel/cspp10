#Worked with Cecilia Gonzalez 
number_list = []
user_input = int(input("Enter a number:  "))
while user_input != 0:
    if user_input  > 0 :
        number_list.append(user_input)
        print(number_list)
        user_input = int(input("Enter another Number: "))
        
    elif user_input < 0:
        user_input = user_input/-1
        if user_input == user_input in number_list:
            number_list.remove(user_input)
            print(number_list)
            user_input = int(input("Enter another Number: "))
        else:
            print("False number")
            user_input = int(input("Enter a correct number Please: "))
    else:
        break