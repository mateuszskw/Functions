def asterisk(_):
  return '*'

def f(number):
  arr = list(map(asterisk, range(0, number)))
  return '/'.join(arr)



def main():
  print(f'f(4) returns {f(4)}')
  print(f'f(1) returns {f(1)}')



if __name__ == "__main__":
  main()
