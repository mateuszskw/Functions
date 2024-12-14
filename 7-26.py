def f(string):
  return '-'.join(list(string))


def main():
  tests = [
    "Univesity", "UE", "x", ""
  ]
  for test in tests:
    print(f'f({test}) returns {f(test)}')



if __name__ == "__main__":
  main()
