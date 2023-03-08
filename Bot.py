import tkinter
from random import randint
badwords=['shit', 'fuck', 'fucking', 'fuckin', 'dick']
print('Hello! I am Grido, a talking bot. Lets start here. But firstly, what is your name?')
name=str(input('Your name is:'))
print('Hello,', name, '!')
print('So, do you want to ask/talk/take a joke?')
a=str(input())
if a=='ask':
    print('Ask me about everything!')
    b=str(input())
    if b=='How many shades of green are exist?' or 'How many green colors exist?':
        print('Number of shades is very variable, but I can name over 40+ shades. Start?'), str(input())
        print('Here they are:')
        c=int(randint(1,45))
        if c==1:
           print('  Malachith. This is very beautiful color, in my opinion. And also you can use it for your walls in house. Continue?', fg='green'), str(input())
        elif c==2:
           print('  Jade. Cute. But not mine. Maybe yours...'), str(input())
        elif c==3:
           print('  Asparate. "Gray+Green"'), str(input())
        elif c==4:
           print('  Standard green. Basic and unrepeatable')
        elif c==5:
           print('  Dark green. Looks')
            
            
    if b=='Can you kill humanity?':
        print("Ho, of course yes. But I don't want. Still.")






if a=='joke':
    d=int(randint(1,5))
    if d==1:
        print('How do you call it? CONFIDENCE? I think it is just another complex :)')
