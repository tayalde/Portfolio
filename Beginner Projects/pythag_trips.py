import numpy as np

def sides():
	sides = []
	print('Please input your three sides.')
	for i in range(3):
		a = input().strip()
		if a.isnumeric():
			sides.append(a)
	return list(map(int, sides))

def pythag(sides):
	leg_a, leg_b, hypo = sorted(sides)
	left = leg_a ** 2 + leg_b ** 2
	right = hypo ** 2

	if left == right:
		triple = True
	else:
		triple = False
	return triple

def main():
	while True:
		try:
			print(pythag(sides()))
		except KeyboardInterrupt:
			break
	return
	
if __name__ == '__main__':
	main()