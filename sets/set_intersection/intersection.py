n1 = int(input())
set1 = set(map(int, input().split()))
n2 = int(input())
set2 = set(map(int, input().split()))
intersection_set = set2.intersection(set1)
print(len(intersection_set))