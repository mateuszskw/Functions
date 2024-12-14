def f(amount):
  result = amount

  coin_5 = int(result / 5)
  result -= coin_5  * 5

  coin_2 = int(result / 2)
  result -= coin_2  * 2

  return coin_5 + coin_2 + result

def main():
  print(f'f(23) returns {f(23)}')
  print(f'f(8) returns {f(8)}')
  print(f'f(1) returns {f(1)}')
  print(f'f(0) returns {f(0)}')



if __name__ == "__main__":
  main()

