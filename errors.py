def convert_to_integer(value):
    result = int(value)
    print(f'Conversion successful! Result: {result}')

# User input
# spam = input('Enter a number to convert to integer: ') # Built input() always returns a string
# print(spam)
# print(type(spam))

# User input
spam = input('Enter a number: ')
convert_to_integer(spam) # Calling the function explicitly: prints an integer
# print(type(spam))
convert_to_integer('50') # Calling the function explicitly with str value: prints an integer
print(type(convert_to_integer))


