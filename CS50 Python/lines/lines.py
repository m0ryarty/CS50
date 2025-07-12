import sys

if len(sys.argv) < 2:
    sys.exit('Too few command-line argumwents')
if len(sys.argv) > 2:
    sys.exit('Too many command-line argumwents')

if sys.argv[1].endswith('.py'):

    count = 0

    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if line.lstrip() == '' or line.lstrip().startswith('#'):
                    pass
                else:
                    count = count + 1
        print(count)
    except FileNotFoundError:
        sys.exit('File does not exist')
else:
    sys.exit('Not a Python file')
