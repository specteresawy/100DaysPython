# 🚨 Don't change the code below 👇

student_heights = input("Input a list of student heights ").split()

# 🚨 Don't change the code above 👆


student_heights =  int(student_heights)

#Write your code below this row 👇
totalHeight = 0
for height in student_heights:
  totalHeight += height
print(totalHeight)

numberOfStudents = 0
for student in student_heights:
  numberOfStudents+=1



average_heights = totalHeight / numberOfStudents

average_heights = round(average_heights)

print(average_heights)



  