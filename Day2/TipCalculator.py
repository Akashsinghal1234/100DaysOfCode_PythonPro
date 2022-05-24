print("Welcome to the tip calculator !")
bill = int(input("What the amount of your total bill : $ "))
tip = (int(input("Enter the percentage of tip you want to give : ")) * bill) / 100
people = int(input("Enter the number of people you want to split bill into : "))
amount = round((tip + bill) / people, 2)
print(amount)



