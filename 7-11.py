def valid(value):
  return value < 0

def f(*arr):
  return any(map(valid, arr))

def main():
  print(f'f(11,6,-4) returns {f(11,6,-4)}')
  print(f'f(5,4,14) returns {f(5,4,14)}')



if __name__ == "__main__":
  main()
