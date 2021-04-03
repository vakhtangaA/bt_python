a = input("ჩაწერე a-ს მნიშვნელობა: ")
b = input("ჩაწერე b-ს მნიშვნელობა: ")
c = input("ჩაწერე c-ს მნიშვნელობა: ")
d = input("ჩაწერე d-ს მნიშვნელობა: ")

a = float(a)
b = float(b)
c = float(c)
d = float(d)

def divideByFour(a, b, c, d):
    r = (a + b + c + d) / 4
    print(r)
    return r

divideByFour(a, b, c, d)
