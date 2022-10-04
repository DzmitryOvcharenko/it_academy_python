print("enter sentence")
sentence = input()
import re
sentences = re.findall("([a-z]|[A-Z])", sentence)
bigl=0
lowl=0
for a in sentences :
    if (a.isupper()) == True :
        bigl += 1
    elif (a.islower()) == True :
        lowl += 1
print("big letters -", bigl)
print("low letters -", lowl)




