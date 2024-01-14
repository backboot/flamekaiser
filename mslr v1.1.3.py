#importing modules
import random as ran
import math

#defining functions
def type(text):
    import time
    for i in text:
        print(i,end='',flush=True)
        time.sleep(0.04)

def cricket():
    if gen=='male':
        cricyn="Do you like cricket "+name+" ?"
        type(cricyn)
        print()
        e=str(input(" "))
        if e=="yes":
            type("Which team do you like ?")
            print()
            team=str(input(" "))
            favtem="Hurray "+team+" is a great team.My favorite too!!:)"
            type(favtem)
            print()
        else:
            type("Oh, then what is ur favourite sport ?")
            print()
            favsp=input()
            type("yeah! it is also a popular game")
            print()

def ambition():
    ambit="what is your ambition "+name+" ?"
    type(ambit)
    print()
    g=str(input(" "))
    myambit="yes "+g+" is a great AMBITION"
    type(myambit)
    print()
    remamb="But remember one thing ,You must work as hard as possible to acheive your goal "+name+" :)"
    type(remamb)
    print()
def favfood():
    type("What is ur favorite food "+ name+" ?")
    food=input()
    type(food+" is a real mouth-watering dish ")
    print()

#intro
type("HELLO !! I am MSLR_18 , A python-based conversation program created by Rahul_cr ")
print()
type("Greetings to you ,I would be happy to interact with you today . But before that I would be happy to know ur name .....")
print()

#gender detection
type("Enter your name :")
name=str(input())
if name[-1] == "a" :
        ge="hi "+name+" mam"
        type(ge)
        gen="female"
elif name[-1] =="i":
        ge="hi "+name+" mam"
        type(ge)
        gen="female"
elif name[-1] =="u":
        ge="hi "+name+" mam"
        type(ge)
        gen="female"
else :
        ge="hi "+name+" sir"
        type(ge)
        gen="male"

print()

#age
aeg="enter your age :"
type(aeg)
print()
age=int(input())



#age divisions
#children
if age<=8 :
        crtn="do you watch cartoon "+name+" ?"
        type(crtn)
        print()
        c=str(input(" "))
        if c=="yes":
            wcrtn="which cartoon do you like the most "+name+" ?"
            type(wcrtn)
            print()
            d=str(input(" "))
            like="I too like "+d+":)"
            type(like)
            print()
        else:
            type("Oh , I see .....It is actually weird to hear that a kid does not watch cartoon :(")
            print()
            type("What are your hobbies "+name +" then ?")
            crtn=input()
            type("great, i hope u enjoy it :) ")
        print()
        #calling functions
        latemov="what is the latest movie that you watched "+name+" ?"
        type(latemov)
        print()
        movi=input(" ")
        enjoymov="Yeah "+movi+" is a very good movie. I hope you enjoyed it :)) "
        type(enjoymov)
        print()
       
        ambition()
        favfood()
        print()

#teenage
elif 8<age<=17:
    #school rating
    type("Enter ur school name :")
    print()
    sch=str(input())
    type("Enter ur rating for ur school(from 1 to 5) :")
    print()
    rate=float(input())
    if rate<=3:
        ty="Try to cope up with "+sch+" "+name
        type(ty)
        print()
    if rate>3:
        hsws="I hope ur satisfied with "+sch+' '+name+" :)"
        type(hsws)
        print()
    strd="Which standard are you studying "+name+" ?"
    type(strd)
    print()
    z=str(input(" "))
    rhsc="Oh! great "+name+",I hope you're studing well in grade "+z+" ☺"
    type(rhsc)
    print()
    if z!="lkg":
        wpe="Are you performing well in your exams "+name+" ?"
        type(wpe)
        print()
    y=str(input(" "))
    if y=="yes":
        type("would you like to enter your mark systematically in python ?")
        print()
        ms=input()
        #mark input
        if ms == "yes":
            type("Great!!")
            print()
            sbj="Enter the number of subjects: "
            type(sbj)
            print()
            subj = int(input())
            exam_marks = {}

            for i in range(subj):
                type("Enter the subject name: ")
                print()
                subject = input()
                sbjc="Enter your mark in "+subject+": "
                type(sbjc)
                print()
                mark = int(input())
                exam_marks[subject] = mark

            type("Your exam report:")
            print()
            type(exam_marks)
            print()

            highest_mark = max(exam_marks.values())
            lowest_mark = min(exam_marks.values())

            highest_mark_subject = ""
            lowest_mark_subject = ""

            for subject, mark in exam_marks.items():
                if mark == highest_mark:
                    highest_mark_subject = subject
                if mark == lowest_mark:
                    lowest_mark_subject = subject

            type("Your highest mark is in "+ highest_mark_subject+ " ("+ str(highest_mark)+ ") ")
            print()
            type("Your lowest mark is in " + lowest_mark_subject+ " ("+ str(lowest_mark)+ ") ")
            print()

    else:
        adv="It's ok "+name+",You can perform really better in the next exam if you work a bit more ☺"
        type(adv)
        print()
        adv1="NEVER EVER GIVE UP AND LOSE HOPE!!!Everyone born in this world are special in some way"
        type(adv1)
        print()
        type("So always be happy :)")
        print()
    #calling functions
    latemov="what is the latest movie that you watched "+name+" ?"
    type(latemov)
    print()
    movi=input(" ")
    enjoymov="Yeah "+movi+" is a very good movie. I hope you enjoyed it :)) "
    type(enjoymov)
    print()
    
    ambition()
    favfood()
    #siblings 
    sibbb="Do you have any siblings "+name+" ?"
    type(sibbb)
    print()
    sib=input()
    if sib=="yes":
        type("How many siblings do you have ?")
        print()
        sibno=int(input())
        sb=[]
        for tyu in range(1,sibno+1):
            bros="I would be happy to know his or her name "+name+" :)"
            type(bros)
            print()
            sibn=input()
            sb.append(sibn)
        wowsib="What a match "+name+" and "+str(sb)
        type(wowsib)
        print()
    #games
    if gen=="male":
        print("do you play online games",name,"?")
        game=input()
        if game=="yes":
            type("Which is your favorite game?")
            print()
            gmf=input()
            gta=gmf+" is one the most famous game among teenagers like you"
            type(gta)
            print()
        else:
            type("oh !! I am amazed as it is like finding a GEM IN THE DIRT to find a teenager not playing games ")
            print()
    #princess
    if gen=="female":
        princes="Do you like disney princesses "+name+" ?"
        type(princes)
        print()
        dp=input()
        if dp=="yes":
            type("Do you know that some of the disney princess are based on real people?")
            print()
            print("For example:", end="/n")
            type("Mulan - Mulan is based on the Chinese legend of Hua Mulan, a female warrior who took her father's place in the army by disguising herself as a man")
            print()

#young adult
elif 17<age<=22 :
    type("i do not wish to advice u like a boomer but this period in ur life is the most important part so beware and whom u choose as ur friend will choose ur future")
    print()
    type("i think you are doing well in ur higher studies "+name+ " :)")
    latemov="what is the latest movie that you watched "+name+" ?"
    type(latemov)
    print()
    movi=input(" ")
    enjoymov="Yeah "+movi+" is a very good movie. I hope you enjoyed it :)) "
    type(enjoymov)
    print()
    
    ambition()
    favfood()
    type("what is the name of ur college "+name+" ?")
    college=input()
    type("how would u rate "+ college+" " +name+" in range of 1 to 10 ?")
    colrate=int(input())
    if colrate<4:
        type("oh !! but try to to cope up with ur college")
    elif 4<colrate<8:
        type("ok then be happy with what u have :) ")
    else:
        type("great , i think u are very much satisfied with ur college")
    #gra. ideas
    print()
    whagrad="What would you like to do after graduation "+name+"?"
    type(whagrad)
    print()
    gri=input()
    greegrad="My greetings to you "+name+".... I hope you acheive it "
    type(greegrad)
    print()
    
#adult
elif  22<age<=57:
    #profession
    proff="what is your profession "+name+" ?"
    type(proff)
    print()
    h=str(input(" "))
    if h=="housecook" :
        merehum="WOW!! "+name+" you are feeding your family members,you are a more than a mere human :)"
        type(merehum)
        print()
    if h!="housecook" :
        jobpro=h+" is a great job!I hope you love it "+name+":)"
        type(jobpro)
        print()
    if age>25:
        #children present
        type("Do you have any children ?")
        print()
        ch=input()
        if ch=="yes":
            type("Great")
            print()
            type("How many children do you have ?")
            print()
            chino=int(input())
            cl=[]
            for cyu in range(1,chino+1):
                kids="I would be happy to know his or her name "+name+" :)"
                type(kids)
                print()
                chin=input()
                cl.append(chin)
            type('i hope '+str(cl)+' are not too mischievous :)')
    print()        
    latemov="what is the latest movie that you watched "+name+" ?"
    type(latemov)
    print()
    movi=input(" ")
    enjoymov="Yeah "+movi+" is a very good movie. I hope you enjoyed it :)) "
    type(enjoymov)
    print()
    print()
    favfood()
    print()
    
    if gen=='female':
        #cooking
        type('do you know cooking '+name+' ?')
        cook=input()
        if cook=='yes':
            type("i hope ur family members like ur cooking :)")
        else:
            type("it's ok, i hope u are working hard to learn it :)")
          
    #fitness
    print()
    type("Are you physically fit ??")
    fitt=input()
    if fitt =='yes':
        type("How do you stay healthy physically?")
        print()
        fit=input()
        type("Great, you have something that many people of your age lack")
        print()
    else:
        type("It's ok! Try to do exercise and be fit and always be Happy as our life is very short ,friend :)")
        print()
    #savings
    type("Are u doing some savings in bank and have u invested in stock market ?")
    print()
    smi=input()
    if smi=='yes':
        type('then i hope that u might know what does fd and rd mean?')
        print()
    else:
        type('then i hope that u might not know what does fd and rd mean?')
        print()
        print()
        type("it's ok i will teach u as it is important to lead a sustainable life ")
        print()
        print()
        type("In a Fixed Deposit, you put a lump sum in your bank for a fixed tenure at an agreed rate of interest. At the end of the tenure, you receive the amount you have invested plus compound interest")
        print()
        print()
        type("RD offers you a fixed interest on the invested amount at a specific frequency till the pre-determined term or up on maturity. At the end of the term, the amount upon maturity(which is your invested capital) along with remaining or accumulated interest is paid")
        print()
        print()
    type('would u like to calculate rd?')
    print()
    savi=input()
    #R.D
    if savi=='yes':
        type("Enter principal amount :")
        principal=int(input())
        princ=0
        princ+=principal
        type("Enter rate of interest :")
        rate=float(input())
        type("Enter no. of times to be compounded :")
        no=int(input())
        for gh in range(1,no+1):
            si=principal*rate/(100*12)
            print("si of",gh,"month:",int(si))
            a=principal+si
            print("amount of",gh,"month:",int(a))
            principal=a+princ
        else:
            finammo="total amount you have gained after"+' '+str(gh)+' '+"years ="+str(principal-princ)
            type(finammo)
            print()
    #goal
    type("what is your goal in life?")
    print()
    goal=input()
    type("My congrats to you !! Work really hard to acheive it")
    print()
    
#senior citizens
elif age>57:
    #lifetime goal
    type("I hope you have acheived your lifetime goal.....")
    print()
    type("Did you ?")
    print()
    j=str(input())
    if j=="yes":
          print("what is it",name,"?")
          i=str(input(" "))
          lifetime="it's great "+name+" you are an inspiration to me"
          type(lifetime)
          print()
    if j!="yes":
          worklife="work a bit more to acheive it "+name+" !"
          type(worklife)
          print()
    #grandchildren
    grachi="Do you have grandchildren "+name+" ?"
    type(grachi)
    print()
    gc=input()
    if gc=="yes":
        type("I would be happy to know their names....")
        print()
        gcn=input()
        gcnhope="I hope "+gcn+" are lokking after you well :>"
        type(gcnhope)
        print()
    latemov="what is the latest movie that you watched "+name+" ?"
    type(latemov)
    print()
    movi=input(" ")
    enjoymov="Yeah "+movi+" is a very good movie. I hope you enjoyed it :)) "
    type(enjoymov)
    print()
    favfood()
    
#random game
type("do u wish to play a random game "+name+" ?")
gmer=input()
if gmer == 'yes':
    type("The rules are simple :")
    print()
    type("        1)You have to select a no. between 1 and 10 (both included)")
    print()
    type("        2)Based on the closeness of your no. to the randomly generated no. , points will be awarded to you")
    print()
    type("        3)If u want to continue type 's',if you want to stop type 'no'")
    print()
    l=[]
    n=1
    n1=ran.randrange(1,11)
    i=int(input("Enter your no.:"))
    if i!=n1:
        print("the no. was",n1)
        p=(10-math.fabs(n1-i))*10
        print("your score is ",p)
        l.append(p)
    elif i ==n1:
        type("Woow,u have guessed it correct!!")
        print()
        p=100
        l.append(p)
        print("your score is ",p)
    n=2
    while n >0:
        type("Ready for your nxt turn?")
        print()
        a=input()
        if a =="s":
            n1=ran.randrange(1,11)
            i=int(input("Enter your no.:"))
            print("the no. was",n1)
            if i!=n1:
                p=(10-math.fabs(n1-i))*10
                l.append(p)
                print("your score is ",p)
            elif i ==n1:
                type("Woow,u have guessed it correct!!")
                print()
                p=100
                l.append(p)
                print("your score is ",p)    
            n+=1
        else:
            s=sum(l)
            totsco="your score is"+' '+str(s)+"/"+str((n-1)*100)
            type(totsco)
            print()
            avg=s/(n-1)
            avgvg="avg. score ="+str(avg)
            type(avgvg)
            print()
            break
else:
    type("it's ok :)")
    print()
cricket()
print()
#factorial
facto="Do you know what a factorial is "+name+"?"
type(facto)
print()
an=input()
if an=="yes":
    type("Oh! great")
    print()
    type("Enter the required no. for which you would like to see the factorial of :")
    print()
    n=int(input())
    i=1
    f=1
    while i<=n:
        f=f*i
        i+=1
    print(f)
else:
    type("It's Ok :), let me teach you")
    print()
    type("Factorial of a no. is the product of all the natural no. till a given no.")
    print()
    type("for ex.) 5! = 1*2*3*4*5")
    print()
    type("Now do you understand it ?")
    print()
    ns=input()
    if ns=="yes":
        type("Enter the required no. for which you would like to see the factorial:")
        print()
        n=int(input())
        i=1
        f=1
        while i<=n:
            f=f*i
            i+=1
        print(f)
type("ok then "+name+" , i think it is time for us to depart . But before that would u like to see a report of our conversation ?")
fin=input()
if fin=='yes':
    type('FINAL REPORT :')
    print()
    type('  your name: '+name)  
    print()
    type('  your age: '+str(age))
    print()
    if age < 8 :
        if c=="yes":
            type('  your fav. cartoon :'+d)
        print()
        
    if 8<age<=17:
        type('  your school :'+sch+' ('+str(rate)+' /5)')
        print()
        type('  grade :'+z)
        print()
        if y=='yes':
            type('  your academic status : Topper ')
            print()
        if sib=='yes':
            type('  no. of siblings :'+str(sibno))
            print()
        
    if 17<age<=22:
        type('  your college :'+college+' ('+str(colrate)+"/10)")
        print()
        
        print()
    if 22<age<=57:
        type("  your profession :"+h)
        print()
        type("  your children :"+str(cl))
        print()
        if smi=='yes':
            type('  savings : sustainable')
            print()
        type('  goal in life :'+goal)
        print()
    if age>57:
        if j=='yes':
            type('  lifetime goal : acheived')
            print()
        else:
            type('lifetime goal : in a not too far future')
            print()
        type("  grandchildren :"+gcn)
        print()
    type("  latest movie watched :"+movi)
    print()
        
    
    type("  your guessing rate in the random game is "+str(avg)+"%")
    print()
tnx="thank you "+name+" bye"
type(tnx)
print()
type("See you next time")
print()
type("Until then ,this is your favorite Program MSLR signing off ")
print()
type("Have a wonderful day ahead :))")
print()    
