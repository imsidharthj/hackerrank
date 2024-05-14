if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n_a = int(input())
        a = set(map(int, input().split()))
        n_b = int(input())
        b = set(map(int, input().split()))
        '''
        is_subset = True
        for i in a:
            if i not in b:
                is_subset = False
                break
        if is_subset:
            print(True)
        else:
            print(False)
        '''
        is_sunset = a.issubset(b)
        print(is_sunset)