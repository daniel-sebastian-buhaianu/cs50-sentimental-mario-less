from cs50 import get_int

# Ask user for positive integer in range (1-8)
height = -1
while True:
	height = get_int("Height: ")
	if height > 0 and height < 9:
		break;

# Print a half pyramid of specified height
i = 0
while i < height:
	j = 0
	while j < height:
		if j >= height - i - 1:
			print("#", end="")
		else:
			print(" ", end="")
		j += 1
	print()
	i += 1
