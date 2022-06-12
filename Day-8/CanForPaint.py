import math
print("Welcome to the wall paint services.")
print("- We can paint 5 square meters of your wall with 1 can of paint.")
print("- Price of 1 single paint can is $13.")
height_of_wall = int(input("Enter the height of the wall : "))
width_of_wall = int(input("Enter the width of the wall : "))
total_cans = math.ceil((height_of_wall*width_of_wall)/5)
total_price = total_cans*13
print(f"Total price for painting your walls would cost you about ${total_price}!!")
