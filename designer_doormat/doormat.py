def main():
  n, m = map(int, input().split())
  design_doormat(n, m)

def design_doormat(n, m):
  c = ".|."
  for i in range(1, n, 2):
    print((c * i).center(m, '-'))

  print('WELCOME'.center(m, '-'))

  for i in range(n-2, 0, -2):
    print((c * i).center(m, '-'))

main()