s = input()
stack = []
good = True
for i in s:
    if  i in '({[':
       stack.append(i)
    elif i in ')}]' :
        if not stack:
            good = False
            break
        a = stack.pop()
        if a == '(' and i==')' :
           continue
        if a == '[' and i ==']':
               continue
        if a == '{' and i =='}':
                   continue
        good = False
        break
if good and len(stack)==0 :
    print('правильная последовательность')
else:
    print('неправильная последовательность')


