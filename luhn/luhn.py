#!/usr/bin/python3

test_card = "8166032979402153"

def luhn(number):
	waga = 1
	number = number[::-1]
	score = ""
	iloczyn = 0

	for i in range(len(number)):
		if waga == 1:
			score += number[i]
			waga = 2
		#if waga == 2:
		else:
			iloczyn = int(number[i]) * 2
			if iloczyn > 9:
				iloczyn -= 9

			score += str(iloczyn)
			waga = 1

	check_sum = 0

	for k in range(len(score)):
		check_sum += int(score[k])

	return check_sum

if __name__ == '__main__':
	card_number = input("Enter your card number: ")
	# print(luhn(card_number))
	print(luhn(test_card)) 