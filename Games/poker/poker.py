from app.hand import Hand, Deck
from app.player import Player

deck = Deck()
player_a = Player(1, 'tom1', Hand(maxlen=2), 100)
player_b = Player(2, 'tom2', Hand(maxlen=2), 100)
player_c = Player(3, 'tom3', Hand(maxlen=2), 100)
player_d = Player(4, 'tom4', Hand(maxlen=2), 100)
players = [player_a, player_b, player_c, player_d]

def bet_stage(players, deck):
	for player in players:
		player.bet(10, deck)

def draw_stage(players, deck):
	i = 0
	while i < 2:
		for player in players:
			player.hand.draw(deck)
		print(i)
		i += 1
	bet_stage(players, deck)

def flop_stage(players, deck):
	flop = Hand(maxlen=3)
	deck.burn_card()
	for i in range(3):
		flop.draw(deck)
	bet_stage(players, deck)
	return flop

def turn_stage(players, deck):
	turn = Hand(maxlen=1)
	deck.burn_card()
	turn.draw(deck)
	bet_stage(players, deck)
	return turn

def river_stage(players, deck):
	river = Hand(maxlen=1)
	deck.burn_card()
	river.draw(deck)
	bet_stage(players, deck)
	return river

def reveal_stage(players, deck, flop, turn, river):
	# evaluate hands
	# give pot to winner
	for player in players:
		player.hand.empty(deck)
		if player.money <= 0:
			players.remove(player)
	flop.empty(deck)
	turn.empty(deck)
	river.empty(deck)
	deck.reset()
	print(deck)


def main():
	bet_stage(players, deck)
	draw_stage(players, deck)
	flop = flop_stage(players, deck)
	turn = turn_stage(players, deck)
	river = river_stage(players, deck)
	reveal_stage(players, deck, flop, turn, river)

if __name__ == '__main__':
	while len(players) > 1:
		print(players)
		for player in players:
			print(player.money)
		main()