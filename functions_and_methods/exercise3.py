def ask_number(question):
    numero = input(question)
    return float(numero)

def multi(num1, num2):
    return num1 *  num2


num1 = ask_number('First number: ')
num2 = ask_number('Second number: ')

print(f'The multiplication between {num1} * {num2} = {multi(num1, num2)}')