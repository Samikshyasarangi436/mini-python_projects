import random
while True:
    print("1.Roll the dice\n")
    print("2.exit")
    user_input = int(input("Enter the number for your choice:\n"))
    if user_input == 1:
        number = random.randint(1, 6)
        print(number)
    else:
        break