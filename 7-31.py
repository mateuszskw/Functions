def f(number, n):
  if n == 1:
    return number
  return number * f(number, n - 1)

def main():
  tests = [
    (5, 3)
  ]
  for test in tests:
    print(f'f({test}) returns {f(*test)}')



if __name__ == "__main__":
  main()
