import re
def main():
    results = []
    T = int(input())
    for _ in range(T):
        S = input().strip()
        results.append(valid_regex(S))
    print("\n".join(map(str, results)))

def valid_regex(S):
    try:
        re.compile(S)
        return True
    except re.error:
        return False
    
if __name__ == "__main__":
    main()