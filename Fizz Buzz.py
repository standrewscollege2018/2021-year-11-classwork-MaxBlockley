fizz=int(input("Enter the number you want to be Fizz"))
buzz=int(input("Enter the number you want to be Buzz"))
for num in range(1,20):
    if num % fizz==0 and num % buzz==0:
        print("fizz buzz")

    elif num % fizz ==0:
        print("fizz")

    elif num % buzz ==0:
        print("buzz")

    else:
        print(num)



