bid = {}


# function to do bidding
def bidding():
    name = input("Enter the name : ")
    price = int(input("Enter the bid : "))
    bid[name] = price


print("Welcome to Vardaan's Secret Auction Bidding !")
bidding()
moreBid = input("Are there any other bidders ? Type 'yes' or 'no' ").lower()
while moreBid == "yes":
    bidding()
    moreBid = input("Are there any other bidders ? Type 'yes' or 'no' ").lower()
maxi = 0
player = ""
for winner in bid:
    if maxi < bid[winner]:
        maxi = bid[winner]
        player = winner
print(f"The winner is {player} with a bid of ${maxi}")
