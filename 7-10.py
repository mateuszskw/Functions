def f(x, y):
  start = min(x, 0)
  end = min(y, 0)
  count = 0
  for i in range(start, end):
    if i % 2 == 0:
      count += 1
  return count

def main():
  print(f'f(-7,8) returns {f(-7, 8)}')
  print(f'f(-1,11) returns {f(-1, 11)}')



if __name__ == "__main__":
  main()
