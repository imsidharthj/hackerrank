def split_and_join(line):
    line_split = []
    line_split = line.split(" ")
    line_join = "-".join(line_split)
    return line_join
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)