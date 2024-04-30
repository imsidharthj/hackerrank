if __name__ == '__main__':
    while True:
        try:
            n = input("")
        except EOFError:
            break
    arr = [int(i) for i in n.split()]
    arr.sort(reverse=True)
    runner_up_score = ""
    for score in arr:
        if score < arr[0]:
            runner_up_score = score
            break
    print(runner_up_score)