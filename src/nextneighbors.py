import random
import math

punktezahl=50
punkte=[]
newelement=[5,10,1]
position=[]
nächste=[]

for i in range(0,punktezahl):
    x=random.randint(0,30)
    y=random.randint(0,30)
    c=random.randint(0,4)
    punkte.append([x,y,c])

# nächste Punkte finden
for punkt in punkte:

    position.append(punkt[0])
    position.append(punkt[1])
    distance=math.sqrt((punkt[0]-newelement[0])**2+(punkt[1]-newelement[1])**2)
    if len(nächste)<5:
        nächste.append([distance,punkt[2]])
    else:
        for element in nächste:
            if element[0]>distance:
                nächste.remove(element)
                nächste.append([distance,punkt[2]])

print(nächste)

# welche nummer hat der neue Punkt?
Z0=0
Z1=0
Z2=0
Z3=0
Z4=0
for element in nächste:
    if element[1]==0:
        Z0+=1
    if element[1]==1:
        Z1+=1
    if element[1]==2:
        Z2+=1
    if element[1]==3:
        Z3+=1
    if element[1]==4:
        Z4+=1
print(Z0,Z1,Z2,Z3,Z4)