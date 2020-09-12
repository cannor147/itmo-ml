n, m, k = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

classes = [[] for i in range(m)]
parts = [[] for i in range(k)]

for i, v in enumerate(c):
    classes[v - 1].append(i)

s = 0
for i in range(m):
    l = len(classes[i])
    for j in range(l):
        parts[s % k].append(classes[i][j])
        s += 1
        
for part in parts:
    print(len(part), end = " ")
    for el in part:
        print(el + 1, end = " ")
    print()