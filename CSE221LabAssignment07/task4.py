import math
input=open("input4.txt","r")
output=open("output4.txt","w")
a=input.readline().split()
num=int(a[0])
target=int(a[1])
denom=input.readline().strip().split()
lst=[]

for i in range(num):
    lst.append(int(denom[i]))

table=[[0]*(target+1) for i in range (num)]

def denom_tab(table,lst):
    for i in range (len(table)): 
        coin = lst[i]
        tab = table[i]
   
        for j in range (len(tab)):
            if i<1:
                if coin == 1:
                    tab[j]=j
                else:
                    if j%coin != 0:
                        tab[j]=math.inf
                    else:
                        tab[j]=j//coin
            else:
                if j<coin:
                    tab[j]=table[i-1][j]
                else:
                    tab[j]=min(table[i-1][j],1+tab[j-coin])
                
output.write(str(table[-1][-1]))