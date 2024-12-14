def f(string):
  people = 0
  result = False
  for char in string:
    if char == '+':
      people += 1
    else:
      people -= 1
    if people >= 3:
      result = True
      break
  return result


def main():
  tests = [
    "+-+++-+---", "+-+-+-+-", "+-++-+--", "+-++-++-+---"
  ]
  for test in tests:
    print(f'f({test}) returns {f(test)}')



if __name__ == "__main__":
  main()
