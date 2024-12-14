
def add(a, b):
  return a + b

def sub(a, b):
  return a - b

config = {
  "+": add,
  "-": sub,
}

def f(string):
  result = int(string[0])
  operator = ''
  for char in string[1:]:
    if char.isnumeric():
      operation = config.get(operator)
      result = operation(result, int(char))
    else:
      operator = char
  return result


def main():
  tests = [
    "2+3", "3+8+1", "2+3-4+5-0"
  ]
  for test in tests:
    print(f'f({test}) returns {f(test)}')



if __name__ == "__main__":
  main()
