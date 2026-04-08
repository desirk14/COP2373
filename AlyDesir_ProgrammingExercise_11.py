import random


# Deck object
class Deck:
    def __init__(self, size):
        # Create the list of cards as numbers
        self.card_list = [i for i in range(size)]
        # Shuffle the deck
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    def deal(self):
        # Reshuffles the deck automatically if all cards are dealt
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print('Reshuffling...!!!')
            # Deals the next card and moves the index forward
        self.current_card += 1

        return self.card_list[self.current_card - 1]
    # Function to deal the initial poker hand


def deal_hand(deck):
    # Create an empty list for the cards
    hand = []
    # Deals 5 cards for the poker hand
    for i in range(5):
        card_num = deck.deal()
        hand.append(card_num)
    return hand


# Function that prints the hand for the user
def show_hand(hand, ranks, suits):
    # Go through each card number
    for c in range(len(hand)):
        # Find the rank and suit of the cards
        r = hand[c] % 13

        s = hand[c] // 13

        print(c + 1, ranks[r], 'of', suits[s])


# Function that replaces selected cards
def draw_new_cards(deck, hand, indices):
    for i in indices:
        if 1 <= i <= 5:
            # Replace the card with a new one
            hand[i - 1] = deck.deal()

    return hand


# Function for the main game
def poker_draw_game():
    # Establish the ranks and suits for the cards
    ranks = ['2', '3', '4', '5', '6', '7', '8',

             '9', '10', 'J', 'Q', 'K', 'A']

    suits = ['clubs', 'diamonds', 'hearts', 'spades']

    # Create and shuffle the deck
    my_deck = Deck(52)

    print('Your initial poker hand:')

    # Deal the user their 5 cards and show their hand
    hand = deal_hand(my_deck)

    show_hand(hand, ranks, suits)

    # Ask user which cards to replace
    user_input = input(
        '\nEnter the numbers of the cards you want to replace (e.g. 1 3 5), or press Enter to keep all: ')

    if user_input.strip() != '':
        indices = [int(x) for x in user_input.split()]

        # Replace selected cards
        hand = draw_new_cards(my_deck, hand, indices)

    print('\nYour final poker hand:')

    show_hand(hand, ranks, suits)


# Start the game
if __name__ == '__main__':
    poker_draw_game()