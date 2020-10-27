'''
BlackJack game
'''

import random


#global vairables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():

	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank


	def __str__(self):
		return self.rank + ' of ' + self.suit



class Deck:

	def __init__(self):
		self.deck = [] #start with empty list

		for suit in suits:
			for rank in ranks:

				self.deck.append(Card(suit,rank))

	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp += '\n' +card.__str__()
		return 'The deck has:' + deck_comp

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card

#test_deck = Deck()
#test_deck.shuffle()
#print(test_deck)

class Hand:

	def __init__(self):
		# empty list which represtents the cardsyou have
		self.cards = []  
		#both value and aces at 0 for a starting point
		self.value = 0
		#attribute for aces
		self.aces =  0


	def add_card(self,card):

		self.cards.append(card)
		self.value += values[card.rank]


		#keep track of aces
		if card.rank == 'Ace':
			self.aces += 1


	def adjust_for_ace(self):

		# If total value > 21 and still have an ace
		# change ace to a 1 instead of 11
		while self.value > 21 and self.aces: #or **self.aces >  0**
			self.value -= 10
			#if u have more than one ace this is a check
			self.aces -= 1



###TESTing Hand class### 
#test_deck = Deck()
#test_deck.shuffle()

#Player
#test_player = Hand()
#deal 1 card from the deck
#pulled_card = test_deck.deal()
#print(pulled_card)
#test_player.add_card(pulled_card)
#print(test_player.value)


#test_player.add_card(test_deck.deal())
#test_player.value


class Chips:

	def  __init__(self, total=100, ):
		self.total = total
		self.bet = 0
		player_chips = total

	def win_bet(self):
		self.total +=  self.bet


	def lose_bet(self):
		self.total -= self.bet






##below are functions##
def take_bet(chips):
	while True:

		try:
			chips.bet = int(input("How many chips would you like to bet?"))
		except:
			print("Sorry please privide an integer")
		else:
			if chips.bet > chips.total:
				print('Sorry, you do not have enough chips! You have {}'.format(chips.total))
			else:
				break

def hit(deck,hand):

	single_card = deck.deal()
	hand.add_card(single_card)
	hand.adjust_for_ace()



def hit_or_stand(deck,hand):

	#to control an upcoming while loop
	global playing

	while True:
		x = input("Hit  or Stand? Enter 'h' or 's'")

		if x[0].lower() == 'h':
			hit(deck,hand)
		elif x[0].lower() == 's':
			print("Player Stands, Dealer's Turn")
			playing = False
		else:
			print("Sorry i didn't understand that, enter h or s only!")
			continue
		break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)




def player_busts(player, dealer, chips):
	print("Player Bust")
	chips.lose_bet()

def player_wins(player, dealer, chips):
	print("Player Won!")
	chips.win_bet()

def dealer_busts(player, dealer, chips):
	print("Dealer Busts! Player wins")
	chips.win_bet()


def dealer_wins(player, dealer, chips):
	print("Dealer Wins! Player lost")
	chips.lose_bet()

def push(player,dealer):
	print('Dealer and player tie! Push')





##game logic###


while True:

	print("Welcome to BlackJack")

	#create deck and shuffle
	deck = Deck()
	deck.shuffle()


	#created a player hand and they need two cards
	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	

	#created dealer card and they need two cards
	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())


	#setting up players chips
	player_chips = Chips()
	
	take_bet(player_chips)

	#show some cards(but keep one dealer card hidden)
	show_some(player_hand,dealer_hand)


	#using global variable
	while playing:

		#promt  player to hit
		hit_or_stand(deck, player_hand)
		#show cards
		show_some(player_hand,dealer_hand)

		#check if exceed 21
		if player_hand.value > 21:
			player_busts(player_hand,dealer_hand,player_chips)
			break

		#if player didn't bust, play dealer until dealer reaches 17 or busts
	if player_hand.value <= 21:

			#check dealer
		while dealer_hand.value < 17:
			hit(deck,dealer_hand) 

			#show all crads
		show_all(player_hand,dealer_hand)

			#check all scenarios

		if dealer_hand.value > 21:
			dealer_busts(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)

		else:
			push(player_hand,dealer_hand)


	#show total chips amount
	print('\n Player total chips are at: {}'.format(player_chips.total))

	#ask if player wants to play again

	new_game = input("Would you like to play again? Y or N")

	if  new_game[0].upper() =='Y':
		playing = True
		continue
	else:
		print('Thank you for playing!')
		break













