import random
n=random.randint(1,10)
a=-1
guess=1
while (a!=n):
    a=int(input("Guess the number: "))
    if(a>n):
        print("Enter lower number: ")
        guess+=1
    elif(a<n):
        print("Enter higher number: ")
        guess+=1
print(f"You guessed a correct number in {guess} attempt.")