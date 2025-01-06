import random

# Initialize Deck and Functions
def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]  # 10 for J, Q, K; 11 for Ace
    return random.choice(cards)

# Calculate Hand Value
def calculate_score(hand):
    """Calculates the score of a hand."""
    if sum(hand) == 21 and len(hand) == 2:  # Check for blackjack
        return 0  # Representing Blackjack as 0
    
    if 11 in hand and sum(hand) > 21:  # Adjust Ace value if necessary
        hand.remove(11)
        hand.append(1)
    
    return sum(hand)

# Compare Player and Dealer Scores
def compare(player_score, dealer_score):
    """Compares the player's and dealer's scores to declare a winner."""
    if player_score == dealer_score:
        return "It's a draw!"
    elif dealer_score == 0:
        return "Dealer has Blackjack! You lose."
    elif player_score == 0:
        return "You have Blackjack! You win!"
    elif player_score > 21:
        return "You went over. You lose."
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose."

# Implement Game Logic
def play_blackjack():
    print("Welcome to Blackjack!")
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    
    game_over = False

    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        
        print(f"Your hand: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")
        
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to hit, or 'n' to stand: ").lower()
            if should_continue == "y":
                player_hand.append(deal_card())
            else:
                game_over = True
    
    # Dealer's turn
    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)
    
    print(f"\nYour final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))

# Run the Game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    play_blackjack()
print("Goodbye!")
