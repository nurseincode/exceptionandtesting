def func_a():
    print('Func A started')
    func_b()
    print('Func A ended')

def func_b():
    print('Func B started')
    func_c()
    print('Func B ended')

def func_c():
    print('Func C started')
    result = 10 / 0 # Intentional error
    print('Func C ended')

# ZeroDivisionError
# Traceback shows the sequence the funcs were called in, to eventually call the error

# Main
func_a()