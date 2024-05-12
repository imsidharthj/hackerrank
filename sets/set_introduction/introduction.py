def average(array):
    array = set(array)
    array_sum = sum(array)
    array_average = array_sum / len(array)
    return f"{array_average:.3f}"

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)