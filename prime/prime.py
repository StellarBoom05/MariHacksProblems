x=input()
y=int(x)
j=1
for i in range(y-2):
    if y%(i+2)==0:
        j="yes"
    else:
        k="no"
if j=="yes":
    print("false")
else:
    print("true")
