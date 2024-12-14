def f(binary_number):
  try:
    int(binary_number, 2)
    return True
  except:
    return False



def main():
  print(f'f("101101") returns {f("101101")}')
  print(f'f("1311a10100") returns {f("1311a10100")}')



if __name__ == "__main__":
  main()
