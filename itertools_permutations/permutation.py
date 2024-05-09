from itertools import permutations

s = input().split()
for i in s:
    if i.isalpha():
        s_list = list(sorted(i))
    else:
        k = i
k = int(k)
print(*list(map("".join, permutations(s_list, k))), sep="\n")