import random
cpu = random.randint(1,100)
count = 5
while True:
    user = int(input("Enter the number.."))
    if user == cpu:
        print("Congrats you have guessed the correct number..")
        break
    elif user > cpu:
        print("You have guessed the larger number..")
    elif user < cpu:
        print("You have guessed the smaller number..")
    else:
        print("invalid number !!")

    count -= 1
    print("chances left",count)

    if count == 0:
        print("you have lost..",cpu)
        break
    
