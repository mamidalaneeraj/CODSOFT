import random
print('welcome to rock paper scissor game')
print('----------------------------------')
print('important instructions')
print('''you win if
      1) rock over scissor
      2) paper over rock
      3) scissorover paper
      you will lose except for above condition and tie conditions
''')
while(True):
    # prompting user to select the option
    print('enter r for rock,s for scissor,p for paper')
    you=input('enter the choice ')
    
    # using random module to choose randomly
    if (you=='r' or you=='p' or you=='s'):
        computer=random.choice(['r','p','s'])
        
        # to print if result is tie
        if you==computer:
            print(f'Its tie! because you and computer choose {computer}')
            
        # winning condition     
        elif (you=='r' and computer=='s') or (you=='p' and computer=='r') or (you=='s' and computer=='p' ):
            print(f'you won! because you choose {you} and computer choose {computer} ')
            
        # losing codition    
        else:
            print(f'you lose! because you choose {you} and computer choose {computer}')
            
        # replay    
        choice=input('Do you want to play again(yes/no) ') .lower()
        if choice!='yes':
            break
    else:
        print('Invalid choice! please enter valid choice')
print('thanks for playing')