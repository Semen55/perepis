f=open('Perepis.txt','r')
ch=int()
print('a)')
for i in f:
    s=str(i)
    if int(s[s.rfind('.')+1:s.rfind('\n')])<1978:
        print(s[:s.find(' '):])
        ch+=1
print(ch)
print('б)')
d1=int(input())
d2=int(input())
f.seek(0,0)
for i in f:
    s=str(i)
    if (int(s[s.rfind('.')+1:s.rfind('\n')])<d1) and (int(s[s.rfind('.')+1:s.rfind('\n')])>d2):
        print(s[:s.rfind('  '):],s[s.rfind('.')+1:s.rfind('\n')])

