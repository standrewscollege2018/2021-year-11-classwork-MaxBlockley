# This program will tell the user how much miligrams of parcetamol they need.

# Get the users Details
age = int(input("What is the patients age?"))


if age <= 11:
    weight = int(input("What is the paiients weight kg ?"))
    print("recomended dose is", weight * 10, "mg paracetamol")


else:
    age <= 12
    print("2x 500mg")