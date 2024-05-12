n1 = int(input())
set_a = set(map(int, input().split()))
n2 = int(input())
for _ in range(n2):
    set_command = input().split()
    set_b = set(map(int, input().split()))
    if set_command[0] == "intersection_update":
        set_a.intersection_update(set_b)
    elif set_command[0] == "update":
        set_a.update(set_b)
    elif set_command[0] == "symmetric_difference_update":
        set_a.symmetric_difference_update(set_b)
    else:
        set_a.difference_update(set_b)
print(sum(set_a))