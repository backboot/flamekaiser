# python module for one-timepad
import onetimepad
# python module to create GUI		
from tkinter import *

		
root = Tk()
root.title("CRYPTOGRAPHY")
root.geometry("800x600")

def encryptMessage():					
	pt = e1.get()

	# inbuilt function to encrypt a message
	ct = onetimepad.encrypt(pt, 'random')
	e2.insert(0, ct)

def decryptMessage():					
	ct1 = e3.get()

	# inbuilt function to decrypt a message
	pt1 = onetimepad.decrypt(ct1, 'random')
	e4.insert(0, pt1)
	

# creating labels and positioning them on the grid
label1 = Label(root, text ='plain text')			
label1.grid(row = 10, column = 1)
label2 = Label(root, text ='encrypted text')
label2.grid(row = 11, column = 1)
l3 = Label(root, text ="cipher text")
l3.grid(row = 10, column = 10)
l4 = Label(root, text ="decrypted text")
l4.grid(row = 11, column = 10)

# creating entries and positioning them on the grid
e1 = Entry(root)
e1.grid(row = 10, column = 2)
e2 = Entry(root)
e2.grid(row = 11, column = 2)
e3 = Entry(root)
e3.grid(row = 10, column = 11)
e4 = Entry(root)
e4.grid(row = 11, column = 11)

# creating encryption button to produce the output
ent = Button(root, text = "encrypt", bg ="red", fg ="white", command = encryptMessage)
ent.grid(row = 13, column = 2)

# creating decryption button to produce the output
b2 = Button(root, text = "decrypt", bg ="green", fg ="white", command = decryptMessage)
b2.grid(row = 13, column = 11)


root.mainloop()

"""
import random
import math
no=random.randrange(1,4)
a=input("Enter the required string :")
stc=[]
d=tuple(stc)
stv=[]
stvr=[]
sta=[]
dech=[]
denum=[]

str=''
for i in a:
      stc.append(i)
      stv.append(ord(i))
for v in stv:
      no=random.randrange(1,3)
      dih=random.randrange(1,3)  
      if no == 1:
              v1=random.randrange(65,91)
              if (v1-v)>0:
                      c='.'
              else:
                      c=','
                      
              v2=math.fabs(v1-v)
              stvr.append(int(v2))
              sta.append(chr(v1))
              
      else:
              v1=random.randrange(97,123)
              if (v1-v)>0:
                      c='.' 
                      
              else:
                      c=','
                      
              v2=math.fabs(v1-v)
              stvr.append(int(v2))
              sta.append(chr(v1))         
      
print(stc)
print(stv)
print(stvr)
print(sta)
for k in sta:
        ind=sta.index(k)
        h=stvr[ind]
        hs=h.__str__()
        str+=k+c+hs+c
        
print(str)

if c==',':
        lc=str.split(',')
        for i in lc:
                if i.isalpha() == True:
                        dech.append(i)
                else:
                        denum.append(i)
else:
        lc=str.split('.')
        for i in lc:
                if i.isalpha() == True:
                        dech.append(i)
                else:
                        denum.append(i)
ans=''
print(denum)
print(dech)
for de in dech:
        dord=ord(de)
        index=dech.index(de)
        if denum=='':
                break
        if c==',':
                diff=dord-int(denum[index])
        else:
                diff=dord+int(denum[index])
        
        ans+=chr(diff)

print(ans)
        
"""
                
