#1) Create and Assign a type float variable called fltOne the value 10 (3)
print ("task 1")
fltOne = 10.
print (float(fltOne))
print ()

#2) Create and Assign a type float variable called fltTwo the value 20 (3)
print ("task 2")
fltTwo = 20.
print (float(fltTwo))
print ()

#3) Create and Assign a type float variable called fltThree with the product of fltTwo and fltOne(3)
print ("task 3")
fltThree = (fltOne + fltTwo)
print (fltThree)
print ()

#4) Create and assign a variable called stringOne with the value "The product of fltOne and fltTwo = "(3)
print ("task 4")
stringOne = ("The product of fltOne and fltTwo = ")
print (stringOne)
print ()

#5) On the console, output stringOne and fltThree (in that order) (3)
print ("task 5")
print (stringOne, fltThree)
print ()

#6) increment fltOne (3)
print ("task 6")
fltOne = fltOne + 1
print (float(fltOne))
print ()

#7) prompt the user to provide an input to fltTwo with the message "Please provide another number for fltTwo". Ensure a float is given (4)
print ("task 7")
fltTwo = float (input("Please provide another number for fltTwo"))
print ()

#8) on the console, output the product of fltOne and fltTwo with a suitable message (3)
print ("task 8")
print ("The product of fltOne and flTwo is :", float (fltOne + fltTwo))
print ()

#8) take the input from fltTwo and apply a decision based on the number inputted.
#The decision should be based on if the user inputs a number below 100
#the code should output "below 100" (5)
print ("task 8")
if fltTwo < 100:
	print ("below 100")
print ()

#Float (Input ("Please provide another number for fltTwo"))
#if fltTwo <= 100
#Print ('below 100')

#9) take the difference between of fltOne and fltTwo (fltOne - fltTwo)
#Using if, else and elif, output the following:
#If the product is below 0, output "below 0"
#if the product is 0 output "value is zero"
#if the product is above 0 output "above 0" (8)
print ("task 9")
#print ("fltOne - fltTwo = ")
difference = fltOne - fltTwo
if difference < 0: 
	print ("below 0")
elif difference is 0:
	print ("value is zero")
else: 
	print ("above 0")
print ()

#10) create a list called listOfInts (4)
print ("task 10")
listOfints = [4,6,8,10,12,14,16,18,20,22]
print (listOfints)
print ()

#11 part a) create a for loop to iterate through the above list and populate the list with
#{4,6,8,10,12,14,16,18,20,22}. Output the list to the console with a suitable message(7)
print ("task 11")
print ("list of ints")
for x in range(len(listOfints)): 
    print(listOfints[x])
print ()

#11 part b) create a for loop to iterate through the above list and
#multiply each value by three assigning the new value to the respective
#index in the list. The list should now look like {12,18,24.....} (8)
print ("task 11")
print ("list of ints * 3")
for x in range(len(listOfints)): 
    print(listOfints[x]*3)
print ()

#11 part c )output listOfInts to the screen with a suitable message (3)
#print ("listOfints: ", range(len(listOfints)))

#14) create a function which calculates a decrease of a given percentage (10 marks)
# the function should be called calcPerc
#the function should take a cost parameter and a percentage parameter
#it should return the cost less the percentage amount
#For example if the paramenters are cost = 100 and percentage = 50, it should return 50.
#For another example, if the parameters are cost = 50 and percentage = 10, it should return 45.
#The percentage value should assume 10% if no value is given
#print a test to the screen with cost set as 50 and percentage set as 10
print ("task 14")
def calcPerc (cost, percentage):
	print ("calcPerc", (cost - percentage))
calcPerc (100, 50)
calcPerc (50, 10)
print ()

#15) create a function called caseChanger which takes a string argument written all in lower case
#It will output all letters in lowercase except e which it will convert to capital E (10 marks)
#Perform a test print which using hello: caseChanger("hello") this should
#print hEllo to the console.
print ("task 15")
#def caseChanger (letter):
#	print ("caseChanger", letter)
#string = input()
#caseChanger (string)
def count (letter):
	string = input("Please input word") # <- user can type string into command line and end by 'Enter'
	count = 0
	for each in string:
		if each == letter:
			count += 1
print (count)
#for each e in string:
#letter = input("What is your word?")
#print (letter)
#final_letter = letter.lower()
#print(final_letter)
#print ()

#16)a) Create a list that represents a set of students. The list should contain the following
#students: Clark,Horan,Rai,White,Cooper,Jones,Cox,Smith (4 marks)
#b) use a method to order the students so that they are in alphabetical order (3 marks)
print ("task 16")
students = ["Clark", "Horan", "Rai", "White", "Cooper", "Jones", "Cox", "Smith"]
print (students)
#for i in students:
#	print (i)
for i in range(len(students)):
	print (sorted(students))
#thislist = ["apple", "banana", "cherry"]
#for i in range(len(thislist)):
#print(thislist[i])
print ()

#17) create a tuple that represents exam marks with the following data. (4 marks)
#These are the respective exam marks for the alphabetically ordered student list
# 65,66,67,80,90,65,65,93
print ("task 17")
#my_tuple = (students, [65,66,67,80,90,65,65,93], )
#print(my_tuple)
#number_students = int(input("Number of Students: ")) #get number of students
#number_grades = int(input ("How many grades per student: ")) #get number of grades per student
#student_list = {} #create empty student dictionary
#for num in range(number_students):
#name = input("Enter Student Name: ")
#student_list[name] = []
#for num in range(number_grades):
#grade = input(f"Enter grade for {name} ")
#student_list[name] += [grade]
print ()

#18) Dictionary question (9 marks)
#No idea, still learning
#create a dictionary
#write code which adds both the student and a their corresponding mark.
#do not perform this long hand (as in writing out the values above). Use data
#from the existing tuples above to create the dictionary
