from collections import deque
from random import shuffle
from app.card import Card

suits = ['Spade', 'Club', 'Heart', 'Diamond']
values = ['2', '3', '4', '5', '6', '7', '8',
		  '9', '10', 'J', 'Q', 'K', 'A']

class Hand(deque):
	def __init__(self, maxlen):
		super().__init__(maxlen=maxlen)

	def __repr__(self):
		return str([card for card in self])

	def draw(self, deck):
		try:
			if len(self) > self.maxlen:
				raise IndexError
			else:
				self.append(deck.pop())
		except IndexError:
			print('too many cards')
			pass

	def empty(self, deck):
		try:
			for i in range(len(self)):
				deck.burn.append(self.pop())
		except IndexError:
			pass


class Deck(deque):
	def __init__(self):
		super().__init__([Card(x, y) for x in values for y in suits], maxlen=52)
		shuffle(self)
		self.burn = []
		self.pot = 0
		self.cur_bet = 0

	def __repr__(self):
		return '<Deck: {}>'.format(len(self))

	def burn_card(self):
		self.burn.append(self.pop())

	def reset(self):
		try:
			for i in range(len(self.burn)):
				self.append(self.burn.pop())
		except IndexError:
			pass
		shuffle(self)

	def update_bet(self, amt):
		self.cur_bet = amt

	def clear_bet(self):
		self.cur_bet = 0
