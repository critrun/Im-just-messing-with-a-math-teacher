import time

TIMEOUT = 40

S = int(input("Answer: "))
T = [int(i) for i in input("Numbers: ").replace(" ","").split(",")]


R = ["+","-","*","/","^","!^","!/","!-"]
startTime = time.time()

def bas(i, bas):
    out=[]
    n = 0
    while True:
        if bas**n > i:
            break
        n+= 1
    n-= 1
    while n >= 0:
        t=0
        while i-(bas**n) >= 0:
            i-= bas**n
            t+= 1
        out.append(t)
        n-=1
    return out

def komb(n, length):
    bruh = ([0 for i in range(length)]+bas(n, len(R)))[-length:]
    return [R[i] for i in bruh]

def perm(n):
    i = 1
    for x in range(n):
        i*= (x+1)
    return i

def permCount(i, perms):
    out=[0 for i in range(perms)]
    step = perms
    while i > 0:
        out[0]+=1
        i-= 1
        for n in range(len(out)):
            if out[n] > perms-n-1:
                out[n] = 0
                out[n+1]+= 1
    return out

print("Finding Number Combs...")
numbCombs = []
penisMomento = 0
for m in range(perm(len(T))):
    temp = []
    for i in T:
        temp.append(i)
    ckomb = []
    
    selection = permCount(m, len(T))
    for i in range(len(T)):
        ckomb.append(temp[selection[i]])
        temp.pop(selection[i])
    
    numbCombs.append(ckomb)

def numb(n):
    return numbCombs[n] 

def calculator(method, a, b):
    if a > 9999999999999 or b > 9999999999999:
        return 9999999999999999
    try:
        if method == "+":
            return a + b
        if method == "-":
            return a - b
        if method == "*":
            return a * b
        if method == "/":
            return a / b
        if method == "^":
            if a > 999999 or b > 999999:
                return 9999999999999
            return a**b
        if method == "!^":
            if a > 999999 or b > 999999:
                return 9999999999999
            return b**a
        if method == "!/":
            return b/a
        if method == "!-":
            return b - a
    except:
        return 999999999999999999

closestAnswer = [[],[], 0]

def printAnswer():
    out = str(closestAnswer[1][0])
    for i in range(len(closestAnswer[0])):
        if closestAnswer[0][i][0] != "!":
            out+= closestAnswer[0][i] + str(closestAnswer[1][i+1]) + ")"
            out = "("+out
        else:
            out = "(" + str(closestAnswer[1][i+1]) + closestAnswer[0][i].replace("!","") + out + ")"
    out = out[1:-1]
    out+= (" =   "+ "~ "*(round(closestAnswer[2]) != closestAnswer[2]) +str(round(closestAnswer[2])) + "\tΔ " + str(abs(closestAnswer[2]-S))).replace("  ~ ", "~ ")
    print(out)

print("Calculating...")
minAnswer = 999999999999
close = False
found = False
for x in range(len(R)**(len(T)-1)):
    calcs = ["+"]+komb(x,len(T)-1)
    for y in range(perm(len(T))):
        numbs = numb(y)
        total = 0
        for i in range(len(calcs)):
            total = calculator(calcs[i], total, numbs[i])
            if total > 9999999999:
                break
        if minAnswer > abs(S-total):
            minAnswer = abs(S-total)
            closestAnswer[0] = calcs[1:]
            closestAnswer[1] = numbs
            closestAnswer[2] = total
            print(" "*50, end="\r")
            printAnswer()
            if abs(S-total) == 0:
                found = True
                break
        if abs(time.time() - startTime) > TIMEOUT:
            close = True
            break
    print(" ",str(1000+round(100*(x+1)/(len(R)**(len(T)-1))))[1:],"%\t",str(round(time.time() - startTime)),"/",TIMEOUT,end="\r")
    if close or found:
        break
print("\n_________________\n")

printAnswer()

if close:
    print("TIMED OUT!")

if found:
    print("Found answer early!")

input("press ENTER to exit.")