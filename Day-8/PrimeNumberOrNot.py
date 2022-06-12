def prime_checker(number):
    end = round(number / 2)
    while end > 1:
        if number % end == 0:
            return print("Not Prime")
        end -= 1
    return print("Prime")


number = int(input("Enter a number to check if it is prime or not : "))
prime_checker(number)
