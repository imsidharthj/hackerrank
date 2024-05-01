if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total_marks = sum(student_marks[query_name])
    number_marks = len(student_marks[query_name])
    average = total_marks / number_marks
    print(f"{average:.2f}")