import random as r
print("welcome to this python baseball game")
st='not out'
score=0
strike=0
while st == 'not out':
    com=r.randrange(1,4)
    user=int(input("enter ur value:"))
    print("my input was",com)
    if com==user:
        score+=1
        print("ur score",score)
        strike=0
        print("ur lifes gone:",strike)
    else:
        strike+=1
        print("ur lifes gone:",strike)
        print("ur score",score)
    if strike ==3:
        st='out'
        print("Ur out")
        print("ur score is",score)
print("Are u ready to bowl?")
cst='not out'
scoreb=0
strikeb=0
while cst == 'not out':
    comb=r.randrange(1,4)
    userb=int(input("enter ur value:"))
    print("my input was",comb)
    if comb==userb:
        scoreb+=1
        print("my score",scoreb)
        strike=0
        print("my lifes gone:",strikeb)
    else:
        strikeb+=1
        print("my lifes gone:",strikeb)
        print("my score",scoreb)
        if strikeb==3:
            print("i'm out")
            cst='out'    
            break
if scoreb>score:
        print('i win')

if cst=='out':
        print("u win")
        
