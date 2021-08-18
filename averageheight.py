student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

heights = 0
total = 0

# Maths without using len() and sum()
for i in student_heights:
	total += i
	heights += 1

average = round(total / heights)

print(f"The average height is {average}")


# 156 178 165 171 187
# 171
