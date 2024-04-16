amount = 0
Qs = [
    "Which of these Pokemon was NOT a starter option in any generation (as of Gen 9)?",
    "What was the first generation to introduce held items for Pokemon to use during battle?",
    "In Pokemon Red and Blue, which of these was NOT a mandatory move HM (Hidden Machine) used to navigate the world?",
    "What legendary Pokemon trio was the mascots for Pokemon Ruby, Sapphire, and Emerald?",
    "Which generation introduced the concept of Mega Evolution for certain Pokemon?",
    "What was the name of the first region players explored in the Pokemon main series games?",
    "Which of these Pokemon is NOT obtainable through normal gameplay in Pokemon Gold, Silver, and Crystal?",
    "The introduction of dual-type Pokemon happened in which generation?",
    "What was the first Pokemon game released for the Nintendo 3DS console?",
    "Which of these is NOT a regional variant introduced in Pokemon Sun and Moon?",
    "The ability to nickname your Pokemon was introduced in which generation?",
    "What was the first Pokemon game to feature a complete day-night cycle affecting the world and Pokemon encounters?",
    "Which generation introduced the concept of regional Pokemon forms, with slight variations on existing Pokemon?",
    "What is the name of the evil team players encounter in Pokemon Black & White?",
    "Which generation marked the debut of introducing a new type - the Fairy-type?",
]
ansList = [
    ["Bulbasaur", "Fennekin", "Ditto", "Mudkip"],
    ["Generation I", "Generation II", "Generation III", "Generation IV"],
    ["Surf", "Cut", "Fly", "Strength"],
    [
        "Articuno, Zapdos, Moltres",
        "Groudon, Kyogre, Rayquaza",
        "Regirock, Regice, Registeel",
        "Suicune, Raikou, Entei",
    ],
    ["Generation V", "Generation VI", "Generation VII", "Generation VIII"],
    ["Kanto", "Johto", "Hoenn", "Sinnoh"],
    ["Suicune", "Celebi", "Lugia", "Tyranitar"],
    ["Generation I", "Generation II", "Generation III", "Generation IV"],
    [
        "Pokemon X & Y",
        "Pokemon Omega Ruby & Alpha Sapphire",
        "Pokemon Sun & Moon",
        "Pokemon Ultra Sun & Ultra Moon",
    ],
    ["Alolan Raichu", "Alolan Vulpix", "Alolan Exeggutor", "Alolan Ponyta"],
    ["Generation I", "Generation II", "Generation III", "Generation IV"],
    [
        "Pokemon Gold, Silver, and Crystal",
        "Pokemon Ruby, Sapphire, and Emerald",
        "Pokemon Diamond, Pearl, and Platinum",
        "Pokemon Black & White",
    ],
    ["Generation IV", "Generation V", "Generation VI", "Generation VII"],
    ["Team Rocket", "Team Magma", "Team Aqua", "Team Plasma"],
    ["Generation VI", "Generation VII", "Generation VIII", "Generation IX"],
]
corrects = ["3", "2", "3", "2", "2", "1", "2", "1", "1", "4", "1", "1", "4", "4", "1"]
print("Welcome to KBC!!!")
print("You have to answer 15 Questionss in a row to win BIG.")
# Running The loop for the Game
for i in range(15):
    print("You are on question", i + 1)
    print(Qs[i])
    print("And your options are:-")
    picked = 0
    for optn in range(4):
        print(optn+1, ") ", ansList[i][optn], sep="")
    while True:
        picked = input("Please enter the Option picked (1,2,3,4) or enter Q to quit\n")
        if picked == "Q":
            print("You Are Quitting")
        if picked == corrects[i]:
            print("That is the correct answer!!!")
            amount = amount * 2
            if(amount == 0):
                amount = 1000
            print("Your current winning amount is $", amount, sep="")
        if (picked in ["1", "2", "3", "4", "Q"]):
            break
    if picked == "Q":
        break
    elif picked == corrects[i]:
        continue
    else:
        print(
            "Unfortunately, You Picked the wrong answer thus you earnings will be quartered."
        )
        amount = amount / 4
        break
if(amount == 16384000):
    print('You completed this KBC you answered all the Questions right.')
print("You earned the Grand Total of $", amount, sep="")
while True:
    pass
