from pysat.solvers import Glucose3

import sys
from lib.functions import *
from lib.semantics import *

def main(args):

    g = Glucose3()
    g.add_clause([-1, 2])
    g.add_clause([-2, 3])

    if g.solve() != False:
        print(g.get_model())
    else:
        print('A fórmula é insatisfatível')

    return 0 

if __name__ == "__main__":
    sys.exit(main(sys.argv))
    