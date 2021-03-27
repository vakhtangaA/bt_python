def a():
    x, z = 5, 2
    numerator = x**2 + z**2
    denominator = x**2 - z**2

    y = numerator / denominator

    return y

a = a()

def b():
    m = 5
    y = -8 * (m ** 3) + 4 * (m ** 2) - 5 * m + 6

    return y

b = b()

def g():
     x, y = 4, 5
     z = (x - y) - 7 * (x + y)**3

     return z

g = g()

def e():
    a, b, c, d = 4, 5, 6, 7

    z_1 = (a * b) / (b + c)
    z_2 = (a + d) / (a + b)

    z = z_1 / z_2

    return z

e = e()

nums = [a, b, g, e]

for num in nums:
    print(num)
