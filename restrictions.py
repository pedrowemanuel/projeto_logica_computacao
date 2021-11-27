"""O objetivo neste módulo é definir funções que recebem os dados dos pacientes,
e montem as fórmulas que representem as restrições para a classificação de patologias """

from lib.semantics import *
from lib.functions import *


"""Restrição 1: Para cada atributo e cada regra, temos exatamente uma das três possibilidades: o atributo aparece
positivamente na regra, o atributo aparece negativamente na regra ou o atributo não aparece na regra."""
def apenas_tres_casos_para_cada_regra_atributo(numero_de_regras, atributos):
    dados_formula = []
    for i in range(1, numero_de_regras + 1):
        and_lista = []

        for a in range(len(atributos)):
            and_lista.append(
                Or (
                    Or(
                        And(
                            And(Atom('X_' + str(atributos[a]) + '_' + str(i) + '_p'), Not(Atom('X_' + str(atributos[a]) + '_' + str(i) + '_n'))),
                            Not(Atom('X_' + str(atributos[a]) + '_' + str(i) + '_s'))
                        ),
                        And(
                            And(Not(Atom('X_' + str(atributos[a]) + '_' + str(i) + '_p')), Atom('X_' + str(atributos[a]) + '_' + str(i) + '_n')),
                            Not(Atom('X_' + str(atributos[a]) + '_' + str(i) + '_s'))
                        ),
                    ),
                    And(
                        And(Not(Atom('X_' + str(atributos[a]) + '_' + str(i) + '_p')), Not(Atom('X_' + str(atributos[a]) + '_' + str(i) + '_n'))),
                        Atom('X_' + str(atributos[a]) + '_' + str(i) + '_s')
                    ),
                )
            )
    
        formula_or = or_all(and_lista)
        dados_formula.append(formula_or)

    return and_all(dados_formula)

'''Cada regra deve ter algum atributo aparecendo nela'''
def restricao2(atributos , num_regras):
    dados_formula = []
    for i in range(1, num_regras+1):
        lista = []
        for j in range(0,len(atributos)):
            or_lista = []
            or_lista.append(
                Not(
                    Atom(
                        "X_"+str(atributos[j])+"_"+str(i)+"_s"  
                    )
                )
            )    
            formula_or = or_all(or_lista)
            lista.append(formula_or)
        formula = or_all(lista)
        dados_formula.append(formula)
    return and_all(dados_formula)

"""Restrição 3: Para cada paciente sem patologia e cada regra, algum atributo do paciente não pode ser aplicado à
regra."""
def pacientes_sem_patologia_algum_atributo_nao_aplicado_regra(pacientes_sem_patologia, numero_de_regras, atributos):
    dados_formula = []

    for j in range(len(pacientes_sem_patologia)):
        and_lista = []

        for i in range(1, numero_de_regras + 1):
            or_lista = []

            for a in range(len(pacientes_sem_patologia[j])):
                if pacientes_sem_patologia[j][a] == 0:
                    or_lista.append(Atom('X_' + str(atributos[a]) + '_' + str(i) + '_p'))
                elif pacientes_sem_patologia[j][a] == 1:
                    or_lista.append(Atom('X_' + str(atributos[a]) + '_' + str(i) + '_n'))
        
            formula_or = or_all(or_lista)
            and_lista.append(formula_or)

        formula_and = and_all(and_lista)
        dados_formula.append(formula_and)

    return and_all(dados_formula)

'''Para cada paciente com patologia, cada regra e cada atributo, se o atributo do paciente n ̃ao se aplicar
ao da regra, ent ̃ao a regra n ̃ao cobre esse paciente.'''
def restricao4(pacientes_com_patologia, atributos, regras):
    dados_formula = []
    for j in range(len(pacientes_com_patologia)):
        lista = []
        for i in range(1, regras + 1):
            implie_lista = []
            for a in range(len(pacientes_com_patologia[j])):
                if pacientes_com_patologia[j][a] == 0:
                    implie_lista.append(
                        Implies(
                            Atom('X_' + str(atributos[a]) + '_' + str(i) + '_p'), Not(Atom("C_"+str(i)+"_"+str(j+1)))
                        )
                    )
                elif pacientes_com_patologia[j][a] == 1:
                    implie_lista.append(
                        Implies(
                            Atom('X_' + str(atributos[a]) + '_' + str(i) + '_n'), Not(Atom("C_"+str(i)+"_"+str(j+1)))
                        )
                    )
            
            lista.append(and_all(implie_lista))
        dados_formula.append(and_all(lista))
    return and_all(dados_formula)
"""Restrição 5: Cada paciente com patologia deve ser coberto por alguma das regras."""
def pacientes_com_patologia_cobertos_alguma_regra(pacientes_com_patologia, numero_de_regras):

    dados_formula = []

    for j in range(len(pacientes_com_patologia)):
        or_lista = []

        for i in range(1, numero_de_regras + 1):
            or_lista.append(Atom('C_'+ str(i) + '_' + str(j + 1)))

        formula_or = or_all(or_lista)
        dados_formula.append(formula_or)

    return and_all(dados_formula)