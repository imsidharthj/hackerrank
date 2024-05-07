def main():
    n = int(input())
    print_formatted(n)

def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(f"{i:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")

main()