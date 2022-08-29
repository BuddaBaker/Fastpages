points = 0
answers = input("Who won the 2021-2022 NBA Championship?")
if answer == "Warriors":
    print("Correct answer!")
    points += 1
else: 
    print("incorrect answer")
    
answers = input("Which NBA franchise has the most MVP winners?")
if answer == "Celtics":
    print("Correct answer!")
    points += 1
else: 
    print("incorrect answer")
    
answers = input("Who won the 2021-2022 NBA MVP?")
if answer == "Nikola Jokic":
    print("Correct answer!")
    points += 1
else: 
    print("incorrect answer")

answers = input("Which NBA team(s) has the most rings?")
if answer == "Nikola Jokic":
    print("Correct answer!")
    points += 1
else: 
    print("incorrect answer")

printL("You got:", points/4, "%")