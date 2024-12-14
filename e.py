def counte(value):
  count = 0
  for char in value:
    if char.upper() == 'E':
      count += 1
  return count

def main():
  print('e', counte('e'))
  print('ee', counte('ee'))

if __name__ == "__main__":
    main()
