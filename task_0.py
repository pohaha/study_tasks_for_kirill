

number_of_stars = 20
is_horizontal = True
screen_output = ""
def main():
	global is_horizontal
	global screen_output
	for i in range(number_of_stars):
		is_horizontal = False
		if ((i == 0) or i == (number_of_stars -1)):
			is_horizontal = True

		for j in range(number_of_stars):
			if is_horizontal:
				screen_output += " "
				continue
			if (j == 0) or (j == (number_of_stars - 1)):
				screen_output += " "
				continue
			screen_output += "*"
		screen_output += "\n"

	return screen_output	
				


print(main())
