import sys
from lib.functions import *
from restrictions import *

def main(args):
    print(is_cnf(Or(Atom('A'), And(Atom('B'), Atom('C'))))) # (A ou (B e C))
    return 0 

if __name__ == "__main__":
    sys.exit(main(sys.argv))
    