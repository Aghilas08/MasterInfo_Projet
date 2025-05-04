#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 19:11:52 2022

@author: jlebovits
"""

from __future__ import division
import sys
import os
import random
from copy import deepcopy


initial_path = os.getcwd()
#print('initial_path = ',initial_path, '\n')


if "/home/ec2-user/python-api" in initial_path or "/Users/pauldampfhoeffer/Documents/DPM_Solutions/Galadrim/PyxiScience/pyxiscience/python-api" in initial_path:
	import src.scripts.Mes_fctions.Mes_fctions_deterministes
	from src.scripts.Mes_fctions.Mes_fctions_deterministes import * 
	
	import src.scripts.Mes_fctions.Mes_fctions_generalistes
	from src.scripts.Mes_fctions.Mes_fctions_generalistes import * 
	
	import src.scripts.Mes_fctions.Mes_fctions_probabilistes
	from src.scripts.Mes_fctions.Mes_fctions_probabilistes import * 
	
	import src.scripts.Mes_fctions.Mes_fctions_d_ecriture_Latex
	from src.scripts.Mes_fctions.Mes_fctions_d_ecriture_Latex import * 
	
	# import src.scripts.Mes_fctions.Mes_fctions_d_alg_generale
	# from src.scripts.Mes_fctions.Mes_fctions_d_alg_generale import * 

else :
	from Mes_fctions_generalistes import *
	from Mes_fctions_d_ecriture_Latex import *
	from Mes_fctions_deterministes import *
	from Mes_fctions_probabilistes import * 
	#from Mes_fctions_d_alg_generale import * 
	#from Prog_Python import *


import sympy

from random import uniform, Random, randrange, randint
from random import *
from functools import reduce

import numpy.random as npr 
import numpy.linalg as alg
import numpy as np

from sympy import *
from sympy.stats import *

from random import uniform, Random, randrange, randint

from sympy.stats import P, E, variance, Die, Normal

from sympy import Eq, simplify


import random


import sympy
from sympy import *
from sympy.stats import *
from random import uniform, Random, randrange, randint
from sympy.stats import P, E, variance, Die, Normal
from sympy import Eq, simplify



from random import uniform, Random, randrange, randint
from random import *
from functools import reduce

import numpy.random as npr 
import numpy.linalg as alg
import numpy as np





import math
from random import uniform, Random, randrange, randint

#import numpy as np
#import numpy.random as npr 
from sympy import *
from random import *
from sympy.stats import *

# from sympy import Eq, simplify, S, Symbol, Rational, binomial, expand_func
from sympy.stats import P, E, variance, Die, Normal, DiscreteUniform, Bernoulli, sample, Binomial, density,  Normal, sample_iter, given
from sympy import Piecewise, log, piecewise_fold
from sympy import S, Symbol
from random import uniform, Random, randrange, randint
from sympy import Eq, simplify, S, Symbol
from sympy import MatrixSymbol, Transpose, transpose

from sympy.abc import x, y
  
import numpy as np
import numpy.random as npr 

inf=float("inf")


import random



#print('toto')



def alg_generale() :
  chaine = "alg generale Ok"
  return chaine



##===========================================================================================
##===========================================================================================
# 
#
#                                 New fction                                      
#
##===========================================================================================
##=========================================================================================

from sympy import S, Symbol
from sympy.stats import DiscreteUniform, sample_iter
import random

from sympy import S, Symbol
from sympy.stats import DiscreteUniform, sample_iter
import random

def Poly_with_random_coef(symbol, deg, constant_coef):
    """
    Génère un polynôme aléatoire de degré deg avec l'indéterminée symbol.
    
    Paramètres:
    - symbol (str): Nom de la variable du polynôme
    - deg (int): Degré du polynôme
    - constant_coef (int): 
        0: Le coefficient constant sera 0
        1: Le coefficient constant sera non-nul (aléatoire mais ≠ 0)
        autre: Le coefficient constant sera aléatoire dans [-9, 9]
    
    Retourne:
    - list: [expression SymPy du polynôme, représentation LaTeX du polynôme]
    """
    # Générer tous les coefficients en une seule fois
    L = random.sample(range(-9, 10), deg + 1)
    
    # Traitement spécial pour le coefficient constant
    if constant_coef == 0:
        L[0] = 0
    elif constant_coef == 1:
        # Assurer un coefficient constant non nul
        while L[0] == 0:
            L[0] = random.randint(-9, 9)
    
    # Créer le symbole pour la variable
    X = Symbol(symbol)
    
    # Construire l'expression symbolique du polynôme
    poly = sum(L[i] * X**i for i in range(deg + 1))
    
    # Construire la représentation LaTeX
    poly_latex = ""
    for i in range(deg + 1):
        coef = L[i]
        if coef == 0:
            continue
            
        # Gérer le premier terme différemment (pas de + ou - initial)
        if poly_latex == "":
            if i == 0:  # Terme constant
                poly_latex = str(coef)
            else:  # Termes avec variable
                if coef == 1:
                    poly_latex = f"{symbol}" if i == 1 else f"{symbol}^{i}"
                elif coef == -1:
                    poly_latex = f"-{symbol}" if i == 1 else f"-{symbol}^{i}"
                else:
                    poly_latex = f"{coef}{symbol}" if i == 1 else f"{coef}{symbol}^{i}"
        else:
            # Termes suivants avec + ou -
            if i == 0:  # Terme constant
                poly_latex += f" + {coef}" if coef > 0 else f" - {-coef}"
            else:  # Termes avec variable
                if coef == 1:
                    term = f"{symbol}" if i == 1 else f"{symbol}^{i}"
                    poly_latex += f" + {term}"
                elif coef == -1:
                    term = f"{symbol}" if i == 1 else f"{symbol}^{i}"
                    poly_latex += f" - {term}"
                elif coef > 0:
                    term = f"{symbol}" if i == 1 else f"{symbol}^{i}"
                    poly_latex += f" + {coef}{term}"
                else:
                    term = f"{symbol}" if i == 1 else f"{symbol}^{i}"
                    poly_latex += f" - {-coef}{term}"
    
    # Si tous les coefficients sont nuls, renvoyer "0"
    if poly_latex == "":
        poly_latex = "0"
        
    return [poly, poly_latex]



##===========================================================================================
##===========================================================================================
#                                   Début des essais                                      
##===========================================================================================
##===========================================================================================


# # Le coef constant est nul
# C =  Poly_with_random_coef('X',3,1)

# u = 6 
# #Z = '({'+str(u)+'})'
# C =  Poly_with_random_coef('Z',3,1)


# C_1 = C[0]
# C_2 = C[1]

# print('C_1 =' , C_1,'\n')
# print('C_2 =' , C_2,'\n')


# # Le coef constant n'est pas nul
# D= Poly_with_random_coef('X',3,1)
# D_1 = D[0]
# D_2 = D[1]

# print('D_1 =' , D_1,'\n')
# print('D_2 =' , D_2,'\n')


# # Le coef constant est tiré aléatoirement et uniformément 
# E= Poly_with_random_coef('X',3,2)
# E_1 = E[0]
# E_2 = E[1]

# print('E_1 =' , E_1,'\n')
# print('E_2 =' , E_2,'\n')

   
##===========================================================================================
##===========================================================================================
#                                   Fin des essais                                      
##===========================================================================================
##===========================================================================================








##===========================================================================================
##===========================================================================================
#                                 New fction                                      
##===========================================================================================
##=========================================================================================


from sympy import Symbol, Poly
import random

def Poly_with_random_coef_v2(symbol, deg, constant_coef):
    """
    Génère un polynôme aléatoire de degré exactement deg avec des coefficients dans [-9, 9].
    
    Paramètres:
    - symbol (str): Nom de la variable du polynôme
    - deg (int): Degré exact du polynôme (coefficient de X^deg sera non-nul)
    - constant_coef (int): 
        0: Le coefficient constant sera 0
        1: Le coefficient constant sera non-nul
        autre: Le coefficient constant sera aléatoire dans [-9, 9]
    
    Retourne:
    - list: [polynôme SymPy, représentation LaTeX ordre croissant, représentation LaTeX ordre décroissant]
    """
    # Générer tous les coefficients aléatoirement
    coefficients = [random.randint(-9, 9) for _ in range(deg + 1)]
    
    # Traitement spécial pour le coefficient constant
    if constant_coef == 0:
        coefficients[0] = 0
    elif constant_coef == 1:
        # Assurer un coefficient constant non nul
        while coefficients[0] == 0:
            coefficients[0] = random.randint(-9, 9)
    
    # Assurer que le coefficient de degré le plus élevé soit non nul
    while coefficients[deg] == 0:
        coefficients[deg] = random.randint(-9, 9)
    
    # Créer le symbole pour la variable
    X = Symbol(symbol)
    
    # Construire l'expression symbolique et créer l'objet Poly
    poly_expr = sum(coefficients[i] * X**i for i in range(deg + 1))
    polynomial = Poly(poly_expr, X)
    
    # Générer la représentation LaTeX en ordre croissant
    asc_latex = ""
    for i in range(deg + 1):
        coef = coefficients[i]
        if coef == 0:
            continue
            
        # Formater le signe
        if asc_latex == "":
            sign = "-" if coef < 0 else ""
        else:
            sign = " + " if coef > 0 else " - "
        
        # Valeur absolue du coefficient pour l'affichage
        abs_coef = abs(coef)
        
        # Formater le terme selon la puissance
        if i == 0:  # Terme constant
            term = str(abs_coef)
        elif i == 1:  # Terme de degré 1 (x au lieu de x^1)
            term = symbol if abs_coef == 1 else f"{abs_coef}{symbol}"
        else:  # Termes de degré supérieur
            term = f"{symbol}^{{{i}}}" if abs_coef == 1 else f"{abs_coef}{symbol}^{{{i}}}"
            
        asc_latex += f"{sign}{term}"
    
    # Cas polynôme nul
    if asc_latex == "":
        asc_latex = "0"
    
    # Générer la représentation LaTeX en ordre décroissant
    desc_latex = ""
    for i in range(deg, -1, -1):
        coef = coefficients[i]
        if coef == 0:
            continue
            
        # Formater le signe
        if desc_latex == "":
            sign = "-" if coef < 0 else ""
        else:
            sign = " + " if coef > 0 else " - "
        
        # Valeur absolue du coefficient pour l'affichage
        abs_coef = abs(coef)
        
        # Formater le terme selon la puissance
        if i == 0:  # Terme constant
            term = str(abs_coef)
        elif i == 1:  # Terme de degré 1
            term = symbol if abs_coef == 1 else f"{abs_coef}{symbol}"
        else:  # Termes de degré supérieur
            term = f"{symbol}^{{{i}}}" if abs_coef == 1 else f"{abs_coef}{symbol}^{{{i}}}"
            
        desc_latex += f"{sign}{term}"
    
    # Cas polynôme nul
    if desc_latex == "":
        desc_latex = "0"
        
    return [polynomial, asc_latex, desc_latex]

##===========================================================================================
##===========================================================================================
#                                   Début des essais                                      
##===========================================================================================
##===========================================================================================



# X = Symbol('X')


# ###Le coef constant n'est pas nul et l'ordre des monomes est croissant
# D = Poly_with_random_coef_v2('X',3,2)
# D_0 = D[0]
# D_1 = D[1]
# D_2 = D[2]

# print('D_0 =' , D_0,'\n')
# print('D_1 =' , D_1,'\n')
# print('D_2 =' , D_2,'\n')

#print('type(D_0) =' , type(D_0),'\n')




# Le coef constant n'est pas nul mais l'ordre des monomes est décroissant
# D = Poly_with_random_coef_v2('X',3,0)
# D_1 = D[0]
# D_2 = D[1]
# D_3 = D[2]

# print('D_1 =' , D_1,'\n')
# print('D_2 =' , D_2,'\n')
# print('D_3 =' , D_3,'\n')



   
##===========================================================================================
##===========================================================================================
#                                   Fin des essais                                      
##===========================================================================================
##===========================================================================================




# def Poly_with_given_list_of_coef(symbol, Lcoef):
#     """
#     Returns a list containing:
#     - A polynomial of degree deg in the indeterminate symbol, whose coefficients are the one given in the list L.
#       Additionally, the coefficient of the term X^deg is non-zero to ensure that the polynomial is indeed of degree deg.
#     - This polynomial written in TeX with the monomials given in ascending order.
#     - This polynomial written in TeX with the monomials given in descending order.

#     FR : renvoie une liste contenant
#     - un polynôme de degré deg en l'indéterminée symbol, dont les coefficients sont donnés par la liste L
#       De plus, le coefficient devant le terme X^deg est non nul de façon à ce que le polynôme soit bien de degré deg.
#     - Ce polynôme écrit en TeX (avec les monômes donnés par ordre croissant).
#     - Ce polynôme écrit en TeX (avec les monômes donnés par ordre décroissant).
#     """
#     L = []


#     for i in range(len(Lcoef)):
#         r = Lcoef[i]
#         L.append(r)

#     X = Symbol(symbol)
#     deg = len(Lcoef) - 1

#     # Construct the polynomial
#     U = L[0] * X**0
#     q_L_0 = L[0]
#     if q_L_0.is_integerl:
#         t =
#     elif q_L_0.is_Rational:
#         q_L_0_numerator = q_L_0.p
#         q_L_0_denominator = q_L_0.q
#         t = "\\"'frac{q_L_0_numerator}{q_L_0_denominator}'

#     U_latex = t if L[0] != 0 else ''

#     for i in range(1, deg + 1):
#         if L[i] == 0:
#             continue
#         U += L[i] * X**i
#         sign = '+' if L[i] > 0 and U_latex != '' else ''
#         if i == 1:
#             term = f"{symbol}" if L[i] == 1 else (f"-{symbol}" if L[i] == -1 else f"{L[i]}{symbol}")
#         else:
#             term = f"{symbol}^{{{i}}}" if L[i] == 1 else (f"-{symbol}^{{{i}}}" if L[i] == -1 else f"{L[i]}{symbol}^{{{i}}}")
#         U_latex += f"{sign}{term}"

#     # Construct the polynomial in descending order
#     V_latex = ""
#     for i in range(deg, -1, -1):
#         if L[i] == 0:
#             continue
#         sign = '' if V_latex == '' else ('+' if L[i] > 0 else '')
#         if i == 0:
#             term = f"{L[i]}"
#         elif i == 1:
#             term = f"{symbol}" if L[i] == 1 else (f"-{symbol}" if L[i] == -1 else f"{L[i]}{symbol}")
#         else:
#             term = f"{symbol}^{{{i}}}" if L[i] == 1 else (f"-{symbol}^{{{i}}}" if L[i] == -1 else f"{L[i]}{symbol}^{{{i}}}")
#         V_latex += f"{sign}{term}"

#     Polynomial = Poly(U, X)
#     Result = [Polynomial, U_latex, V_latex]

#     return Result

# ##===========================================================================================
# ##===========================================================================================
# #                                   Début des essais                                      
# ##===========================================================================================
# ##===========================================================================================



# X = Symbol('X')
# L = [1, Rational(2 , 3), 6, 4, 5]
# print('L =' , L,'\n')

# L_inv = L[::-1]
# print('L_inv =' , L_inv,'\n')

# ###Le coef constant n'est pas nul et l'ordre des monomes est croissant
# D = Poly_with_given_list_of_coef('X',L)
# D_0 = D[0]
# D_1 = D[1]
# D_2 = D[2]

# print('D_0 =' , D_0,'\n')
# print('D_1 =' , D_1,'\n')
# print('D_2 =' , D_2,'\n')

# #print('type(D_0) =' , type(D_0),'\n')


# r = Rational(3, 4)

# # Get the numerator
# numerator = r.p
# denominator = r.q
# print(numerator)

# # Get the denominator
# print(denominator)

# f = Rational(2, 3)

# if f.is_Rational:
#     f_numerator = f.p
#     f_denominator = f.q
#     t = "\\"'frac{f_numerator}{f_denominator}'

# print('t =' , t,'\n')

#"\\"'begin{align*}\n'


# Le coef constant n'est pas nul mais l'ordre des monomes est décroissant
# D = Poly_with_random_coef_v2('X',3,0)
# D_1 = D[0]
# D_2 = D[1]
# D_3 = D[2]

# print('D_1 =' , D_1,'\n')
# print('D_2 =' , D_2,'\n')
# print('D_3 =' , D_3,'\n')



   
##===========================================================================================
##===========================================================================================
#                                   Fin des essais                                      
##===========================================================================================
##===========================================================================================




##===========================================================================================
##===========================================================================================
#                                   Début des essais                                      
##===========================================================================================
##===========================================================================================











##===========================================================================================
##===========================================================================================
# 
#
#                                 New fction                                      
#
##===========================================================================================
##===========================================================================================



##===========================================================================================
##===========================================================================================
#                                   Fin des essais                                      
##===========================================================================================
##===========================================================================================





##===========================================================================================
##===========================================================================================
#                                   Début des essais                                      
##===========================================================================================
##===========================================================================================