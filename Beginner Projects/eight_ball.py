from random import randint
from time import sleep

def main():
	responses = [
		"It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
		"You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
		"Yes", "Signs point to yes", "Reply hazy try again", "Ask again later",
		"Better not tell you now", "Cannot predict now", "Concentrate and ask again",
		"Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", 
		"Very"
	]

	q_bool = True
	while True:
		question = input("What question do you desire to know the answer to?\n")
		print("Thinking...\n")
		sleep(randint(0, 5))
		print(responses[randint(0, len(responses))])
		while True:
			try:
				redo = input("Would you like to ask another question? (Y/N)\n")
				if redo.lower() == 'y': 
					q_bool = True
					break
				elif redo.lower() == 'n':
					q_bool = False
					break
				else:
					raise ValueError
			except ValueError:
				pass
		if q_bool == False:
			break
	return

if __name__ == '__main__':
	main()
