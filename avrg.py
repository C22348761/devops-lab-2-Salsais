
a = input("insert a list of numbers space separated: ")

a = a.split()
# print(a)
avrg = 0

for i in a:    
    avrg += int(i)

avrg /= len(a)
print("Updated")
print(avrg)


