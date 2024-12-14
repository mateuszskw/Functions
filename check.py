def in_range(n, start, end):
  return n >= start and n <= end

def main():
  print(in_range(1, 0, 1))
  print(in_range(-1, -2, 0))
  print(in_range(-1, 0, 1))


if __name__ == "__main__":
  main()
