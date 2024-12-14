def valid(x):
  return x % 2 == 0 and x % 3 == 0 and x % 4 != 0

def f(start, end):
  return sum(filter(valid, range(start, end + 1)))


def main():
  tests = [
    (1, 20), (10, 30)
  ]
  for test in tests:
    print(f'f({test}) returns {f(*test)}')



if __name__ == "__main__":
  main()
