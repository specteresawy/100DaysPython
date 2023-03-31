
place_holder = 0

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):   
  student_scores[n] = int(student_scores[n])

max_iteration = len(student_scores) 

for i in range(max_iteration):
      for x in range(0, max_iteration-i-1):     
        if (student_scores[x] > student_scores[x+1]):
          place_holder = student_scores[x+1]
          student_scores[x+1] = student_scores[x]
          student_scores[x]= place_holder



print(f"The highest score in the class is: {student_scores[max_iteration-1]}")
# 🚨 Don't change the code above 👆
print(f"the scores ascendingly are: {student_scores}")
#Write your code below this row 👇

