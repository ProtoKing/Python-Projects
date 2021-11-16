from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program")
bid_entry = []
max_bid = {"name":"","bid":0}
other_participants = True

while other_participants:
    name = input("What is your name?: ")
    bid = float(input("What's your bid? $"))

    bid_entry_individual = {"name":name, "bid":bid}
    bid_entry.append(bid_entry_individual)

    bidders = input("Are there any other bidders? Type 'yes' or '' no: ")
    
    if bidders == "no":
        other_participants = False

        for item in bid_entry:
            if item['bid'] > max_bid['bid']:
                max_bid = item
        clear()
        print(f"The winner is {max_bid['name']} with a bid of ${max_bid['bid']}")
       
    elif bidders == "yes":
        other_participants = True
        clear()    

