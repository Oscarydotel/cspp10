d ={
    
}
choice = str(input("Add\nRemove Key\nRemove Value\nUpdate\nExit\nUser Input:")).lower()

if choice == "add":
    Key = str(input("Enter a Key:"))
    Value_Key = str(input("Enter a Value:"))
    #d[input("Enter a Key:")] = input("Enter a value for a key:")
    if Key in d:
        print("Tr again. Your inputed -Key- is already in d")
        Key = str(input("Enter another Key:"))
        Value_Key = str(input("Enter another Value:"))
    