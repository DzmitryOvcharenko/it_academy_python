print('enter santence')
s=input()
s=str(s)
s1=s.replace(' ','')
st=[]
for a in s1 :
    if not a in st :
        st += a
print(''.join(st))
