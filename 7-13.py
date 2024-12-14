def f(number):
  arr = map(str, range(1, number + 1))
  return ''.join(list(arr))



def main():
  print(f'f(11) returns "{f(11)}"')
  print(f'f(4) returns "{f(4)}"')



if __name__ == "__main__":
  main()
