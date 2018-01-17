def main():
	bottles_str = "{0} {1} of beer"
	chorus_str = " Take one down, pass it around, "
	for item in range(99, 0, -1):
		if item == 1:
			verse_str = bottles_str.format(item, "bottle")
		else:
			verse_str = bottles_str.format(item, "bottles")

		print("{0} on the wall, {0}. {1} {0} on the wall.\n".format(verse_str,
																    chorus_str))
	return

if __name__ == "__main__":
	main()
