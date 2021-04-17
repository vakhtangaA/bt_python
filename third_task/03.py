import math

z = int(input("ჩაწერე z-ის მნიშვნელობა: "))

numerator = math.pow(10, -7) * math.log(abs(9 * math.pow(z, 3))) + math.cos(2 * math.pow(z, 2))
denominator = math.pow(abs(z + 1), 2) + 2 * math.pow(10, 6)

print(numerator / denominator)