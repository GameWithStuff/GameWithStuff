while True:
    import random

    choice = "4"
    while not choice.lower()[0] in "swg":
        choice = input("Enter your choice of Snake water or Gun (S, W, G):\n")
    choice = "swg".find(choice[0].lower())
    comp = random.randint(0, 2)
    swg = ["Snake", "Water", "Gun"]


    def stop():
        while True:
            pass


    def whoWon(choice, comp):
        if choice == comp:
            return "d"
        elif (comp == 2 and choice == 0) or (choice > comp):
            return "c"
        elif (choice == 2 and comp == 0) or (choice < comp):
            return "p"


    won = whoWon(choice, comp)
    match won:
        case "d":
            print(f"It is a draw, we both chose {swg[comp]}")
        case "c":
            print(f"I won as you picked {swg[choice]}, while I picked {swg[comp]}.")
        case "p":
            print(f"I won as you picked {swg[choice]}, while I picked {swg[comp]}.")
    print('Lets play agian \n\n\n\n')
