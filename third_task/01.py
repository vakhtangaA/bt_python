x = int(input("ჩაწერე x-ის მნიშვნელობა: "))

x_2, x_3, x_4, x_5 = 1, 1, 1, 1

for i in range(2):
	x_2 *= x

for i in range(3):
	x_3 *= x

for i in range(4):
	x_4 *= x

for i in range(5):
	x_5 *= x


y = 1 - x + x_2 - x_3 + x_4 - x_5

print("y - ის მნიშვნელობაა ", y)

