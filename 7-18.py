def f(sentence):
  return sentence.replace(" ", "")

def main():
  tests = [
    'integrated development environment',
    'A programming language is a system of notation for writing computer programs',
  ]
  for test in tests:
    print(f'f({test}) returns {f(test)}')



if __name__ == "__main__":
  main()
