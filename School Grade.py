#This Program will tell the user what grade it got if it got a cretin Mark
#check if the mark is between 0 and 100
print("Welcome to my grade giving program")

mark = int(input("Enter your mark"))
if mark >=0 and mark <=100:
    if mark >= 90:
        print("A")
    elif mark >= 70:
        print("B")
    elif mark >= 50:
        print("C")
    else:
        print("Fail")
else:
    print("Invalid mark")