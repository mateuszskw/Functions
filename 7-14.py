def mul(a, b):
  return a * b

def mod(a, b):
  return a % b

def add(a, b):
  return a + b

def sub(a, b):
  return a - b

config = {
  "+": add,
  "-": sub,
  "*": mul,
  "%": mod,
  "**": pow
}

def f(a, b, operator):
  return config.get(operator)(a, b)


def main():
  print(f'f(2,3, "+") returns "{f(2,3, "+")}"')
  print(f'f(2,3, "%") returns "{f(2,3, "%")}"')
  print(f'f(2,3, "**") returns "{f(2,3, "**")}"')
  print(f'f(2,3, "*") returns "{f(2,3, "*")}"')
  print(f'f(2,3, "-") returns "{f(2,3, "-")}"')



if __name__ == "__main__":
  main()
