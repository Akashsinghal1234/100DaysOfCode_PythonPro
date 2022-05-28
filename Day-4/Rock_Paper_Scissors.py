import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]
human = int(input("Enter your choice, Type 0 for rock, 1 for paper, 2 for scissors : "))
computer = random.randint(0, 2)
if human == 0:
    if computer == 0:
        print(f"You choose:\n{game[human]}\nComputer choose: \n {game[computer]}")
        print("Oops, It's a tie.")
    elif computer == 1:
        print(f"You choose:\n{game[human]}\nComputer choose: \n {game[computer]}")
        print("You Lose.")
    else:
        print(f"You choose:\n{game[human]}\nComputer choose: \n {game[computer]}")
        print("You Win.")
elif human == 1:
    if computer == 1:
        print(f"You choose:\n{game[human]}\nComputer choose: \n {game[computer]}")
        print("Oops, It's a tie.")
    elif computer == 2:
        print(f"You choose:\n{game[human]}\nComputer choose: \n {game[computer]}")
        print("You Lose.")
    else:
        print(f"You choose:\n{game[human]}\nComputer choose: \n {game[computer]}")
        print("You Win.")
else:
    if computer == 2:
        print(f"You choose:\n{game[human]}\nComputer choose: \n {game[computer]}")
        print("Oops, It's a tie.")
    elif computer == 0:
        print(f"You choose:\n{game[human]}\nComputer choose: \n {game[computer]}")
        print("You Lose.")
    else:
        print(f"You choose:\n{game[human]}\nComputer choose: \n {game[computer]}")
        print("You Win.")