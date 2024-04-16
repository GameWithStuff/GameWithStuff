import time
hr = int(time.strftime("%H"))
if hr >= 20 or hr < 5:
    print("Good Night Sir")
elif hr >= 16:
    print("Good Evening Sir")
elif hr >= 12:
    print("Good Afternoon Sir")
else:
    print("Good Morning Sir")
print("Today is", time.strftime("%B %d, %Y %A"))
print("It's", time.strftime("%H: %M"))
while True:
    pass