import argparse
import sys

def calc(args):
    if args.o=='add':
        return args.x + args.y
    
    elif args.o == 'mul':
        return args.x *args.y
    
    elif args.o== 'div':
        return args.x / args.y
    
    else:
        return "invalid input"
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float , default= None, help="Enter first number. This is a utility function , please contact me")

    parser.add_argument('--y', type=float , default= None, help="Enter second number. This is a utility function , please contact me")

    parser.add_argument('--o', type=str , default= None, help="This is a utility function , please contact me")

args = parser.parse_args()
sys.stdout.write(str(calc(args)))
