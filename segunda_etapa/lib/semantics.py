"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """


from .formula import *
from .functions import atoms, remove_atom_from_list, get_value


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
    interpretation = primary_interpretation(formula, listAtoms)

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

def primary_interpretation(formula, listAtoms):
    """Creates an initial interpretation for formulas if they are of the instance Atom, Not (Atom), or And (if at least one of their sides contains an Atom or Not (Atom).
       For each Atom added in the interpretation, it is removed from the atom list. """

    interpretation = []

    true_interpretation_for_atom_not_and(formula, interpretation, listAtoms)

    return interpretation

def true_interpretation_for_atom_not_and(formula, interpretation, listAtoms):
    """Adds the truth value in interpretation and removes the atoms from the listAtoms"""

    if isinstance(formula, Atom):
        interpretation.append((str(formula), True))
        remove_atom_from_list(formula, listAtoms)
    elif isinstance(formula, Not):
        if isinstance(formula.inner, Atom):
            interpretation.append((str(formula.inner), False))
            remove_atom_from_list(formula.inner, listAtoms)
    if isinstance(formula, And):
        true_interpretation_for_atom_not_and(formula.left, interpretation, listAtoms)
        true_interpretation_for_atom_not_and(formula.right, interpretation, listAtoms)
    
def DPLL(formula):
    """Checks if the formula is satisfiable.
      It takes an input formula in CNF format and if satisfies, it returns an interpretation that assigns true to the formula.
      Otherwise, it returns False."""

    result = DPLL_check(formula, [])

    if result != False:
        return assign_value_irrelevant_literals(formula, result)

    return result

def DPLL_check(formula, interpretation):
    [formula, interpretation] = unit_propagation(formula, interpretation)

    if formula == []:
        return interpretation

    if check_empty_clause(formula):
        return False

    atomic = get_atomic(formula)

    formulaCopy = formula.copy()
    formulaCopy2 = formula.copy()

    formulaCopy.append([atomic])
    formulaCopy2.append([-atomic])

    result = DPLL_check(formulaCopy, interpretation)

    if result != False:
        return result
    
    return DPLL_check(formulaCopy2, interpretation)

    

def unit_propagation(formula, interpration):
    """BCP."""

    while has_unit_clause(formula):

        literal = literal_unit(formula)
        interpration.append(literal)

        formula = remove_clauses_with_literal(formula, literal)
        formula = remove_complement_literal(formula, literal)

    return [formula, interpration]

def check_empty_clause(formula):
    """ check if there is an empty clause in the formula """

    for clause in range(len(formula)):
        if len(formula[clause]) == 0:
            return True

    return False

def get_atomic(formula):
	literal = most_frequent_literal(formula)
    
	if literal < 0:
		return -(literal)

	return literal

def has_unit_clause(formula):
	""" checks if the formula has a unitary clause """

	for clause in range(len(formula)):
		if len(formula[clause]) == 1:
			return True

	return False

def literal_unit(formula):
	""" get literal from unit clause """
	for clause in range(len(formula)):
		if len(formula[clause]) == 1:
			return formula[clause][0]

	return False

def remove_clauses_with_literal(formula, literal):
   """ remove all formula clauses, which have the literal """

   new_formula = []

   for clause in range(len(formula)):
       clause_contains_literal = False

       for literal_clause in range(len(formula[clause])):

            if literal == formula[clause][literal_clause]:
                clause_contains_literal = True
                break

       if not clause_contains_literal:
           new_formula.append(formula[clause])

   return new_formula

def remove_complement_literal(formula, literal):
   """ remove all complements from the literal in the formula """

   new_formula = []

   for clause in range(len(formula)):

       new_clause = []

       for literal_clause in range(len(formula[clause])):

            if -(literal) != formula[clause][literal_clause]:
                new_clause.append(formula[clause][literal_clause])

       new_formula.append(new_clause)
       
   return new_formula

def most_frequent_literal(formula):
	""" take the most frequent literal in the formula"""

	literals = {}

	for clause in range(len(formula)):

		for literal in range(len(formula[clause])):

			if formula[clause][literal] not in literals:
				literals[formula[clause][literal]] = 0

			literals[formula[clause][literal]] += 1


	literals_sorted = sorted(literals, key = literals.get, reverse = True)

	return literals_sorted[0]

def assign_value_irrelevant_literals(formula, interpretation):
    """ assign value in irrelevant literals """

    for clause in range(len(formula)):

       for literal in range(len(formula[clause])):

            if (formula[clause][literal] not in interpretation) and (-(formula[clause][literal]) not in interpretation):
                
                if (formula[clause][literal] >= 0):
                    interpretation.append(-(formula[clause][literal]))
                else:
                    interpretation.append(formula[clause][literal])

    return interpretation
    