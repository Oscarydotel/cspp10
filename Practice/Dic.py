from pprint import pprint
d ={
}
choice = input("Add\nRemove Key\nUpdate\nExit\nUser Input:").lower()

if choice == "add":
    Key = str(input("Enter a Key:"))
    Value_Key = str(input("Enter a Value:"))
    #d[input("Enter a Key:")] = input("Enter a value for a key:")
    if Key in d:
        print("Try again. Your inputed -Key- is already in d")
        Key = str(input("Enter another Key: "))
        Value_Key = str(input("Enter another Value: "))
        pprint(d)
        d[Key] = Value_Key
elif choice == "remove key":
    ask_user_key = input("What -Key- do you want to remove?: ")
    if ask_user_key in d:
        del d[ask_user_key]
    else:
        ask_user_key = input("Try again: ")
elif choice == "update":
    ask_user_key = input("What -Key- do you want to update?: ")
    if ask_user_key in d:
        value = input("What is the value of {} ?: ")
    else:
        ask_user_key = input("Enter another -Key-: ")
elif choice == "exit":
    pprint(d)
    print("---End of Game!--")