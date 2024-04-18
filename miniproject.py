import random

target=random.randint(1,100)

while True:
    userchoice=int(input('guess the target or Q:'))
    if(userchoice=='Q'):
        break

    userchoice=int(userchoice)
    if(userchoice==target):
        print('success: correct guess!!')
        break
    elif(userchoice < target):
        print('your choice is too small. take a bigger guess')
    
    else:
        print('your choice is too big. take a smaller guess')

print('-----GAME OVER-----')