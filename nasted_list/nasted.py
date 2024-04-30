if __name__ == '__main__':
    n = int(input())
    records = []
    for _ in range(n):
        name = input()
        score = float(input())
        records.append([name, score])
    scores = sorted(score for name, score in records)
    second_lowest_score = scores[1]
    students_with_second_lowest = [name for name, score in records if score == second_lowest_score]
    students_with_second_lowest.sort()
    for student in students_with_second_lowest:
        print(student)
