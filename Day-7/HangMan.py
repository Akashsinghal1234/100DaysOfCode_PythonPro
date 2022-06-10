import random
import HangMan_Stages
import HangMan_Words
lives = 6
word = random.choice(HangMan_Words.words)
print(word)
ans = []
ok = True
for i in range(len(word)):
    ans.append("_")
while "_" in ans:
    ok = True
    choice = input("Enter a char: ").lower()
    for i in range(len(word)):
        if word[i] == choice:
            ans[i] = choice
            ok = False
    if ok:
        ok = True
        lives -= 1
    print(HangMan_Stages.stages[lives])
    if lives == 0:
        break
    print(ans)
print("GAME OVER")