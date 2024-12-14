
def sum_digits(value):
  number = int(value)
  abs_number = abs(number)
  str_number = str(abs_number)
  sum = 0
  for i in str_number:
    sum += int(i)
  return sum


user_input = input('Enter integer number: ')
print(f'The sum of the digits in the number {user_input} is {sum_digits(user_input)}')
