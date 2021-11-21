"""O objetivo neste módulo é definir funções que recebem os dados dos pacientes,
e montem as fórmulas que representem as restrições para a classificação de patologias """

from lib.semantics import *
from lib.functions import *

"""Restrição 5: Cada paciente com patologia deve ser coberto por alguma das regras."""
def pacientes_com_patologia_cobertos_alguma_regra(pacientes_com_patologia, numero_de_regras):

    dados_formula = []

    for j in range(len(pacientes_com_patologia)):
        or_lista = []

        for i in range(1, numero_de_regras):
            or_lista.append(Atom('c_'+ str(i) + '_' + str(j + 1)))

        formula_or = or_all(or_lista)
        dados_formula.append(formula_or)

    return and_all(dados_formula)