students=input("Enter Scores of students").split()
print(students)
for n in range (0,len(students)):
    students[n]=int(students[n])
print(students)
high_score=0
for i in range(0,len(students)):
    if(high_score<students[i]):
        high_score=students[i]
print(high_score)
