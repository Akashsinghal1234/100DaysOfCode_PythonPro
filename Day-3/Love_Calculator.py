print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
true = 0
love = 0
new_name1 = name1.lower()
new_name2 = name2.lower() #lower() function is being used to convert a peice of string all in lower case .
true = true + new_name1.count("t") + new_name2.count("t") + new_name1.count("r") + new_name2.count("r") + new_name1.count("u") + new_name2.count("u") + new_name1.count("e") + new_name2.count("e")
love = love + new_name1.count("l") + new_name2.count("l") + new_name1.count("o") + new_name2.count("o") + new_name1.count("v") + new_name2.count("v") + new_name1.count("e") + new_name2.count("e")
love_score = int(str(true) + str(love))
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")