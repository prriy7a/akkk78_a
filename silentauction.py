import os
def findwinner(bidder_details):
    highestbid=0
    winner=""
    for bidder in bidder_details:
        biddingprice=bidder_details[bidder]
        if biddingprice>highestbid:
            highestbid=biddingprice
            winner=bidder
    print(f"The bidders details are:{bidder}")
    print(f"The winner is {winner} with a bid amount of {highestbid}")
bidder_data={}
endofbid=False
while not endofbid:
    name=input("What is your name?:")
    price=int(input("What is your bid?:"))
    bidder_data[name]=price
    morebid=input("Are there more bidders?Type 'yes' or 'no'").lower()
    if morebid=="no":
        endofbid=True
        findwinner(bidder_data)
    elif morebid=="yes":
        os.system('cls')#it will clear the screen