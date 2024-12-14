

def f(number):
  result = 0
  arr = list(str(number))
  for i in set(arr):
    count = arr.count(i)
    result += count * int(i) * int(bool(count - 1))
  return result


def main():
  tests = [
    1027, 230335, 513553007
  ]
  for test in tests:
    print(f'f({test}) returns {f(test)}')



if __name__ == "__main__":
  main()
