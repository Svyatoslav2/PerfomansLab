import sys
first_file=sys.argv[1]
numbers=[]
with open(first_file,'r') as f:
    while True:
        
        temp=f.readline().strip()
        if temp: 
            numbers.append(int(temp))
        else:
            break
numbers=sorted(numbers)
medianna= numbers[len(numbers)//2]
result=0
for i in numbers:
    diff=i-medianna
    result+=abs(diff)

print(result)


