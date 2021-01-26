from enum import Enum
from enum import IntEnum
from random import *

full_deck = []
partial_deck = []
dealer_cards = []
player_cards = []

#Card enum for playing cards
class Card(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 10
    KING = 10
    ACE = 11

#suit enum for playing cards
class Suit(Enum):
    SPADES = 'spades'
    CLUBS = 'clubs'
    HEARTS = 'hearts'
    DIAMONDS = 'diamonds'

#Class to hold info for playing cards
class PlayingCard:
    def __init__(self, card_vlaue, card_suit):
        self.card = card_vlaue
        self.suit = card_suit

#function to deal full deck of cards
def create_deck():
    for suit in Suit:
        for card in Card:
            full_deck.append(PlayingCard(Card(card), Suit(suit)))
    return full_deck

#Draw single card from deck
def draw_card(deck):
    rand_card = randint(0, len(deck)-1)
    return deck.pop(rand_card)

#deal 2 cards to dealer and player from shuffled deck
def deal_BlackJack():
    while(len(dealer_cards) != 2):
        dealer_cards.append(draw_card(partial_deck))
    while(len(player_cards) != 2):
        player_cards.append(draw_card(partial_deck))


create_deck()
partial_deck = list(full_deck)
deal_BlackJack()

#Shows dealer hand (only one)
print("Dealer has: ? and", dealer_cards[0].suit, dealer_cards[0].card)

#Shows player hand and score   
for i in range(0, len(player_cards)):
    print("Player has: ", player_cards[i].suit, player_cards[i].card)

score1 = player_cards[0].card + player_cards[1].card 
dealer_score = dealer_cards[0].card + dealer_cards[1].card

print("Score: ", score1)

#Hit or stay action of player, and adds score up
while score1 < 21:
    hit_stay = str(input("Do you want to hit or stay? "))
    if hit_stay == "hit":
        player_cards.append(draw_card(partial_deck))
        score1 += player_cards[len(player_cards)-1].card
        for i in range(0, len(player_cards)-1):
            print("You now have: ", player_cards[i].card)
        print("Your score now is: ", score1)
    else:
        print("The dealer has a total of: ", dealer_score)
        print("With the hand: ", dealer_cards[0].suit, dealer_cards[0].card, dealer_cards[1].suit, dealer_cards[1].card)
        if dealer_score >= score1:
            print("Dealer wins!!!")
        else:
            print("Player wins!!")
            break
if score1 > 21:
    print("BUST! Dealer wins!!")
elif score1 == 21 and score1 > dealer_score:
    print("BLACKJACK! you win")
