import random

rock = "R"
paper = "P"
scissors = "S"

moves = ["R", "P", "S"]

while True:
    computer = random.choice(moves).upper()
    player = input(" R ,P or, S:  ").upper()

    if player == computer:
        if player == "R".upper() and computer == "R".upper():
            print(f"CPU(Rock), Player(Rock) \n There is a tie")
        elif player == "P".upper() and computer == "P".upper():
            print(f"CPU(Paper), Player(Paper) \n There is a tie")
        elif player == "S".upper() and computer == "S".upper():
            print(f"CPU(Scissors), Player(Scissors) \n There is a tie")
        else:
            print("")
    elif player == "R".upper() and computer == "P".upper():
        print(f"CPU(Paper), Player(Rock)")
        print("CPU", "wins")
        break
    elif player == "P".upper() and computer == "R".upper():
        print(f"CPU(Rock), Player(Paper)")
        print("Player", "wins")
        break
    elif player == "R".upper() and computer == "S".upper():
        print(f"CPU(Scissors), Player(Rock)")
        print("player", "wins")
        break
    elif player == "S".upper() and computer == "R".upper():
        print(f"CPU(Rock), Player(Scissors)")
        print("CPU", "wins")
        break
    elif player == "P".upper() and computer == "S".upper():
        print(f"CPU(Scissors), Player(Paper)")
        print("CPU", "wins")
        break
    elif player == "S".upper() and computer == "P".upper():
        print(f"CPU(Paper), Player(Scissors)")
        print("Player", "wins")
        break
    else:
        print("Not amongst our options \nEnter your option again")