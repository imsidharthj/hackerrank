n1 = int(input())
s = set(map(int, input().split()))
n2 = int(input())
for _ in range(n2):
    command = list(input().split())
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    else:
        s.discard(int(command[1]))
sum = 0
for i in s:
    sum = sum + i
print(sum)