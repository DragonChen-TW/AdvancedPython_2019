# Some functions in this file
# Main logic in advanced_04

def hi(s):
    print('hi', s)

def bye(s):
    print('bye', s)

print('>> __name__ is "{}"'.format(__name__))

# if you wanna do some test
# but do not be executed in main file
if __name__ == '__main__':
    print('THERE IS MAIN FUNCTION')
    name = 'Jackson'
    hi(name)
    bye(name)
