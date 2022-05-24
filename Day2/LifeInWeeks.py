age = input("What is your current age? \n")

days = (90 - int(age)) * 365
weeks = int(days / 7)
months = int(weeks / 4)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")