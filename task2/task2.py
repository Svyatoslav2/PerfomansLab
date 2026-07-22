import sys
first_file=sys.argv[1]
second_file=sys.argv[2]
eps = 1e-9
with open(first_file, 'r') as file:
    centre = file.readline().strip()
    radius = file.readline().strip()

xc,xy = map(float,centre.split())
radius=float(radius)
coords=[]
with open(second_file, 'r') as file:
    while True:

        temp=file.readline().strip()
        if temp:
            bx,by=map(float,temp.split())
            coords.append([bx,by])
        else:
            break


for i in coords:
    diff = (i[0]-xc)**2 + (i[1]-xy)**2 - radius**2
    if abs(diff) < eps:
        print(0)
    elif diff>0:
        print(2)
    else:
        print(1)