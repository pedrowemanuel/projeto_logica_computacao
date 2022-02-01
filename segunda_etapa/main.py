import sys
from lib.functions import *
from restrictions import *

def main(args):
    print(is_cnf(Not(Not(Not(Not(Not(Not(Not((Atom("G")))))))))))
    return 0 

if __name__ == "__main__":
    sys.exit(main(sys.argv))