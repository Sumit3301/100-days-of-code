#avg height
heights=input("Enter heights of people").split()
print(heights)
i=0
for n in range(0,len(heights)):
    heights[n]=int(heights[n])
    sum=sum+heights[n]
    i+=1
print(f'Number of people ={i}')
    

