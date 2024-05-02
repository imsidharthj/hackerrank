import re
def main():
    T = int(input())
    for _ in range(T):
        S = input().strip()
        result = valid_regex(S)
    print(result)

def valid_regex(S):
    try:
        re.compile(S)
        return True
    except re.error:
        return False
    
if __name__ == "__main__":
    main()