#avg height
heights=input("Enter heights of people").split()
print(heights)
i=0
sum=0
for n in range(0,len(heights)):
    heights[n]=int(heights[n])
    sum=sum+heights[n]
    i=i+1
print(f'Number of people: {i}')
print(f'sum of heights:{sum}')
avg=sum/i
print(f'Average height of people {avg}')


