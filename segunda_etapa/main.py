import sys
from lib.functions import *
from restrictions import *

def main(args):
    formula = Or(Atom('p'), Not(Not('q')))
    print(is_cnf(formula))
    return 0 

if __name__ == "__main__":
    sys.exit(main(sys.argv))