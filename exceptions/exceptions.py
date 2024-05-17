t = int(input())
results = []
for _ in range(t):
    try:
        a, b = input().split()
        division = int(a) // int(b)
        results.append(division)
    except ZeroDivisionError as e:
        results.append(f"Error Code: {e}")
    except ValueError as e:
        results.append(f"Error Code: {e}")
for result in results:
    print(f"{result}")