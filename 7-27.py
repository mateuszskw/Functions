def f(string):
  return sum(map(int, string[:-1])) % 7 == int(string[-1])


def main():
  tests = [
    "1082", "2035", "1114", "7071"
  ]
  for test in tests:
    print(f'f({test}) returns {f(test)}')



if __name__ == "__main__":
  main()
