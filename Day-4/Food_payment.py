import random
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
choice = random.randint(0, len(names)-1)
# choice = random.randint(0, 10)
print(f"{names[choice]} is going to pay for food today .")
#vardaan, akash, pratham, rhythm, devansh, tassu


