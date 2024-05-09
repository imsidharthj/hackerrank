import string
def print_rangoli(size):
    n = size
    width = 4 * n - 3
    alphabet = list(string.ascii_lowercase)
    for i in range(1, n+1):
        print(("-".join(alphabet[n-1:n-i:-1] + alphabet[n-i:n])).center(width, "-"))
    for i in range(n-1, 0, -1):
        print(("-".join(alphabet[n-1:n-i:-1] + alphabet[n-i:n])).center(width, "-"))

if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)