def f(number, even):
  result = 0
  for char in str(number):
    if even == (int(char) % 2 == 0):
      result += int(char)
  return result

def main():
  print(f'f(3124,True) returns {f(3124, True)}')
  print(f'f(3124,False) returns {f(3124, False)}')
  print(f'f(20576,False) returns {f(20576, False)}')
  print(f'f(20576,True) returns {f(20576, True)}')
  print(f'f(13115,True) returns {f(13115, True)}')



if __name__ == "__main__":
  main()
