def calc(a,b):
    c=a-b
    return c
a,b=input().split(" ")
c=int(a)
d=int(b)

if calc(c,d)>0:
    print('>')
elif calc(c,d)<0:
    print('<')
else:
    print('==')

