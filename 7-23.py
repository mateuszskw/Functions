

def f(string):
  return len(string) >= 6 and len(string) == len(set(string))


def main():
  tests = [
    "ax15", "book123", "A2water3", "qwerty", ""
  ]
  for test in tests:
    print(f'f({test}) returns {f(test)}')



if __name__ == "__main__":
  main()
