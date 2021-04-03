a = input("ჩაწერე a-ს მნიშვნელობა: ")
b = input("ჩაწერე b-ს მნიშვნელობა: ")
c = input("ჩაწერე c-ს მნიშვნელობა: ")
d = input("ჩაწერე d-ს მნიშვნელობა: ")

a = float(a)
b = float(b)
c = float(c)
d = float(d)

def powered(a, b, c, d):
    r = (a + b + c + d) ** 0.25
    print(r)
    return r

powered(a, b, c, d)
