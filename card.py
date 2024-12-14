def hide(value):
  hidden = value[0:2]
  for i in value[2:-4]:
    hidden += '*'
  hidden += value[-4:]
  return hidden

def main():
  print(hide('5290312400019022'))


if __name__ == "__main__":
  main()
