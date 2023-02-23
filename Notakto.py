# Check the current status of the moving
# 判断当下步骤的状况
def pan(givenlist,k):
    r=1
    if k==1:
        g=givenlist[1]
    elif k==2:
        g=givenlist[2]
    elif k==3:
        g=givenlist[3]
    for i in range(0,8,3):
        for j in range(1,3):
            if g[i]!=g[i+j]:
                break
            elif j==2:
                r=0
    if r!=0:
        for i in range(0,3):
            for j in range(1,3):
                if g[i]!=g[i+3*j]:
                    break
                elif j==2:
                    r=0
    if r!=0:
        if g[0]==g[4] and g[0]==g[8]:
            r=0
    if r!=0:
        if g[2]==g[4] and g[2]==g[6]:
            r=0
    return r

def p():
    si=0
    for i in range(1,4):
        if situation[i]==1:
            si+=1
    t=0
    for i in range(1,4):
        if situation[i]==1 and t<si-1:
            print(title[i]+'      ',end='')
            t+=1
        elif situation[i]==1 and t==si-1:
            print(title[i])
    t=0
    for k in range(0,3):
        t=0
        for i in range(1,4):
            if situation[i]==1:
                for j in range(0,3):
                    if t<3*si-1:
                        print(d[i][3*k+j],end=' ')
                        t+=1
                    elif t==3*si-1:
                        print(d[i][3*k+j])
                    if j==2 and t<3*si-1:
                        print(' ',end='')

def cal(fi,se,th,fo):
    for i in range(6):
        if fi>=2:
            fi-=2
        if  se>=3:
            se-=2
        if se>=2 and th>=1:
            se-=2
        if th>=3:
            th-=1
            fi+=1
        if se>=2 and fo>=1:
            se-=2
        if th>=1 and fo>=1:
            th-=1
            fi+=1
        if fo>=2:
            fo-=2
            th+=2
    ss='a'*fi+'b'*se+'c'*th+'d'*fo
    if fi==0 and se==0 and th==0 and fo==0:
        ss='lose'
    return ss

def result(first,second,third):
    l1=[0,0,0,0]
    l2=[first,second,third]
    for i in l2:
        if i=='one':
            continue
        elif i=='a':
            l1[0]+=1
        elif i=='b':
            l1[1]+=1
        elif i=='c':
            l1[2]+=1
        elif i=='d':
            l1[3]+=1
        elif i=='cc':
            l1[2]+=2
        elif i=='ab':
            l1[0]+=1
            l1[1]+=1
        elif i=='ad':
            l1[0]+=1
            l1[3]+=1
    sss=cal(l1[0],l1[1],l1[2],l1[3])
    return sss

def turn(x):
    g=[0 for i in range(9)]
    g[0],g[1],g[2],g[3],g[4],g[5],g[6],g[7],g[8]=x[2],x[5],x[8],x[1],x[4],x[7],x[0],x[3],x[6]
    return g

def chazhao(x):
    put=0
    for i in range(len(onelist)):
        if onelist[i]==x:
            put='one'
            return put
    for i in range(len(alist)):
        if alist[i]==x:
            put='a'
            return put
    for i in range(len(blist)):
        if blist[i]==x:
            put='b'
            return put
    for i in range(len(dlist)):
        if dlist[i]==x:
            put='d'
            return put
    for i in range(len(ablist)):
        if ablist[i]==x:
            put='ab'
            return put
    for i in range(len(adlist)):
        if adlist[i]==x:
            put='ad'
            return put
    return put
            
def reset(x,y):
    x1=x[:]
    if situation[y]==0:
        return 'one'
    elif x1.count('X')==0:
        return 'c'
    elif x1.count('X')==1 and x1[4]=='X':
        return 'cc'
    for i in range(4):
        chu=[]
        for j in range(9):
            if x1[j]=='X':
                chu.append(j)
        s1s=chazhao(chu)
        if s1s!=0:
            return s1s
        x1=turn(x1)

def ai():
    a1,b1,c1=a[:],b[:],c[:]
    a2,b2,c2=a[:],b[:],c[:]
    re=[0,0,0]
    re[0]=reset(a2,1)
    re[1]=reset(b2,2)
    re[2]=reset(c2,3)
    if situation[1]==1:
        for i in range(9):
            if a1[i]!='X':
                a1[i]='X'
                d1=[0,a1,0,0]
                if pan(d1,1)==0:
                    rere='one'
                else:
                    rere=reset(a1,1)
                ss=result(rere,re[1],re[2])
                if ss=='a' or ss=='bb' or ss=='bc' or ss=='cc':
                    return 'A'+str(i)
                a1[i]=a2[i]
    if situation[2]==1:
        for i in range(9):
            if b1[i]!='X':
                b1[i]='X'
                d1=[0,0,b1,0]
                if pan(d1,2)==0:
                    rere='one'
                else:
                    rere=reset(b1,2)
                ss=result(re[0],rere,re[2])
                if ss=='a' or ss=='bb' or ss=='bc' or ss=='cc':
                    return 'B'+str(i)
                b1[i]=b2[i]
    if situation[3]==1:
        for i in range(9):
            if c1[i]!='X':
                c1[i]='X'
                d1=[0,0,0,c1]
                if pan(d1,3)==0:
                    rere='one'
                else:
                    rere=reset(c1,3)
                ss=result(re[0],re[1],rere)
                if ss=='a' or ss=='bb' or ss=='bc' or ss=='cc':
                    return 'C'+str(i)
                c1[i]=c2[i]

onelist=[[0],[1],[0,5,7]]
alist=[[0,8],[1,3],[1,7],[0,2,4],[0,2,7],[0,4,5],[0,1,6],[0,1,3,4],[0,1,3,5],[0,1,3,8],[0,1,7,8],[0,2,6,8],[1,3,5,7],[0,1,4,5,6],[0,1,5,6,7],[0,1,5,6,8],[0,1,3,5,7,8],[1,2,8],[2,3,4],[1,2,3,5],[1,2,6,7],[1,2,3,4,8]]
blist=[[0,2],[0,4],[0,5],[1,4],[0,1,3],[1,3,5],[0,1,4,5],[0,1,4,6],[0,1,5,6],[0,1,6,7],[0,1,6,8],[0,2,4,7],[0,4,5,7],[0,1,3,5,7],[0,1,3,5,8],[2,3],[1,2,3,4],[1,2,4,8],[1,2,3,8],[1,2,7,8],[1,2,6,8],[1,2,3,5,6]]
cclist=[[4]]
dlist=[[0,1,5],[0,1,7],[0,1,8],[1,2,3],[1,2,7],[1,2,6]]
ablist=[[0,1,4],[0,2,6],[1,3,4],[0,1,5,7],[0,1,5,8],[1,2,4],[1,2,3,7]]
adlist=[[0,1],[1,2]]

a=[0,1,2,3,4,5,6,7,8]
b=[0,1,2,3,4,5,6,7,8]
c=[0,1,2,3,4,5,6,7,8]
situation=[0,1,1,1]
title=[0,'A','B','C']
d=[0,a,b,c]
total=3
time=1
p()

while total>0:  
    if time%2==1:
        gude=ai()
        s=str(gude)
        print('Player 1:',s)
    else:
        s=str(input('Player 2: '))

    if len(s)!=2:
        print('Invalid move, please input again')
        continue
    else:
        n=ord(s[0])-64
        t=0
        if n<1 or n>3:
            print('Invalid move, please input again')
            continue
    
    if situation[n]==1 and ord(s[1])>=48 and ord(s[1])<=56:
        t=int(s[1])
        if d[n][t]!='X':
            d[n][t]='X'
        else:
            print('Invalid move, please input again')
            continue
    else:
        print('Invalid move, please input again')
        continue
    
    if pan(d,n)==0:
        situation[n]=0
        total-=1
    p()
    time+=1


if time%2==0:
    print('Player 2 wins game')
else:
    print('Player 1 wins game')
