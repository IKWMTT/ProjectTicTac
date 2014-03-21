#-------------------------------------------------------------------------------
# Name:        TicTac
# Purpose:      I want a good mark
#
# Author:      IKWMTT
#
# Created:     20.03.2014
# Copyright:   (c) IKWMTT 2014
# Licence:     Ive got none
#-------------------------------------------------------------------------------

pole = []
for i in range(0,3):
    pole.append(["."]*3)
def print_pole (pole):
    for strk in pole:
        print " ".join(strk)
print_pole(pole)
turn = True
nturn = 0
vari=0
vari1=0
x_hod = []
def xturn(pole):
    print "Your turn"
    flag = False
    hod=[]
    while flag==False:
        x_row = int(raw_input("Row number:"))
        x_col = int(raw_input("Col number:"))
        if x_row not in range(3) or x_col not in range(3):
            print "Out of bounds.Try again."
        elif pole[x_row][x_col]=="X" or pole[x_row][x_col]=="0":
            print "You cant place X here.Try again."
        else:
            pole[x_row][x_col]="X"
            print_pole(pole)
            hod.append(x_row)
            hod.append(x_col)
            flag=True
            return hod
def oturn(pole,nturn,vari,x_hod):
    print "My turn"
    th = x_hod
    if nturn==1:
        if pole[1][1]!='X' and pole[1][1]!='0':
            pole[1][1]="0"
            print_pole(pole)
            return 0
        elif pole[0][0]!='X' and pole[0][0]!='0':
            pole[0][0]="0"
            print_pole(pole)
            return 0
    if nturn==3:
        if pole[1][1]=='X':
            if pole[2][2]=='X':
                pole[2][0]="0"
                print_pole(pole)
                return 1
            else:
                if th[0]==1:
                    pole[1][(th[1]+2)%4]="0"
                    print_pole(pole)
                    return th[1]
                elif th[1]==1:
                    pole[(th[0]+2)%4][1]="0"
                    print_pole(pole)
                    return th[0]
                else:
                    pole[(th[0]+2)%4][(th[1]+2)%4]="0"
                    print_pole(pole)
                    return 3
        if pole[1][1]=='0':
            if th[1]==1:
                if pole[th[0]][0]=='X':
                    pole[th[0]][2]='0'
                    print_pole(pole)
                    return 4
                elif pole[th[0]][2]=='X':
                    pole[th[0]][0]='0'
                    print_pole(pole)
                    return 4
                else:
                    pole[th[0]][0]='0'
                    print_pole(pole)
                    return 0

            elif th[0]==1:
                if pole[0][th[1]]=='X':
                    pole[2][th[1]]='0'
                    print_pole(pole)
                    return 4
                elif pole[2][th[1]]=='X':
                    pole[0][th[1]]='0'
                    print_pole(pole)
                    return 4
                else:
                    pole[0][th[1]]='0'
                    print_pole(pole)
                    return 0
            elif th[0]==0:
                if th[1]==2 or th[1]==0:
                    if pole[2][(th[1]+2)%4]=='X':
                        pole[2][1]='0'
                        print_pole(pole)
                        return 5
                if th[1]==2 or th[1]==0:
                    if pole[0][(th[1]+2)%4]=='X':
                        pole[0][1]='0'
                        print_pole(pole)
                        return 6
                    if pole[0][1]=='X':
                        pole[0][(th[1]+2)%4]='0'
                        print_pole(pole)
                        return 4
                    if pole[1][th[1]]=='X':
                        pole[2][th[1]]='0'
                        print_pole(pole)
                        return 4
                    if pole[2][th[1]]=='X':
                        pole[1][th[1]]='0'
                        print_pole(pole)
                        return 6
                    if pole[2][1]=='X':
                        pole[1][0]='0'
                        print_pole(pole)
                        return 0
                    if pole[1][2]=='X':
                        pole[0][1]='0'
                        print_pole(pole)
                        return 0
            elif th[0]==2:
                if th[1]==2 or th[1]==0:
                    if pole[0][(th[1]+2)%4]=='X':
                        pole[2][1]='0'
                        print_pole(pole)
                        return 5
                    if pole[2][(th[1]+2)%4]=='X':
                        pole[2][1]='0'
                        print_pole(pole)
                        return 6
                    if pole[2][1]=='X':
                        pole[2][(th[1]+2)%4]='0'
                        print_pole(pole)
                        return 4
                    if pole[1][th[1]]=='X':
                        pole[0][th[1]]='0'
                        print_pole(pole)
                        return 4
                    if pole[0][th[1]]=='X':
                        pole[1][th[1]]='0'
                        print_pole(pole)
                        return 6
                    if pole[0][1]=='X':
                        pole[1][2]='0'
                        print_pole(pole)
                        return 0
                    if pole[1][0]=='X':
                        pole[2][1]='0'
                        print_pole(pole)
                        return 0
    if nturn==5 or nturn==7:
        count=0
        finalr=0
        finalc=0
        for i in range(3):
            for j in range(3):
                if pole[i][j]=='0':
                    count+=1
                elif pole[i][j]=='X':
                    break
            if count==2:
                for j1 in range(3):
                    if pole[i][j1]=='.':
                        pole[i][j1]='0'
                        print_pole(pole)
                        return -1
            count=0
        for j in range(3):
            for i in range(3):
                if pole[i][j]=='0':
                    count+=1
                elif pole[i][j]=='X':
                    break
            if count==2:
                for i1 in range(3):
                    if pole[i1][j]=='.':
                        pole[i1][j]='0'
                        print_pole(pole)
                        return -1
            count=0
        for i in range(3):
            if pole[i][i]=='0':
                count+=1
            elif pole[i][i]=='X':
                break
            if count==2:
                for i1 in range(3):
                    if pole[i1][i1]=='.':
                        pole[i1][i1]='0'
                        print_pole(pole)
                        return -1
        count=0
        for i in range(3):
            if pole[i][2-i]=='0':
                count+=1
            elif pole[i][2-i]=='X':
                break
            if count==2:
                for i1 in range(3):
                    if pole[i1][2-i1]=='.':
                        pole[i1][2-i1]='0'
                        print_pole(pole)
                        return -1
        count=0







        for i in range(3):
            for j in range(3):
                if pole[i][j]=='X':
                    count+=1
                elif pole[i][j]=='0':
                    break
            if count==2:
                for j1 in range(3):
                    if pole[i][j1]=='.':
                        pole[i][j1]='0'
                        print_pole(pole)
                        return 0
            count=0
        for j in range(3):
            for i in range(3):
                if pole[i][j]=='X':
                    count+=1
                elif pole[i][j]=='0':
                    break
            if count==2:
                for i1 in range(3):
                    if pole[i1][j]=='.':
                        pole[i1][j]='0'
                        print_pole(pole)
                        return 0
            count=0
        for i in range(3):
            if pole[i][i]=='X':
                count+=1
            elif pole[i][i]=='0':
                break
            if count==2:
                for i1 in range(3):
                    if pole[i1][i1]=='.':
                        pole[i1][i1]='0'
                        print_pole(pole)
                        return 0
        count=0
        for i in range(3):
            if pole[i][2-i]=='X':
                count+=1
            elif pole[i][2-i]=='0':
                break
            if count==2:
                for i1 in range(3):
                    if pole[i1][2-i1]=='.':
                        pole[i1][2-i1]='0'
                        print_pole(pole)
                        return 0
        count=0
        if pole[0][0]!='X':
            pole[0][0]='0'
            print_pole(pole)
            return 0
        if pole[0][2]!='X':
            pole[0][2]='0'
            print_pole(pole)
            return 0
        if pole[2][2]!='X':
            pole[2][2]='0'
            print_pole(pole)
            return 0























while nturn<9:
    if nturn==8:
        print "Tie!"
        break
    if turn==True:
        x_hod=xturn(pole)
        turn=False
    else:
        vari1=oturn(pole,nturn,vari,x_hod)
        vari=vari1
        if vari==-1:
            nturn=9
            print "You lose!"
        turn=True
    nturn+=1

