student_scores = input("Input a list of student scores ").split()

print(student_scores)

max = 0
for score in student_scores:
	if score > max:
		max = score

print(f"The hieghest score is {max}")

#78 65 89 86 55 91 64 89
#91
