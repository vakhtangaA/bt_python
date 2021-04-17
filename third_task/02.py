import random

sum = 0
numbers = 0

while(sum < 999):
	randomInteger = random.randint(100, 150)

	if randomInteger != 111:
		numbers += 1
		sum += randomInteger

	if sum / randomInteger % 5 != 0 and numbers != 0:
		print("საშუალო არითმეტიკულია: ", round(sum / numbers, 2))
