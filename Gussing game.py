import random
#set boolean to true
keep_asking=True

#Ask them for their number
G_NUMBER = random.randint(1,10)
while keep_asking==True:
    number=int(input("Guess a number between 1 and 10"))

    if number == G_NUMBER :
        keep_asking=False
    else:
        print("wrong number")
        if number > G_NUMBER:
            print("To high")
        elif number < G_NUMBER:
            print("to Low")

print("That is correct")