from sys import stdin, stdout
from repl.repl import start_repl

def main():
    print('Welcome to the pymonkey interpreter')
    start_repl(stdin, stdout)
    
if __name__ == '__main__':
    main()
