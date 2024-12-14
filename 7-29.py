def f(n):
  if n==0 or n==1:
    return 1
  return n * f(n-1)


def main():
  tests = [
    5
  ]
  for test in tests:
    print(f'f({test}) returns {f(test)}')



if __name__ == "__main__":
  main()
