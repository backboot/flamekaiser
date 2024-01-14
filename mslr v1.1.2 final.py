import webbrowser as wb
def type(text):
    import time
    for i in text:
        print(i,end='',flush=True)
        time.sleep(0.04)
        
type("HELLO !! I am MSLR_18 , A python-based conversation program created by Rahul_cr ")
print()
type("Greetings to you ,I would be happy to help you today . But before that.....")
print()
type("Enter your name :")
name=str(input())
if name[-1] == "a" :         #gender detection program 
        type("hi "+name+" mam")
        
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
caps="your name fully capitalized is "+ name.upper()
type(caps)
print()
title="your name in title form is ",name.title()
type(title)
print()
aeg="enter your age :"
type(aeg)
print()
age=int(input())
if age<=10 :
        crtn="do you watch cartoon "+name+" ?"
        type(crtn)
        print()
        c=str(input(" "))
        if c=="yes":
            wcrtn="which cartoon do you watch "+name+" ?"
            type(wcrtn)
            print()
            d=str(input(" "))
            like="I too like"+d+":)"
            type(like)
            print()
if 8<age<=17:
    type("enter ur school name :")
    print()
    sch=str(input())
    type("enter ur rating for ur school(1 to 5) :")
    print()
    rate=float(input())
    if rate<=3:
        ty="try to cope up with "+sch
        type(ty)
        print()
    if rate>3:
        hsws="i hope ur satisfied with "+sch+" :)"
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
        wpe="are you performing well in your exams "+name+" ?"
        type(wpe)
        print()
    y=str(input(" "))
    if y=="yes":
        type("would you like to enter your mark systematically in phyton ?")
        print()
        ms=input()
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
            highest_mark_subject = [subject for subject, mark in exam_marks.items() if mark == highest_mark]
            lowest_mark_subject = [subject for subject, mark in exam_marks.items() if mark == lowest_mark]    
            print(f"Your highest mark is in {highest_mark_subject} ({highest_mark})")
            print()
            print(f"Your lowest mark is in {lowest_mark_subject} ({lowest_mark})")
            print()
    else:
        adv="It's ok "+name+",You can perform really better in the next exam if you work a bit more ☺"
        type(adv)
        print() 
        adv1="NEVER EVER GIVE UP AND LOSE HOPE!!! "+name+" Everyone born in this world are special in some way"
        type(adv1)
        print()
        type("So always be happy :)")
        print()
    movv="what is the latest movie that you watched "+name+" ?"
    type(movv)
    print()
    mov=input(" ")
    gmov="Yeah "+mov+" is one of the greatest movie of this decade"
    type(gmov)
    print()
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
    cricyn="Do you like cricket "+name+" ?"
    type(cricyn)
    print()
    e=str(input(" "))
    if e=="yes":
        type("Which team do you like ?")
        print()
        team=str(input(" "))
        favtem="Hurray "+team+" is a great team.It's my favorite too!! :)"
        type(favtem)
        print()
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
    
elif 17<age<=22 :
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
    if e!="yes":
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
    type("Kindly enter the name of your college:")
    college=input()
    print()
    wowcoll="Wow!! "+college+" is a very famous college "
    type(wowcoll)
    print()
    whagrad="What would you like to do after graduation "+name+"?"
    type(whagrad)
    print()
    gri=input()
    greegrad="My greetings to you "+name+".... I hope you acheive it "
    type(greegrad)
    print()

elif  22<age<=50:
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
    latemov="what is the latest movie that you watched "+name+" ?"
    type(latemov)
    print()
    mov=input(" ")
    enjoymov="Yeah "+mov+" is a very good movie. I hope you enjoyed it :)) "
    type(enjoymov)
    print()
    
    if age>25:
        type("Do you have any children ?")
        print()
        ch=input()
        if ch=="yes":
            type("Great")
            print()
            type("What is their name ?")
            print()
            chname=input()
            agechil="how old are they "+name+"  ?"
            type(agechil)
            print()
            type("I hope they are not too mischievous :))")
            print()
    type("Are you fit mentally and physically ??")
    fitt=input()
    if fitt =='yes':
        type("How do you stay healthy both physically and mentally ?")
        print()
        fit=input()
        type("Great, you have something that many people of your age lack")
        print()
    else:
        type("It's ok! Try to do exercise and be fit and always be Happy as our life is very short ,friend :)")
    type("what is your goal in life?")
    print()
    goal=input()
    type("My congrats to you !! Work really hard to acheive it")
    print()
    type("Do you know what a R.D mean in savings ?")
    print()
    fd=input()
    if fd=="yes":
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
    else:
        type("Oh! I thought you would know it....But it's ok let me teach you ")
        type("It is a type saving in bank in which you will have to deposit amount at a regulr intervals so it would sum up along with some interest and will give you sum after some period of time")
        type("I hope you understood it !")
        type("Let's see an example :")
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
elif age>50:
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
    latemov="what is the latest movie that you watched "+name+" ?"
    type(latemov)
    print()
    mov=input(" ")
    enjoymov="Yeah "+mov+" is a very good movie. I hope you enjoyed it :)) "
    type(enjoymov)
    print()
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
           
import random as ran
import math 
l=[]
type("If u want to start type 'yes' , If u want to continue type 's',if you want to stop type 'no'")
print()
type("The rules are simple :")
print()
type("        1)You have to select a no. between 1 and 10 (both included)")
print()
type("        2)Based on the closeness of your no. to the randomly generated no. , points will be awarded to you")
print()
a=input("do you want to play the guess game?")
print()
if a== "yes":
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
        avg=s/n
        avgvg="avg. score ="+str(avg)
        type(avgvg)
        print()
        break
else:
    type("it's ok :)")
    print()
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
    type("It's Ok :), let me teach you  :)")
    print()
    type("Factorial of a no. is the product of all the natural no. till a given no.")
    print()
    type("for ex.) 5! = 1*2*3*4*5")
    print()
    type("Now do you understand it ?")
    print()
    ns=input()
    if ns=="yes":
        type("Enter the required no. for which you would like to see the factorial of :")
        print()
        n=int(input())
        i=1
        f=1
        while i<=n:
            f=f*i
            i+=1
        print(f)
type("Do you want to search for something in web?")
web=input()
print()
if web=="yes" or "YES" or "Yes":
    type("Do you have an active internet connection ?")
    print()
    Web=input()
    if Web=="no" :
        type("Oh!! , I am sorry if you don't have internet you cannot search for something in the web :(")
        print()
        
    else:
        type("Yeah great !! Let us continue ...... ")
        print()
        type("enter the required word :")
        a=input()
        c="https://www.google.co.in/search?q="
        b=c+a
        wb.open_new_tab(b)

type("Would u like to see the final report of our today's conversation ?")
print()
final=input()
if final == "yes":
    type("Final report:")
    print()
    jhg="your name ="+name
    type(jhg)
    dfg="your age =" +str(age)
    type(dfg)
    print()
    if age<=18:
        print("your school name =",sch)
    if age <23:
        if e =="yes":
            type("you're a CRICKET FAN")
            print()
            sxc="your favorite team is "+team
            type(sxc)
            print()
        if y=="yes": 
            type("you're status:TOPPER IN SCHOOL")
            print()
    if 20<age<=50:
        tyu="your profession :"+h
        type(tyu)
        print()
    if an=="yes":
        type("you have high IQ ☺☺☺☺ :)))")
        print()
    if age>50:
        if gc=="yes":
            qwe="Your grandchildren:"+gcn
            type(qwe)
            print()
    else:
        pass
    ihg="in assumption game , your avg score is "+ avg
    type(ihg)
    print()
    erf="Your recently watched movie :"+mov
    type(erf)
    print()
type("See you next time")
print()
tnx="thank you"+name+"bye"
type(tnx)
print()
type("This is your favorite Program MSLR signing off ")
print()
type("Have a wonderful day ahead :))")
print()
