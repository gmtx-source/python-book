number = 4936

one = number % 10
print('Ones:', one)

number = number // 10

tens = number % 10
print('Tens:', tens)

number = number // 10

hundreds = number % 10
print('Hundreds:', hundreds)

thousands = number // 10
print('Thousands:', thousands)