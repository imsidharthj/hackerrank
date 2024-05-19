n,x = map(int, input().split())
exter_list = []
for i in range(x):
    marks = map(float, input().split())
    exter_list.append(marks)
zip_list = zip(*exter_list)
for i in zip_list:
    total = sum(i)
    average = total / x
    print(f"{average:.1f}")