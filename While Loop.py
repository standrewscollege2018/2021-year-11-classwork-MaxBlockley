#set boolean to True
keep_asking=True

#Start aking f what their name is
while keep_asking== True:
    name=input("Enter your name")
    if name=="Max"or name== "max":
        keep_asking=False
    else:
        print("Wrong Name")


#Loop is now finished print Max
print("Hi Max")