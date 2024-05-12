n = int(input())
country_stamps = [input() for _ in range(n)]
distinct_stamp = set()
for stamp in country_stamps:
    distinct_stamp.add(stamp)
print(len(distinct_stamp))