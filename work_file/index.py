import inspect

with open("./reading.txt", "r") as reader:
	number = reader.read()

def filter(number):
	stringsList = list(number)
	numbersList = [int(i) for i in stringsList]
	# remove multiplies of three
	a = [i for i in numbersList if i % 3 != 0]
	# add one to even numbers
	b = [i + 1 if i % 2 == 0 else i for i in numbersList]
	# only even digits
	c = [i for i in numbersList if i % 2 == 0]
	# remove digits above 5
	d = [i for i in numbersList if i < 5]
	# only odd digits
	e = [i for i in numbersList if i % 2 != 0]

	resultLists = [a, b, c, d, e]

	# transform list to numbers
	resultLists = ["".join(str(e) for e in i) for i in resultLists]

	result = inspect.cleandoc(f"""starting number - {number}
	remove multiplies of three - {resultLists[0]}
	add one to even numbers - {resultLists[1]}
	only even digits - {resultLists[2]}
	remove digits above five - {resultLists[3]}
	only odd digits - {resultLists[4]}
	""")

	return result

result = filter(number)

print(result)

with open("./results.txt", "w") as writer:
	writer.write(result)