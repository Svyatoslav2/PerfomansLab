import sys
n = int(sys.argv[1])
m = int(sys.argv[2])
test=[]
arr = list(range(1, n + 1))
result="1"
current=0
while True:
    end = (current + m - 1) % n   
    if end == 0:                 
        break
    result += str(arr[end])       
    current = end     
print(result)

