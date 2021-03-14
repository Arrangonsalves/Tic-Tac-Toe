import os
l=['-','-','-','-','-','-','-','-','-']
flag=0
def des():
    print('               ','-'*21)
    print('              ','|''      ''|''      ''|''      ''|')
    print('              ','|''      ''|''      ''|''      ''|')
    print('              ','|''  %s   ''|''  %s   ''|''  %s   ''|'%(l[0],l[1],l[2]))
    print('              ','|''  1   ''|''  2   ''|''  3   ''|')
    print('              ','|''      ''|''      ''|''      ''|')
    print('               ','-'*21)
    print('              ','|''      ''|''      ''|''      ''|')
    print('              ','|''      ''|''      ''|''      ''|')
    print('              ','|''  %s   ''|''  %s   ''|''  %s   ''|'%(l[3],l[4],l[5]))
    print('              ','|''  4   ''|''  5   ''|''  6   ''|')
    print('              ','|''      ''|''      ''|''      ''|')
    print('               ','-'*21)
    print('              ','|''      ''|''      ''|''      ''|')
    print('              ','|''      ''|''      ''|''      ''|')
    print('              ','|''  %s   ''|''  %s   ''|''  %s   ''|'%(l[6],l[7],l[8]))
    print('              ','|''  7   ''|''  8   ''|''  9   ''|')
    print('              ','|''      ''|''      ''|''      ''|')
    print('               ','-'*21)
des()
def win():
        global flag
        if(l[0]=='X' and l[1]=='X' and l[2]=='X'):
            print('Player one wins')
            flag=1
        elif(l[0]=='O' and l[1]=='O' and l[2]=='O' ):
            print('Player two wins')
            flag=1
        elif(l[3]=='X' and l[4]=='X' and l[5]=='X' ):
            print('Player one wins')
            flag=1
        elif(l[3]=='O' and l[4]=='O' and l[5]=='O' ):
            print('Player two wins')
            flag=1
        elif(l[6]=='X' and l[7]=='X' and l[8]=='X' ):
            print('Player one wins')
            flag=1
        elif(l[6]=='O' and l[7]=='O' and l[8]=='O' ):
            print('Player two wins')
            flag=1
        elif(l[0]=='X' and l[3]=='X' and l[6]=='X' ):
            print('Player one wins')
            flag=1
        elif(l[0]=='O' and l[3]=='O' and l[6]=='O' ):
            print('Player two wins')
            flag=1
        elif(l[1]=='X' and l[4]=='X' and l[7]=='X' ):
            print('Player one wins')
            flag=1
        elif(l[1]=='O' and l[4]=='O' and l[7]=='O' ):
            print('Player two wins')
            flag=1
        elif(l[2]=='X' and l[5]=='X' and l[8]=='X' ):
            print('Player one wins')
            flag=1
        elif(l[2]=='O' and l[5]=='O' and l[8]=='O' ):
            print('Player two wins')
            flag=1
        elif(l[0]=='X' and l[4]=='X' and l[8]=='X' ):
            print('Player one wins')
            flag=1
        elif(l[0]=='O' and l[4]=='O' and l[8]=='O' ):
            print('Player two wins')
            flag=1
        elif(l[2]=='X' and l[4]=='X' and l[6]=='X' ):
            print('Player one wins')
            flag=1
        elif(l[2]=='O' and l[4]=='O' and l[6]=='O' ):
            print('Player two wins')
            flag=1
        
for p in range(1,10):
    if(p%2==0):
        print('Player 2 turn')  
        x=int(input('Enter the position '))
        if(x==1 and l[0]=='-'):
            l[0]='O'
            win()
            if(flag==1):
             break
        elif(x==2 and l[1]=='-'):
            l[1]='O'
            win()
            if(flag==1):
              break
        elif(x==3 and l[2]=='-'):
            l[2]='O'
            win()
            if(flag==1):
              break
        elif(x==4 and l[3]=='-'):
            l[3]='O'
            win()
            if(flag==1):
              break
        elif(x==5 and l[4]=='-'):
            l[4]='O'
            win()
            if(flag==1):
              break
        elif(x==6 and l[5]=='-'):
            l[5]='O'
            win()
            if(flag==1):
              break
        elif(x==7 and l[6]=='-'):
            l[6]='O'
            win()
            if(flag==1):
              break
        elif(x==8 and l[7]=='-'):
            l[7]='O'
            win()
            if(flag==1):
              break
        elif(x==9 and l[8]=='-'):
            l[8]='O'
            win()
            if(flag==1):
              break
        else:
            print('Space is occupied,therefore your chance is skipped')
            continue
    else:
        print('Player 1 turn')
        x=int(input('Enter the position '))
        if(x==1 and l[0]=='-'):
            l[0]='X'
            win()
            if(flag==1):
              break
        elif(x==2 and l[1]=='-'):
            l[1]='X'
            win()
            if(flag==1):
              break
        elif(x==3 and l[2]=='-'):
            l[2]='X'
            win()
            if(flag==1):
              break
        elif(x==4 and l[3]=='-'):
            l[3]='X'
            win()
            if(flag==1):
              break
        elif(x==5 and l[4]=='-'):
            l[4]='X'
            win()
            if(flag==1):
              break
        elif(x==6 and l[5]=='-'):
            l[5]='X'
            win()
            if(flag==1):
              break
        elif(x==7 and l[6]=='-'):
            l[6]='X'
            win()
            if(flag==1):
              break
        elif(x==8 and l[7]=='-'):
            l[7]='X'
            win()
            if(flag==1):
              break
        elif(x==9 and l[8]=='-'):
            l[8]='X'
            win()
            if(flag==1):
              break
        else:
            print('Space is occupied ,therefore your chance is skipped')
            continue
    des()
if(flag==1):
    des()



