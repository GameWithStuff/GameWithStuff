totalLength = "w"
while not (totalLength.isnumeric()):
    totalLength = input("Please Enter a number to base the star on\n")
totalLength = int(totalLength) * 2 + 1
totalLength = min(totalLength, 61)
# totalLength = 5
listOfStr = []
char = "*"
for i in range(1, totalLength):
    listOfStr.append(char.center(totalLength * 3, " "))
    char = char + (char[0] * 2)
    print(listOfStr[-1])
listOfStr.reverse()
for i in listOfStr[1:]:
    print(i)
while True:
    pass
