A = []
for i in range(1,27):
    A.append(i)
B = list(map(chr, range(ord('A'), ord('Z') + 1)))
dictAB = dict(zip(A,B))
print(dictAB)