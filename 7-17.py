def f(palindrome):
  return palindrome == ''.join(reversed(list(palindrome)))

def main():
  tests = [
    'radar', '12-11-21', 'book'
  ]
  for test in tests:
    print(f'f({test}) returns {f(test)}')



if __name__ == "__main__":
  main()
