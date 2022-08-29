points = 0
answer = input("Who won the 2021-2022 NBA Championship?")
if answer == "Warriors":
    print("Correct answer!")
    points += 1
else: 
    print("incorrect answer")
    
answer = input("Which NBA franchise has the most MVP winners?")
if answer == "Celtics":
    print("Correct answer!")
    points += 1
else: 
    print("incorrect answer")
    
answer = input("Who won the 2021-2022 NBA MVP?")
if answer == "Nikola Jokic":
    print("Correct answer!")
    points += 1
else: 
    print("incorrect answer")

answer = input("Which NBA team(s) has the most rings?")
if answer == "Celtics":
    print("Correct answer!")
    points += 1
else: 
    print("incorrect answer")

print("You got:", (points/4)*100, "%")