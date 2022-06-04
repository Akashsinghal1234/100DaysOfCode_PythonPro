import random
letters = [chr(i) for i in range(97,123)]+[chr(i) for i in range(65,91)]
numbers = [str(i) for i in range(0,10)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
characters = int(input("Enter the number of letters that you want in password : "))
digits = int(input("Enter the number of numbers that you want in password : "))
special = int(input("Enter the number of symbols that you want in password : "))
ans = []
for i in range(1, characters+1):
    ans.append(random.choice(letters))
for i in range(1, digits+1):
    ans.append(random.choice(numbers))
for i in range(1, special+1):
    ans.append(random.choice(symbols))


def listToString(s):
    # initialize an empty string
    str1 = ""

    # return string
    return (str1.join(s))


# Driver code
random.shuffle(ans)
print(listToString(ans))
