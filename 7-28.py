def f(string):
  top = ''
  maximum = 0
  curr = 0
  for i in range(0, len(string)):
    if string[i - 1] == string[i]:
      curr += 1
    else:
      curr = 1
    if curr >= maximum:
      top = string[i]
      maximum = curr
  return top


def main():
  tests = [
    "5233165554211", "2133"
  ]
  for test in tests:
    print(f'f({test}) returns {f(test)}')



if __name__ == "__main__":
  main()
