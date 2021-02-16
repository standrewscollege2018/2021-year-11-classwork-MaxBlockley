import random
high_score = 1000000

keep_playing = True
while keep_playing == True:
    #set boolean to true
    keep_asking=True
    counter=0

    #Ask them for their number
    G_NUMBER = random.randint(1,100)

    while keep_asking==True:
        #add one to the counter
        counter += 1
        number=int(input("Guess a number between 1 and 100"))

        if number == G_NUMBER :
            keep_asking=False
        else:
            print("wrong number")
            if number > G_NUMBER:
                print("To high")
            elif number < G_NUMBER:
                print("to Low")


    if counter <= high_score :
        print("contgrat you got high score")
        high_score = counter

    print("Congratulations you guessed correct")
    print("you took {} guess".format(counter))
    y_n = input("play again y/n?")

    if y_n == "y":
        keep_playing = True

    else:
        keep_playing = False






