a = (3 + 7.) * 12

def b():
    c = 15
    return c / 5 + 8.35

b = b()

g = (14 % 3 + 2) / 5

def d():
    a, b, c = 1, 4, 2
    return (a + b + c) // 3

d = d()

def e():
    n, m = 5, 2

    return (m + n) / 2.0

e = e()

def v():
    x = 9
    return 14 - x / 4

v = v()

def z():
    n, m = 5, 2
    return (m ** n) // 7

z = z()

nums = [a, b, g, d, e, v, z]


for num in nums:
    print(num, type(num))
