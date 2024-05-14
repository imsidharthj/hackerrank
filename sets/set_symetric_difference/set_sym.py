m = int(input())
m_list = [int(i) for i in input().split()]
m_set = set(m_list)
n = int(input())
n_set = set(map(int, input().split()))
sym_diff = m_set.symmetric_difference(n_set)
for i in sorted(sym_diff):
    i = str(i)
    print(i)