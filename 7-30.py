def f(n):
  if n == 1:
    return 1
  return n + f(n - 1)

def main():
  tests = [
    10
  ]
  for test in tests:
    print(f'f({test}) returns {f(test)}')



if __name__ == "__main__":
  main()
