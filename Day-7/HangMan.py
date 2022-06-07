import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
words = ["celeso", "setenota", "onemandband"]
word = random.choice(words)
print(word)
ans = []
ok = True
for i in range(len(word)):
    ans.append("_")
while "_" in ans:
    choice = input("Enter a char: ").lower()
    for i in range(len(word)):
        if word[i] == choice:
            ans[i] = choice
            ok = False
    if ok:
        ok = True
        lives -= 1
    print(stages[lives])
    print(ans)
print("GAME OVER")