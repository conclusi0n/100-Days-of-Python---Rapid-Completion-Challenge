#The Python Dictionary
scores={
    "Biraj":20,
    "lamsal":22,
    "Apple":10
}
print(scores["Biraj"])

for key,value in scores.items():
    print(f"{key}:{value}")

print("///////////////////////////////////////////////////////////////////////////////")
# Nesting Lists and Dictionaries

students = [
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 87},
]
print(students[1]["name"])  # Output: Alice
print(students[1]["score"])
#List Inside a Dictionary:
travel_log = {
    "France": ["Paris", "Lyon", "Nice"],
    "USA": ["New York", "Los Angeles", "Chicago"],
}
print(travel_log["France"])  # Output: ['Paris', 'Lyon', 'Nice']

#Dictionary Inside a Dictionary:
travel_log = {
    "France": {"cities_visited": ["Paris", "Lyon"], "total_visits": 3},
    "USA": {"cities_visited": ["New York", "Chicago"], "total_visits": 2},
}
print(travel_log["France"]["cities_visited"])  # Output: ['Paris', 'Lyon']

print("//////////////////////////////////////////////////////////////////")

# Function to find the highest bidder
def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder, bid_amount in bids.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Main auction logic
print("Welcome to the Secret Auction!")
bids = {}
auction_ongoing = True

while auction_ongoing:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid  # Add the bid to the dictionary
    
    # Ask if there are more bidders
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more_bidders == "no":
        auction_ongoing = False  # End the auction
        find_highest_bidder(bids)  # Determine the winner
