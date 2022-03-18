import os
import random

def generate_cards(deck, suit):
    
    for j in suit:
        i = 1
        while i < 14:
            i += 1
            card = {}
            if i == 11:
               card['value'] = str(10)
               card['name'] = 'J'
               card['suit'] = j
            elif i == 12:
                card['value'] = str(10)
                card['name'] = 'Q'
                card['suit'] = j
            elif i == 13:
                card['value'] = str(10)
                card['name'] = 'K'
                card['suit'] = j
            elif i == 13:
                card['value'] = str(10)
                card['name'] = 'K'
                card['suit'] = j
            elif i == 14:
                card['value'] = str(10)
                card['name'] = 'A'
                card['suit'] = j
            else:
                card['value'] = str(i)
                card['name'] = str(i)
                card['suit'] = j
            deck.append(card)

    return deck    
        
            
            
def deal(deck):
    hand = []
    random.shuffle(deck)
    print(str(len(deck)))
    for i in range(2):
        card = deck.pop()
        hand.append(card)
    return hand, deck

def play_again():
    again = ''
    while again != 'y' and again != 'n':
        again = input("Do you want to play again? (Y/N) : ").lower()
        if again == "y":
            game()
        elif again == 'n':
            print( "Bye!")
            exit()

def total(hand):
    total = 0
    for card in hand:
        if card['name'] =='A':
            if total  >= 11:
                total +=1
            else:
                total += 11
        else:
            total = total + int(card['value'])
    return total

def hit(hand, deck):
    card = deck.pop()
    hand.append(card)
    return hand

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')
        
def generate_string(hand, person):
    string = ''
    j = 0
    if person == 'player':
        string = "You had a "
    else:
        string =  "The dealer had  a "

    for i in hand:
        j +=1
        if  j == len(hand):
            string +=  'and a ' + str(i['name']) + ' of ' + str(i['suit'])
        else:
            string += str(i['name']) + ' of ' + str(i['suit']) + ', '
    string += "\nfor a total of " + str(total(hand))
    return string

def print_results(dealer_hand, player_hand):
    clear()
    string = generate_string(dealer_hand, 'dealer')
    print(string)
    string = generate_string(player_hand,'player')
    print(string)

def blackjack(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print( "Congratulations! You got a Blackjack!\n")
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)        
        print( "Sorry, you lose. The dealer got a blackjack.\n")
        play_again()

def score(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print( "Congratulations! You got a Blackjack!\n")
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)        
        print( "Sorry, you lose. The dealer got a blackjack.\n")
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print( "Sorry. You busted. You lose.\n")
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)               
        print( "Dealer busts. You win!\n")
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print( "Sorry. Your score isn't higher than the dealer. You lose.\n")
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)               
        print( "Congratulations. Your score is higher than the dealer. You win\n")        

def game():
    choice = 0
    clear()
    deck = []
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    dealer_hand = []
    player_hand = []
    
    deck = generate_cards(deck, suits)
    
    print( "WELCOME TO BLACKJACK!\n")
    
    dealer_hand, deck = deal(deck)
    player_hand, deck = deal(deck)
    
    while choice != "q":
        string = "The dealer is showing a " + str(dealer_hand[0]['name']) + ' of ' + str(dealer_hand[0]['suit'])
        print (string)
        string = generate_string(player_hand, 'player')
        print(string)
        
        blackjack(dealer_hand, player_hand)
        if total(player_hand) <= 21:
            choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        clear()
        
        if total(player_hand) >= 21  or choice == "s":
            while total(dealer_hand) < 17:
                hit(dealer_hand, deck)
            score(dealer_hand, player_hand)
            play_again()
        elif choice == "h":
            hit(player_hand, deck)
            while total(dealer_hand) < 17:
                hit(dealer_hand, deck)
        elif choice == "q":
            print( "Bye!")
            exit()
    
if __name__ == "__main__":
   game()