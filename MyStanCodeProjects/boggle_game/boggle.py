"""
File: boggle.py
Name: Evonne
----------------------------------------
This program runs the boggle game to find find out all valid words in dictionary after user input 16 characters.
The word only can be formed using adjacent (up, down, left, right, and diagonal)characters,
and each letter only can be used once.
The result will shows all valid words and how many valid words in total.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	This program runs the boggle game, it will ask user to input 16 characters first,
	and use recursion to find out all valid words in dictionary.
	It will show the result of all valid words and how many in total.
	"""
	boggle_lst = []
	ch_lst = []  # For read_dictionary use
	for i in range(4):
		letters = input(f'{i+1} row of letters: ')
		lst = letters.split()
		row_lst = []
		for ch in lst:
			if ch.isalpha() and len(ch) == 1:
				ch = ch.lower()
				row_lst.append(ch)
				ch_lst.append(ch)
			else:
				return print('Illegal input')
		boggle_lst.append(row_lst)

	start = time.time()
	####################
	# Make the specific dictionary list for this boggle game.
	dict_lst = read_dictionary(ch_lst)

	# Use a list to record the total number of answers
	total_ans = [0]

	find_anagrams(boggle_lst, dict_lst, total_ans)
	print(f'There are {total_ans[0]} words in total.')

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(ch_lst):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	massive_dictionary = []
	target_dictionary = []

	# Only store the word has the length >= 4 into massive dictionary.
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			if len(word) >= 4:
				massive_dictionary.append(word)

	# To compare and only leave the word has more than or equal to 4 target characters in the dictionary.
	for word in massive_dictionary:
		matched_ch = 0
		for ch in word:
			if ch in ch_lst:
				matched_ch += 1
		if matched_ch >= 4:
			target_dictionary.append(word)

	return target_dictionary


def find_anagrams(boggle_lst, dict_lst, total_ans):
	"""
	:param boggle_lst: list, the 4 x 4 list array from user input
	:param dict_lst: list, the dictionary list.
	:param total_ans: list, with an int inside to record the total number of answers
	"""
	ans_lst = []
	index_lst = []

	# 將list視為二維矩陣(row 4, column 4)，逐一讀取16個字母
	for x in range(4):
		for y in range(4):
			find_anagrams_helper(x, y, '', index_lst, boggle_lst, ans_lst, dict_lst)
	total_ans[0] += len(ans_lst)


def find_anagrams_helper(x, y, current_s, current_index, boggle_lst, ans_lst, dict_lst):

	# 重複按照九宮格方式找出相鄰字母，並排除邊界條件以及已經存取過的座標(x,y)
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			ch_x = x + i
			ch_y = y + j
			if 0 <= ch_x < 4 and 0 <= ch_y < 4 and (ch_x, ch_y) not in current_index:

				# Choose
				current_s += boggle_lst[ch_x][ch_y]
				current_index.append((ch_x, ch_y))
				if current_s in dict_lst and current_s not in ans_lst:
					print(f'Found: {current_s}')
					ans_lst.append(current_s)

				# Explore
				if has_prefix(current_s, dict_lst):
					find_anagrams_helper(ch_x, ch_y, current_s, current_index, boggle_lst, ans_lst, dict_lst)

				# Un-choose
				current_index.pop()
				current_s = current_s[:len(current_s) - 1]


def has_prefix(sub_s, dict_lst):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dict_lst: list, the dictionary list.
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dict_lst:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
