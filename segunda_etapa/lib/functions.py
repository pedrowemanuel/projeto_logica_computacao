"""The goal in this module is to define functions that take a formula as input and
do some computation on its syntactic structure. """


from os import replace

from auxiliary_functions import substituir_valores_por_atomos
from .formula import *


def length(formula):
    """Determines the length of a formula in propositional logic."""
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return length(formula.inner) + 1
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return length(formula.left) + length(formula.right) + 1


def subformulas(formula):
    """Returns the set of all subformulas of a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for subformula in subformulas(my_formula):
        print(subformula)

    This piece of code prints p, s, (p v s), (p → (p v s))
    (Note that there is no repetition of p)
    """

    if isinstance(formula, Atom):
        return {formula}
    if isinstance(formula, Not):
        return {formula}.union(subformulas(formula.inner))
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        sub1 = subformulas(formula.left)
        sub2 = subformulas(formula.right)
        return {formula}.union(sub1).union(sub2)

#  we have shown in class that, for all formula A, len(subformulas(A)) <= length(A).


def atoms(formula):
    """Returns the set of all atoms occurring in a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for atom in atoms(my_formula):
        print(atom)

    This piece of code above prints: p, s
    (Note that there is no repetition of p)
    """
    list_atoms = []
    for subformula in subformulas(formula):
        if isinstance(subformula, Atom):
            list_atoms.append(subformula)
    return list_atoms


def number_of_atoms(formula):
    #mostra o numero de atomicas
    if isinstance(formula,Atom):
        return 1
    if isinstance(formula, Not):
        return number_of_atoms(formula.inner)
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return number_of_atoms(formula.right) + number_of_atoms(formula.left)

def remove_atom_from_list(atom, listAtoms):
    """Removes an Atom from a list of atoms (listAtoms)"""

    for index in range(len(listAtoms)):
        if listAtoms[index] == atom:
            del listAtoms[index]
            break

def get_value(atom, interpretation):
    """Get the value of an Atom in an interpretation. If it doesn't find the Atom, it returns None."""
    for key in interpretation.keys():
        if str(key) == str(atom):
            return interpretation[str(key)]

    return None

def number_of_connectives(formula):
    if isinstance(formula, Atom):
        return 0
    if isinstance(formula, Not):
        return number_of_connectives(formula.inner)
    if isinstance(formula, Implies) or isinstance(formula, Or):
        return number_of_connectives(formula.left) + number_of_connectives(formula.right)
    if isinstance(formula, And):
        return number_of_connectives(formula.left) + number_of_connectives(formula.right) + 1


def is_literal(formula):
    """Returns True if formula is a literal. It returns False, otherwise"""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def substitution(formula, old_subformula, new_subformula):
    """Returns a new formula obtained by replacing all occurrences
    of old_subformula in the input formula by new_subformula."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_clause(formula):
    """Returns True if formula is a clause. It returns False, otherwise"""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_negation_normal_form(formula):
    if isinstance(formula, Atom):
        return formula

    if isinstance(formula, Not):
        if isinstance(formula.inner, Atom):
            return formula

        if isinstance(formula.inner , Not):
            return is_negation_normal_form(formula.inner.inner)

        if isinstance(formula.inner, And):
            return is_negation_normal_form(Or(Not(formula.inner.left), Not(formula.inner.right)))

        if isinstance(formula.inner, Or):
            return is_negation_normal_form(And(Not(formula.inner.left), Not(formula.inner.right)))

    if isinstance(formula, Or):
        return (Or(is_negation_normal_form(formula.left), is_negation_normal_form(formula.right)))

    if isinstance(formula, And):
        return (And(is_negation_normal_form(formula.left), is_negation_normal_form(formula.right)))




def implication_free(formula):
    if isinstance(formula, Implies):
        return (Or(Not(implication_free(formula.left)),implication_free(formula.right)))

    if isinstance(formula, And):
        return (And(implication_free(formula.left), implication_free(formula.right)))

    if isinstance(formula, Or):
        return (Or(implication_free(formula.left), implication_free(formula.right)))

    if isinstance(formula, Atom):
        return formula

    if isinstance(formula, Not):
        return (Not(implication_free(formula.inner)))

def distributive(formula):
    if isinstance(formula, Atom):
        return formula

    if isinstance(formula, And):
        return And(distributive(formula.left), distributive(formula.right))

    if isinstance(formula, Or):
        b1 = distributive(formula.left)
        b2 = distributive(formula.right)

        if isinstance(b1, And):
            return And(distributive(Or(b1.left, b2)), distributive(Or(b1.right, b2)))

        if isinstance(b2, And):
            return And(distributive(Or(b1, b2.left)), distributive(Or(b1, b2.right)))

        return (Or(b1, b2))

    return formula

def is_cnf(formula):
    b = implication_free(formula)

    b = is_negation_normal_form(b)

    b = distributive(b)

    return b



def is_term(formula):
    """Returns True if formula is a term. It returns False, otherwise"""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_dnf(formula):
    """Returns True if formula is in disjunctive normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_decomposable_negation_normal_form(formula):
    """Returns True if formula is in decomposable negation normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========

# auxiliary functions:

def and_all(list_formulas):
    """
    Returns a BIG AND formula from a list of formulas
    For example, if list_formulas is [Atom('1'), Atom('p'), Atom('r')], it returns
    And(And(Atom('1'), Atom('p')), Atom('r')).
    :param list_formulas: a list of formulas
    :return: And formula
    """
    first_formula = list_formulas[0]
    del list_formulas[0]
    for formula in list_formulas:
        first_formula = And(first_formula, formula)
    return first_formula


def or_all(list_formulas):
    """
    Returns a BIG OR of formulas from a list of formulas.
    For example, if list_formulas is [Atom('1'), Atom('p'), Atom('r')], it returns
    Or(Or(Atom('1'), Atom('p')), Atom('r')).
    :param list_formulas: a list of formulas
    :return: Or formula
    """
    first_formula = list_formulas[0]
    del list_formulas[0]
    for formula in list_formulas:
        first_formula = Or(first_formula, formula)
    return first_formula

def write_file(formula, atomicas):
    if isinstance(formula, Atom):
        return atomicas[formula]
    if isinstance(formula, And) or isinstance(formula, Or):
        return write_file(atomicas[formula.left], atomicas[formula.right])

def dimacs_para_cnf(arquivo):
    
    try:
        arquivo = open(arquivo, 'r')
        numeros = []
        lista = []
        atomos = {}
        
        pegar_atomos = False

        for linha in arquivo:
            
            # pegando as atomicas e seus numeros correspondentes
            if 'c atomics' in linha:
                pegar_atomos = True
                continue
            if 'c end atomics' in linha:
                pegar_atomos = False
                continue
            if pegar_atomos:
                linha_com_atomo = linha.split("c ")
                
                atomo = linha_com_atomo[1].split(":")
                atomos[int(atomo[1].replace("\n",""))] = atomo[0]
                continue

            if 'c' in linha or 'p' in linha or '%' in linha:
                continue
            
            # pegando a formula
            numeros.append(linha.split(" "))
        
        for j in numeros:
            
            linha = []

            for i in range(0, len(j) - 1):
                linha.append(int(j[i]))

            lista.append(linha)
            
        arquivo.close()

        return [lista, atomos]
    except FileNotFoundError as err:
        return err

def atomos_dimacs_cnf(arquivo):
    
    try:
        arquivo = open(arquivo, 'r')
        atomos = {}
        
        pegar_atomos = False

        for linha in arquivo:
            
            # pegando as atomicas e seus numeros correspondentes
            if 'c atomics' in linha:
                pegar_atomos = True
                continue
            if 'c end atomics' in linha:
                pegar_atomos = False
                continue
            if pegar_atomos:
                linha_com_atomo = linha.split("c ")
                
                atomo = linha_com_atomo[1].split(":")
                atomos[int(atomo[1].replace("\n",""))] = atomo[0]
                continue
            
        arquivo.close()

        return atomos
    except FileNotFoundError as err:
        return err


def cnf_para_dimacs(formula_cnf, nome_arquivo, regras):
    lista = atoms(formula_cnf) #recebe as atomicas
    atomicas = {}
    qtd_and = number_of_connectives(formula_cnf)
    index = 1

    for elemento in lista:
        atomicas[index] = str(elemento)
        index += 1

    # Escrita do arquivo
    arquivo = open(f"./DIMACS/Fórmulas Restrições Pacientes/{nome_arquivo}_solution_{regras}_regras.cnf","w", encoding="utf-8")
    arquivo.write("c THIS FORMULA IS GENERATED BY CNF\n")
    arquivo.write("c \n")
    arquivo.write("c atomics\n")
    for i in atomicas.items():
        arquivo.write(f"c {i[1]}:{i[0]}\n")
    arquivo.write("c end atomics\n")
    arquivo.write(f"p cnf {index-1} {qtd_and}\n")
    
    
    print("O arquivo '"+nome_arquivo+"_solution_"+str(regras)+"_regras.cnf' foi gerado")
    
    arquivo.close()
