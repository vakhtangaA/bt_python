import random
from collections import Counter
import math

subjects = ('Python', 'Microprocessor', 'Programming Languages', 'Computer Software', 'Mobile Development')

numberOfStudents = int(input('დ  ა ა ს ა ხ ე ლ  ე თ   ს ტ უ დ ე ნ ტ ე ბ ი ს   ს ა ე რ  თ  ო   რ ა ო დ ე ნ ო ბ ა '))

students = []


class Student:
    def __init__(self, name):
        self.name = name
        self.mySubjects = []
        self.checkerSubjects = []
        numberOfSubjects = random.randint(1, len(subjects))


        for x in range(numberOfSubjects):
        	class Subject:
        		def __init__(self, subject, result):
        			self.subject = subject
        			self.result = result
        	
        	subject = random.choice(subjects)

        	if subject not in self.checkerSubjects:
        		self.checkerSubjects.append(subject)
        		self.mySubjects.append(Subject(subject, 0))




    def printInfo(self):
        print('Hello, my name is ' + self.name + ' and my subjects are: ')
        print('--------------------------------------------------------')
        for x in self.mySubjects:
        	print(x.subject + ' - ' + str(x.result))

        print('\n')

    def exam(self):
    	for x in self.mySubjects:
    		x.result = random.randint(51, 100)

    def getSubjects(self):
    	return self.mySubjects



for x in range(numberOfStudents):
	students.append(Student('Student ' + str(x + 1)))


all_subjects = []
subjectsWithPoints = []

for x in students:
	subs = x.getSubjects()
	for x in subs:
		all_subjects.append(x.subject)
		subjectsWithPoints.append(x)
	



print('--------------------BEFORE EXAM---------------------')
for student in students:
	student.printInfo()
	student.exam()

print('--------------------AFTER EXAM-----------------------')
for student in students:
	student.printInfo()


print('--------------------STATISTICS---------------------------:')

count = Counter(all_subjects)
print('Students Per Subject \n')
for x in count:
	print(x + ' - ' + str(count[x]))

print('\nAverage point per Subject\n')


python, microprocessor, programming_languages, computer_software, mobile_development = 0, 0, 0, 0, 0

'Microprocessor', 'Programming Languages', 'Computer Software', 'Mobile Development'
for x in subjectsWithPoints:
	if x.subject == 'Python':
		python += x.result
	elif x.subject == 'Microprocessor':
		microprocessor += x.result
	elif x.subject == 'Programming Languages':
		programming_languages += x.result
	elif x.subject == 'Computer Software':
		computer_software += x.result
	elif x.subject == 'Mobile Development':
		mobile_development += x.result
	else:
		print('Out Of Scope' + x.subject)

forAverage = [python, microprocessor, programming_languages, computer_software, mobile_development]


for x in subjects:
	if count[x] != 0:
		if x == 'Python':
			print(x + ': ' + str(math.floor(python / count[x])))
		elif x == 'Microprocessor':
			print(x + ': ' + str(math.floor(microprocessor / count[x])))
		elif x == 'Programming Languages':
			print(x + ': ' + str(math.floor(programming_languages / count[x])))
		elif x == 'Computer Software':
			print(x + ': ' + str(math.floor(computer_software / count[x])))
		elif x == 'Mobile Development':
			print(x + ': ' + str(math.floor(mobile_development / count[x])))

