import random
print("!GUESS THE NUMBER!")
num=random.randint(0,100)
count=0
while(True):
    n=int(input("Enter a number: "))
    if(n>num):
        print("The number is lesser than the entered number")
        count+=1
    elif(n<num):
        print("The number is greater than the entered number")
        count+=1
    else:
        print("Congratulations you won")
        count+=1
        break

print(f"you have guessed the number in {count} attempts ")



