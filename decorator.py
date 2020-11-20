def cough_dec(func):
    def func_wrapper():
        # code before function
        print('cough*')
        func()
        # code after
        print('cough**')

    return func_wrapper

@cough_dec
def question():
    print('can you give me a discount on that?')

def answer():
    print('it\'s only 50p you cheapskate')

question()
answer()