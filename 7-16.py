def f(n):
  if n == 1:
    return 0
  if n == 2:
    return 1
  return f(n - 1) + f(n - 2)

def main():
  tests = [
    5, 9
  ]
  for test in tests:
    print(f'f({test}) returns {f(test)}')



if __name__ == "__main__":
  main()
