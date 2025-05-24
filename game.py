'''1 for snake
-1 for waterr
o for gun'''
import random
list=[1,-1,0]
computer = random.choice(list)
num=computer
youstr = input("enter your choice")
youDict = {"s":1, "w":-1, "g":0}
you =youDict[youstr]
print("computer =", computer)
if (computer== -1 and you==1):
    print("you win")
elif(computer==-11 and you == 0):
    print("you lost")

elif(computer==1 and you == -1):
    print("you lost")
elif(computer==1 and you == 1):
    print("you win")
elif(computer==0 and you == -1):
    print("you win")
elif(computer==0 and you == 1):
    print("you lost")
else: (print ("sthg went wrong"))