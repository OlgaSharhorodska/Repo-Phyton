import argparse

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def main():
    parser = argparse.ArgumentParser(description='Simple Calculator')
    parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'], help='Operation to perform (add/subtract/multiply/divide)')
    parser.add_argument('x', type=float, help='First number')
    parser.add_argument('y', type=float, help='Second number')
    args = parser.parse_args()

    if args.operation == 'add':
        result = add(args.x, args.y)
        print(f'{args.x} + {args.y} = {result}')
    elif args.operation == 'subtract':
        result = subtract(args.x, args.y)
        print(f'{args.x} - {args.y} = {result}')
    elif args.operation == 'multiply':
        result = multiply(args.x, args.y)
        print(f'{args.x} * {args.y} = {result}')
    elif args.operation == 'divide':
        result = divide(args.x, args.y)
        print(f'{args.x} / {args.y} = {result}')

if __name__ == '__main__':
    main()
