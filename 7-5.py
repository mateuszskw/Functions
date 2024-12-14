import check


number = float(input('A number: '))
print(f'Number {number} in the range <2,15>: {'yes' if check.in_range(number, 2, 15) else 'no'}')
