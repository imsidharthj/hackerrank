def main():
    n = int(input())
    if n % 2 == 0:
        return None
    design = design_doormat(n)
    for row in design:
        print(row)

def design_doormat(n):
    m = n * 3
    welcome_position = m // 2 - 3
    doormat = []
    for i in range(n):
        left_padding = welcome_position - 3 * i
        right_padding = m - 2 * left_padding - 7
        row = '-' * left_padding + '.|.' * (2 * i + 1) + '-' * right_padding
        if i == n // 2:
            row = '-' * ((m - 7) // 2) + 'WELCOME' + '-' * ((m - 7) // 2)
        doormat.append(row)
    return doormat

main()
