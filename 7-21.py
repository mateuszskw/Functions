def f(n1, n2, n3):
  largest = max(n1, n2, n3)
  smallest = min(n1, n2, n3)
  return largest - smallest


def main():
  tests = [
    (7, 4, 9), (2, 12, 8)
  ]
  for test in tests:
    print(f'f({test}) returns {f(*test)}')



if __name__ == "__main__":
  main()
