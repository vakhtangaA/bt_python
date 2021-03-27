
def printer(num):
    wholeNumber = num // 3
    preciseNumber = num / 3

    print(str(num) + '-ისთვის 3-ზე გაყოფისას, მთელი რიცხვია '
    + str(wholeNumber) + ' და ზუსტი მნიშვნელობაა ' + str(preciseNumber) + '\n')

nums = [4, 14, 25]

for num in nums:
    printer(num)
