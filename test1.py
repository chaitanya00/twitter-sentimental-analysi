a=open('D:/AFINN-96.txt')
data=a.readlines()
b=' '.join(data)
c=b.split('\t')
d=' '.join(c)
e=d.split('\n')
h={}
f=' '.join(e)
g=f.split()
len(g)
for i in range(0,2976):
    if(i%2==0):
        h[g[i]]=g[i+1]
        
m=open('D:/clean_ElectionGujrat2017.txt')
o=m.readlines()
p=' '.join(o)
q=p.split('|')
c1=0
pp=[]
rr=[]
for i in q:
    c1=c1+1
    pp=i.split()
    for kk in pp:
        if(kk=='+0000'):
            rr.append(c1+2)
            
len(rr)
r=[]
for i in rr:
    r.append(q[i-1])
    
list=[]
for i in r:
    z=i.split()
    s=0
    for key in z:
        try:
            temp=h[key]
            s=s+int(temp)
        except:    
            s=s+0
    list.append(s)
    
ld=[]
c2=0
ldd=[]
for i in q:
    c2=c2+1
    ld=i.split()
    for kk in ld:
        if(kk=='+0000'):
            ldd.append(c2+5)
            
ldd[0:5]
ss=0
ll=0
for i in ldd:
    if(q[i-1]<0 and list[ll]<0):
        ss=ss+1
    elif(q[i-1]>0 and list[ll]>0):    
        ss=ss+1
    elif(q[i-1]==0 and list[ll]==0):   
        ss=ss+1
    ll=ll+1
    
ss=0
for i in ldd:
    if(q[i-1]<0 and list[ll]<0):
        ss=ss+1
    elif(q[i-1]>0 and list[ll]>0):    
        ss=ss+1
    elif(q[i-1]==0 and list[ll]==0):   
        ss=ss+1
    ll=ll+1