# 🚨 Don't change the code below 👇
total_heights = 0
number_of_students = 0

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  total_heights += student_heights[n]
  number_of_students = n+1
# 🚨 Don't change the code above 👆




#print(f"total heights : {total_heights}")
#print(f"number of students : {number_of_students}")

#Write your code below this row 👇
average_heights = total_heights / number_of_students

average_heights = round(average_heights)

print(average_heights)

