a = []

class Agent():
    def __init__(self,p:list,ste:bool,bre:bool,wum:bool,gol:bool,pit:bool,i:int,j:int):
        self.p = p
        self.s = ste #stench
        self.b = bre #breeze
        self.w = wum #wumpus
        self.g = gol #gold
        self.h = pit #pit
       # self.pos = False
        self.i = i
        self.j = j
    #directions
        self.l = True
        self.u = True
        self.d = True
        self.r = True
    #visited
        self.visit = False

def left(vars):
    return [vars.i,vars.j - 1]

def right(vars):
    return [vars.i,vars.j + 1]

def up(vars):
    return [vars.i - 1,vars.j]

def down(vars):
    return [vars.i + 1,vars.j]

for i in range(0,4):
    b = []
    for j in range(0,4): 
        print(f"\nFor square [{4-i}][{j+1}]: Stench-s/Breeze-b/Wumpus-w/Pit-p/Gold-g ")
        s = input("Enter detail : ")
        s = s.lower().split(" ")
        ste = "s" in s
        bre = "b" in s
        wum = "w" in s
        gol = "g" in s
        pit = "p" in s
        ag = Agent([4-i,1+j],ste,bre,wum,gol,pit,i,j)
        b.append(ag)
    a.append(b)

for i in range(0,4):
    a[0][i].u = False
    a[3][i].d = False
    a[i][0].l = False
    a[i][3].r = False

r,c = int(input("\nEnter i for start : ")),   int(input("Enter j for start : "))
pos = [4-r,c-1]
print("Initial Position:\n")
for i in range(0,4):
    for j in range(0,4):
        if a[i][j].h:
            print("P",end=" ")
        elif a[i][j].w:
            print("W",end=" ")
        elif a[i][j].s:
            print("S",end=" ")
        elif a[i][j].b:
            print("B",end=" ")
        elif i==pos[0] and j==pos[1] and a[i][j].g:
            print("*",end=" ")
        elif a[i][j].visit == True:
            print("V",end=" ")
        elif a[i][j].g:
            print("G",end=" ")
        elif i==pos[0] and j==pos[1]:
            print("A",end=" ")
        else:
            print("-",end=" ")
       
    print()

k = 1
flag = True
while flag:
    arr = []
    if a[pos[0]][pos[1]].u:
        arr.append(a[up(a[pos[0]][pos[1]])[0]][up(a[pos[0]][pos[1]])[1]])
    if a[pos[0]][pos[1]].d:
        arr.append(a[down(a[pos[0]][pos[1]])[0]][down(a[pos[0]][pos[1]])[1]])
    if a[pos[0]][pos[1]].l:
        arr.append(a[left(a[pos[0]][pos[1]])[0]][left(a[pos[0]][pos[1]])[1]])
    if a[pos[0]][pos[1]].r:
        arr.append(a[right(a[pos[0]][pos[1]])[0]][right(a[pos[0]][pos[1]])[1]])

    status = [None,None,None,None,None]
    
    for ele in arr:
        if(ele.visit == False):
            if(ele.h==False):
                if (ele.w==False):
            
                    if a[ele.i][ele.j].h:
                        print("P",end=" ")
                        status[3]="Pit"
                    if a[ele.i][ele.j].s:
                        print("S",end=" ")
                        status[0]="Stench"
                    if a[ele.i][ele.j].b:
                        print("B",end=" ")
                        status[1]="Breeze"
                    if a[ele.i][ele.j].w:
                        print("W",end=" ")
                        status[4]="Wampus"
                    if a[ele.i][ele.j].g:
                        print("G",end=" ")
                        status[2]="Glitter"
                    a[ele.i][ele.j].pos = True
                    pos = [ele.i,ele.j]
                    a[ele.i][ele.j].visit = True
                    break
                
    print(f"\nFor iteration {k}:\n")
    for i in range(0,4):
        for j in range(0,4):
            if a[i][j].h:
                print("P",end=" ")
            elif i==pos[0] and j==pos[1] and a[i][j].g:
                print("*",end=" ")
            elif a[i][j].s:
                print("S",end=" ")
            elif a[i][j].b:
                print("B",end=" ")
            elif a[i][j].w:
                print("W",end=" ")
            elif i==pos[0] and j==pos[1]:
                print("A",end=" ")
            elif a[i][j].visit == True:
                print("V",end=" ")
            elif a[i][j].g:
                print("G",end=" ")
            else:
                print("-",end=" ")
        print()
    print()

    print(status)

    print(f"Points: {1000-k}")
    k += 1

    if a[pos[0]][pos[1]].g==True:
        print(f"Gold found at position {a[pos[0]][pos[1]].p}")
        flag = False
        break
    else:
        continue