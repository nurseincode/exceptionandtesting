# def convert_to_integer(value):
#     result = int(value)
#     print(f'Conversion successful! Result: {result}')

# # User input
# # spam = input('Enter a number to convert to integer: ') 
# # print(spam) 
# # print(type(spam)) # Builtin input() always returns a string

# # User input
# spam = input('Enter a number: ')
# convert_to_integer(spam) # Calling the function explicitly: prints int when input is an int
# convert_to_integer('50') # Calling the function explicitly with str value: convertes to int
# print(type(convert_to_integer)) # Class function

# Handling the exception
def convert_to_integer(value):
    try:
        x = 10 / 0
        result = int(value)
        print(f'Conversion successful! Result: {result}')
    except ValueError:
       print(f'Conversion failed. Please enter a valid integer.')
    # except: Handles all exceptions, you can see what the error was
    except Exception as e: # Catches exception + stores the exception object in a variable e
        print(f'An unexpected error occured {e}')
# #   except (ValueError, ZeroDivisionError) handling specific multiple errors
#     except ZeroDivisionError:
#         print('Divide by zero!')
    else: # Only runs if no exceptions occurred
        print(f'Else invoked')
    finally: # Always runs
        print(f'Closing any open resources')

# User input
spam = input('Enter a number: ')
convert_to_integer(spam) 