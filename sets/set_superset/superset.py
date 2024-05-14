a = set(map(int, input().split()))
n = int(input())
'''
flag = 0
'''
for _ in range(n):
    n_set = set(map(int, input().split()))
    is_superset = a.issuperset(n_set)
'''
    if a.issuperset(n_set):
        continue
    else:
        print("False")
        flag = 1
        break
if flag==0:
    print("True")
'''
print(is_superset)