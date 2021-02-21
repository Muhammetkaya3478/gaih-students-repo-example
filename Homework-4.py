import random

def DisplayCurrentState():
    for i in currentState:
        print(i + ' ' , end='')
    
    print('\n')



def UpdateCurrentStete(userLetter):
    for i in range(len(colorlist)):
        if colorlist[i] == userLetter:
            currentState[i]=userLetter

def CheckGameOver():
    global wordguessed

    if colorlist == currentState:
        wordguessed  = True



listofcolors=['kırmızı','turuncu','sarı','yesil','mor','mavi']
color=random.choice(listofcolors)

colorlist=list(color)
currentState=['_']*len(colorlist)

wordguessed=False

while not wordguessed:
    DisplayCurrentState()
    userLetter = input('bir harf tahmin et: ')
    print()

    if userLetter in colorlist:
        if userLetter in currentState:
            print('Bu harfi zaten tahmin ettiniz.')
        else:
            UpdateCurrentStete(userLetter)
    else:
        print('Try again!')

    CheckGameOver()

DisplayCurrentState()
print('\n')
print('The color was ' + color)
print('Thanks for playing')