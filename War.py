'''
This file will contain the card class. 
representing all possiple card and 
storing a dictionary
'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card():

	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.values = values[rank]

	def __str__(self):
		return self.rank + ' of ' + self.suit


   

class Deck():

	def __init__(self):
		self.all_cards = []

		for suit in suits:
			for rank in ranks:
				#create  the card  object
				created_card = Card(suit,rank)

				#assumes the card class has been defined already
				self.all_cards.append(created_card)


	def shuffle(self):

		random.shuffle(self.all_cards)


	def deal_one(self):
		return self.all_cards.pop()


#new_deck = Deck()
#new_deck.shuffle()
#mycard  = new_deck.deal_one()

#print(len(new_deck.all_cards))

class Player:

	def __init__(self,name):

		self.name = name
		self.all_cards = []

	def remove_one(self):
		#need to pop at the top of list so that's why it is pop(0)
		return self.all_cards.pop(0)

	def add_cards(self, new_cards):
		if type(new_cards) == type([]):
			#list of multiple card objects
			self.all_cards.extend(new_cards)
		else:
			#a single card object
			self.all_cards.append(new_cards)

	def __str__(self):
		return f'Player {self.name} has {len(self.all_cards)} cards'


#new_player = Player("Branden")
#print(new_player)

#new_player.add_cards([mycard,mycard,mycard,mycard,mycard,mycard])
#print(new_player)

#new_player.remove_one()
#new_player.remove_one()
#print(new_player)


'''
Game setup logic
'''

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()
for x in range(26):
	player_one.add_cards(new_deck.deal_one())
	player_two.add_cards(new_deck.deal_one())


game_on = True

round_num = 0
#while game_on
while game_on:
	round_num += 1
	print(f"Round {round_num}")


	#check to see if player 1 is out of cards
	if len(player_one.all_cards) == 0:
		print('Player One, out of cards! Player Two Wins!')
		game_on = False
		break


	#check to see if player 2 is out of cards
	if len(player_two.all_cards) == 0:
		print('Player Two, out of cards! Player One Wins!')
		game_on = False
		break

	#starting new  round grabbing one card each
	player_one_cards = []
	player_one_cards.append(player_one.remove_one())

	player_two_cards = []
	player_two_cards.append(player_two.remove_one())




	at_war = True
	#while at_war
	while at_war:


		#if players go to war this compares the last drawn card
		#this check is if player1 had greater card
		if player_one_cards[-1].values > player_two_cards[-1].values:

			#player1 gets their cards back and player2 cards
			player_one.add_cards(player_one_cards)
			player_one.add_cards(player_two_cards)

			at_war = False

		#this check is for if player2 had greater card
		elif player_one_cards[-1].values < player_two_cards[-1].values:

			#player2 gets their cards back and player1 cards
			player_two.add_cards(player_one_cards)
			player_two.add_cards(player_two_cards)

			at_war = False


		else:
			print('WAR!')

			#check to make sure player 1 has enough cards
			if len(player_one.all_cards) < 5:
				print("Not enough Cards! Player1 lost")
				print("Player2 wins!")
				game_on = False
				break

			#check to make sure player 2 has enough cards
			elif len(player_two.all_cards) < 5:
				print("Not enough Cards! Player2 lost")
				print("Player1 wins!")
				game_on = False
				break
		
			else:
				for num in range(5):
					player_one_cards.append(player_one.remove_one())
					player_two_cards.append(player_two.remove_one())






