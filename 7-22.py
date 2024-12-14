def firstLetter(word):
  return word[0]

def f(string):
  return ''.join(map(firstLetter, string.split()))


def main():
  tests = [
    "Internet of Things", "For Your Information", "Python"
  ]
  for test in tests:
    print(f'f({test}) returns {f(test)}')



if __name__ == "__main__":
  main()
