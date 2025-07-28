numbers = input()
y=numbers.split(", ")
y = [int(number) for number in y]

#for number in y:
#    number
a = sorted(y)
#print(a)
a.reverse()
#z=a.split(",")
printed = False
for i in range(len(a)):
    if i == len(a) - 1:
        break
    elif a[i] == a[i+1]:
        continue
    else:
        print(a[i+1])
        printed = True
        break
if printed == False:
    print("The second largest number does not exist in this array.")

