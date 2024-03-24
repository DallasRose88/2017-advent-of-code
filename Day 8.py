f = open('trial.txt','r')

maxs = []
nodes = {}
for line in f:
    split= line.split(' ')
    if split[0] not in nodes:
        nodes[split[0]] = 0 
    if split[4] not in nodes:
        nodes[split[4]] = 0
    if split[5] == '<':
        if (nodes[split[4]]) < int(split[6]):
            if split[1] == 'inc':
                nodes[split[0]] += int(split[2])
            if split[1] == 'dec':
                nodes[split[0]] -= int(split[2])
    if split[5] == '>':
        if (nodes[split[4]]) > int(split[6]):
            if split[1] == 'inc':
                nodes[split[0]] += int(split[2])
            if split[1] == 'dec':
                nodes[split[0]] -= int(split[2])
    if split[5] == '>=':
        if (nodes[split[4]]) >= int(split[6]):
            if split[1] == 'inc':
                nodes[split[0]] += int(split[2])
            if split[1] == 'dec':
                nodes[split[0]] -= int(split[2])
    if split[5] == '==':
        if (nodes[split[4]]) == int(split[6]):
            if split[1] == 'inc':
                nodes[split[0]] += int(split[2])
            if split[1] == 'dec':
                nodes[split[0]] -= int(split[2])
    if split[5] == '<=':
        if (nodes[split[4]]) <= int(split[6]):
            if split[1] == 'inc':
                nodes[split[0]] += int(split[2])
            if split[1] == 'dec':
                nodes[split[0]] -= int(split[2])
    if split[5] == '!=':
        if (nodes[split[4]]) != int(split[6]):
            if split[1] == 'inc':
                nodes[split[0]] += int(split[2])
            if split[1] == 'dec':
                nodes[split[0]] -= int(split[2])
    maxs.append(max(nodes.values()))
        

print('part 1=',max(nodes.values()))
print('Part 2=',max(maxs))
