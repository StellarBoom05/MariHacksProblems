txt = input()
txt = txt.lower()
#print (txt)
y =txt[::-1].lower()
#print(y)

if y == txt:
    print("true")
else:
    print("false")
