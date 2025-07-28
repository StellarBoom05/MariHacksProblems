x=input()
s = input()
k=int(s)
y=list(x)
p=[]
if k>=0:
    if k<=26:
        for i in y:
            if i.isalpha():
                if i.isupper():
                    if (ord(i)+k)>90:
                        i=chr((ord(i)+k)-26)
                        p+=[i]
                        #print(p)
                        continue
                    else:
                        i=chr(ord(i)+k)
                        p+=[i]
                       # print(p)
                elif i.islower():
                    if 122<(ord(i)+ k):
                        i=chr((ord(i)+k)-26)
                        p+=[i]
                       # print(p)
                        continue
                    else:
                        i=chr(ord(i)+k)
                        p+=[i]
            else:
                p+=[" "]
    else:
        k -=26
        for i in y:
            if i.isalpha():
                if i.isupper():
                    if (ord(i)+k)>90:
                        i=chr((ord(i)+k)-26)
                        p+=[i]
                        #print(p)
                        continue
                    else:
                        i=chr(ord(i)+k)
                        p+=[i]
                        #print(p)
                elif i.islower():
                    if 122<(ord(i)+ k):
                        i=chr((ord(i)+k)-26)
                        p+=[i]
                        #print(p)
                        continue
                    else:
                        i=chr(ord(i)+k)
                        p+=[i]
            else:
                p+=[" "]
#negative k :(
else:
    if k>=-26:
        for i in y:
            if i.isalpha():
                if i.isupper():
                    if (ord(i)+k)<65:
                        i=chr((ord(i)+k)+26)
                        p+=[i]
                        #print(p)
                        continue
                    else:
                        i=chr(ord(i)+k)
                        p+=[i]
                      # print(p)
                elif i.islower():
                    if (ord(i)+ k)<97:
                        i=chr((ord(i)+k)+26)
                        p+=[i]
                        #print(p)
                        continue
                    else:
                        i=chr(ord(i)+k)
                        p+=[i]
                       # print(p)
            else:
                p+=[" "]
    else:
        k +=26
        for i in y:
            if i.isalpha():
                if i.isupper():
                    if (ord(i)+k)<65:
                        i=chr((ord(i)+k)+26)
                        p+=[i]
                        #print(p)
                        continue
                    else:
                        i=chr(ord(i)+k)
                        p+=[i]
                        #print(p)
                elif i.islower():
                    if (ord(i)+ k)<97:
                        i=chr((ord(i)+k)+26)
                        p+=[i]
                        #print(p)
                        continue
                    else:
                        i=chr(ord(i)+k)
                        p+=[i]
            else:
                p+=[" "]
z="".join(p)
print(z)
