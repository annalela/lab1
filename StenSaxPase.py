import random


def func():
    stensaxpase = ['sten', 'sax', 'påse']
    return random.choice(stensaxpase)

def func2(spelarval, datorval):
    if spelarval == datorval:
        print('Oavgjort! Ny omgång.')
    elif spelarval == 'sten':
        if datorval == 'sax':
            print('Sten är bättre än sax, du vann! Applåder!')
        else: 
            print('Påse är bättre än sten. Ledsen men datorn vann.')
    elif spelarval == 'sax':
        if datorval == 'påse':
            print('Sax är bättre än påse, du vann! Applåder!')
        else: 
            print('Sten är bättre än sax. Ledsen men datorn vann.')
    elif spelarval == 'påse':
        if datorval == 'sten':
            print('Påse är bättre än sten, du vann! Applåder!')
        else: 
            print('Sax är bättre än påse. Ledsen men datorn vann.') 

while True:            
    datorval = func()
    spelarval = input('Välj sten, sax eller påse ')

    print('Du valde', spelarval)
    print('Datorn valde', datorval)

    func2(spelarval, datorval)
    
    if spelarval != datorval:
        break
    