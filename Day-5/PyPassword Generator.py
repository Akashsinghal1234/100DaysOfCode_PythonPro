import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
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
