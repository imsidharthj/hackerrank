def print_rangoli(size):
    width = 4 * size - 3
    center = ord("a")
    lines = []
    for i in range(size):
        alphabets = '-'.join(chr(center + size - j - 1) for j in range(i + 1))
        line = alphabets[:-1] + alphabets[::-1]
        lines.append(line.center(width, '-'))
    print('\n'.join(lines + lines[:-1][::-1]))

if __name__=="__main__":
    size = int(input())
    print_rangoli(size)
