#!/usr/bin/env python3

#Exercise 1-highest score exercise Looping, conditionals

student_scores = [78, 90, 78, 22, 55, 97, 100]
highest_score = 0;
for score in student_scores:
	if score > highest_score:
		highest_score = score

print(f"The highest score in the class is : {highest_score}")


#Exercise 2- for loop using range function

total = 0
for number in range(1, 101):
	total += number
print(total)

#Exercise 3- Adding even numbers
total = 0
for number in range(2, 101, 2):
	if number % 2 == 0:
		print(number)
		

	
#4 Fizz Buzz Exercise
		
for num in range (1, 101):
	if num % 3 == 0 and num % 5 ==0:
		print("Fizz Buzz")
	elif num % 3 == 0:
		print("Fizz Buzz")
	elif num % 5 ==0:
		print("Fizz")
	else:
		print(num)