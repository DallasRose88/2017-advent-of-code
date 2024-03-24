f = open('code','r')

names = []
reps = []
for line in f:
    rem = line.replace(',','')
    split = rem.strip().split(' ')
    if len(split) > 2:
        names.append(split[0])
        m = 3
        while m < len(split):
            reps.append(split[m])
            m += 1

for r in reps:
    if r in names:   
        names.remove(r)

        
print('part 1 =',names)
