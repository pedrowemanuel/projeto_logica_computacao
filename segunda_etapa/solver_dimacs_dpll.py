import sys
from lib.functions import *
from lib.semantics import *

def main(args):
    result = DPLL([[1,-1, 2], [1]])

    if result != False:
        print(result)
    else:
        print('A fórmula é insatisfatível')

    return 0 

if __name__ == "__main__":
    sys.exit(main(sys.argv))
    