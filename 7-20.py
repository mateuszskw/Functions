def is_prime(number):
  factors_found = False

  for i in range(2, int(number / 2) + 1):
    if number % i == 0:
      factors_found = True
      break

  return not factors_found

def f(n):
  i = 0
  j = 1
  prime = 0
  while i < n:
    j += 1
    if is_prime(j):
      prime = j
      i += 1
  return prime


def main():
  tests = [
    1, 5, 200
  ]
  for test in tests:
    print(f'f({test}) returns {f(test)}')



if __name__ == "__main__":
  main()
