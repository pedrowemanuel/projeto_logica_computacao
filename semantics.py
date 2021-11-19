"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """


from formula import *
from functions import atoms, remove_atom_from_list, get_value
from lib import *


def truth_value(formula, interpretation):
    """Determines the truth value of a formula in an interpretation (valuation).
    An interpretation may be defined as dictionary. For example, {'p': True, 'q': False}.
    """

    if isinstance(formula, Atom):
        return get_value(formula, interpretation)
    if isinstance(formula, Not):
        return not truth_value(formula.inner, interpretation)
    if isinstance(formula, And):
        return truth_value(formula.left, interpretation) and truth_value(formula.right, interpretation)
    if isinstance(formula, Or):
        return truth_value(formula.left, interpretation) or truth_value(formula.right, interpretation)
    if isinstance(formula, Implies):
        if truth_value(formula.left, interpretation) and (not truth_value(formula.right, interpretation)):
            return False
        else:
            return True

    return False


def is_logical_consequence(premises, conclusion):  # function TT-Entails? in the book AIMA.
    """Returns True if the conclusion is a logical consequence of the set of premises. Otherwise, it returns False."""
    pass
    # ======== YOUR CODE HERE ========


def is_logical_equivalence(formula1, formula2):
    """Checks whether formula1 and formula2 are logically equivalent."""
    pass
    # ======== YOUR CODE HERE ========


def is_valid(formula):
    """Returns True if formula is a logically valid (tautology). Otherwise, it returns False"""
    pass
    # ======== YOUR CODE HERE ========

def satisfiability_brute_force(formula):
    """Checks whether formula is satisfiable.
    In other words, if the input formula is satisfiable, it returns an interpretation that assigns true to the formula.
    Otherwise, it returns False."""
    listAtoms = atoms(formula)
    interpretation = primary_interpretation_in_formula_and(formula, listAtoms)

    return sat(formula, listAtoms, interpretation)

def sat(formula, atoms, interpretation):
    """Performs the recursive part of satisfiability_brute_force"""
    if atoms == []:
        interpretation_convert = dict(interpretation)
        if truth_value(formula, interpretation_convert):
            return interpretation_convert
        else:
            return False

    atom = atoms.pop()
    atomsCopy = atoms.copy()
    atomsCopy2 = atoms.copy()

    interpretationTrue = interpretation.copy()
    interpretationTrue.append((str(atom), True))

    interpretationFalse = interpretation.copy()
    interpretationFalse.append((str(atom), False))

    resultInterpretationTrue = sat(formula, atomsCopy2, interpretationTrue)

    if resultInterpretationTrue != False:
        return resultInterpretationTrue
    
    return sat(formula, atomsCopy, interpretationFalse)

def primary_interpretation_in_formula_and(formula, listAtoms):
    """Creates initial interpretation for formulas if they are of the And instance and on at least one of their sides contains an Atom or Not(Atom).
    For each Atom that is added in interpretation, it is removed from the Atoms list"""

    interpretation = []

    if isinstance(formula, And):
        true_interpretation_for_atom_or_not(formula.left, interpretation, listAtoms)
        true_interpretation_for_atom_or_not(formula.right, interpretation, listAtoms)

    return interpretation

def true_interpretation_for_atom_or_not(formula, interpretation, listAtoms):
    """Adds the truth value in interpretation if the formula is an Atom or Not(Atom) and removes the atoms from the listAtoms"""

    if isinstance(formula, Atom):
        interpretation.append((str(formula), True))
        remove_atom_from_list(formula, listAtoms)
    elif isinstance(formula, Not):
        if isinstance(formula.inner, Atom):
            interpretation.append((str(formula.inner), False))
            remove_atom_from_list(formula.inner, listAtoms)