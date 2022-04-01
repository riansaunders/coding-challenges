def backspace_compare(str1, str2):
  # use two pointer approach to compare the strings
	l = len(str1) - 1
	r = len(str2) - 1

	def get_next_valid_char_index(str, index):
		backspace_count = 0
		while (index >= 0):
			if str[index] == '#':  # found a backspace character
				backspace_count += 1
			elif backspace_count > 0:  # a non-backspace character
				backspace_count -= 1
			else:
				break
			index -= 1  # skip a backspace or a valid character

		return index

	while (l >= 0 or r >= 0):
		i1 = get_next_valid_char_index(str1, l)
		i2 = get_next_valid_char_index(str2, r)
		if i1 < 0 and i2 < 0:  # reached the end of both the strings
			return True
		if i1 < 0 or i2 < 0:  # reached the end of one of the strings
			return False
		if str1[i1] != str2[i2]:  # check if the characters are equal
			return False

		l = i1 - 1
		r = i2 - 1

	return True





def main():
  print(backspace_compare("xy#z", "xzz#"))
  print(backspace_compare("xy#z", "xyz#"))
  print(backspace_compare("xp#", "xyz##"))
  print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()