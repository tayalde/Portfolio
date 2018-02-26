from app.hand import Hand, Deck

class Player(object):
	def __init__(self, id, nick, hand, money):
		self.id = id
		self.nick = nick
		self.hand = hand
		self.money = money

	def __repr__(self):
		return '<Player: {}-{}>'.format(self.id, self.nick)

	def bet(self, amt, deck):
		self.money -= amt
		deck.pot += amt

	def check(self):
		pass

	def fold(self, deck):
		self.hand.empty(deck)
