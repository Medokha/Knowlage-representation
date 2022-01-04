# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 10:47:06 2022

@author: Dell
"""
from logic2 import *


# question 1.1
# in English : Carrots color is orange
carrots = Symbol("carrots")
orange = Symbol("orange")
knowledge_for_question1 = And(
    Implication(carrots, orange)
)
# print(knowledge_for_question1.formula())  # print the output formula of knowledge base
#---------------------------------------------------


# question 1.2
# in English : " if person is vegetarian , person likes carrots "
person = Symbol("person")
vegetarian = Symbol("vegetarian(x)")
like = Symbol("like")
like_person_carrots = Symbol("like(x, carrots)")
knowledge_for_question2 = And(Implication(vegetarian, like_person_carrots))
# print(knowledge_for_question2.formula())  # print the output formula of knowledge base
#---------------------------------------------------

# question 1.3
# in English : " student pass if he studies hard "
pass_exam = Symbol("pass(x)")
study_hard = Symbol("study_hard(x)")
knowledge_for_question3 = Implication(study_hard, pass_exam)
# print(knowledge_for_question3.formula())  # print the output formula of knowledge base
#---------------------------------------------------

# question 1.4
# in English : " who will pass? "
Pass = Symbol("? pass(who)")
knowledge_for_question4 = And(Pass)
# print(knowledge_for_question4.formula())  # print the output formula of knowledge base
#---------------------------------------------------

# question 1.5
# in English : " which course teacher teach ? "
teaches = Symbol("? teaches(course, which)")
knowledge_for_question5 = And(teaches)
# print(knowledge_for_question5.formula())   # print the output formula of knowledge base
#---------------------------------------------------
# question 1.6
# in English : " if x & y are enemies, x hate y and x fight y "
x = Symbol("x")
y = Symbol("y")
enemies = Symbol(f"enemies({x}, {y})")
hates = Symbol(f"hates({x}, {y})")
fight = Symbol(f"fight({x}, {y})")
knowledge_for_question6 = And(Implication(enemies, And(hates, fight)))
# print(knowledge_for_question6.formula()) # print the output formula of knowledge base
# =============================================================================
# 
# =============================================================================
from utils import *
from logic2 import *

# question 2.1
#  read(maria, logic programming book) ==> by(peter lucas)
maria = Symbol("maria")
peter_lucas = Symbol("peter lucas")
read = Symbol(f" read ({maria}, logic programming book)")
by = Symbol(f"by ({peter_lucas})")
knowledge_for_question1 = And(Implication(read, by))
# print(knowledge_for_question1.formula())

#-----------------------------------------------------------

# question 2.2
# is_girl(x) ==> like(x, shopping)
is_girl = Symbol("is_girl(x)")
shopping = Symbol("shopping")
like = Symbol(f"like(x, {shopping} )")
knowledge_for_question2 = And(Implication(is_girl, like))
# print(knowledge_for_question2.formula())

#-----------------------------------------------------------
# question 2.3
# ? likes( x , shopping)
who = Symbol("?")
knowledge_for_question3  = And(who ,like)
# print(knowledge_for_question3.formula())
#-----------------------------------------------------------
# question 2.4
# city( x ,big , crowdy) ==> hates(kirke, x)
city = Symbol("city(x, big, crowdy)")
hates = Symbol("kirke, x")
knowledge_for_question4 = And(Implication(city, hates))
# print(knowledge_for_question4.formula())
# =============================================================================
# 
# =============================================================================
from utils import *
from logic2 import *


""""
question 3.1
  hates(x,y), hates(y,x) ==> enemies(x, y)
  the correct 
  
  enemies(x, y) ==> hates(x, y) ^ hates(y, x)
  with python :
"""
x = Symbol("x")
y = Symbol("y")
enemies = Symbol(f"enemies({x}, {y})")
hates1 = Symbol(f"hates({x}, {y})")
hates2 = Symbol(f"hates({y}, {x})")
knowledge_for_question1 = And(Implication(enemies, And(hates1, hates2)))
# print(knowledge_for_question1.formula())

#------------------------------------------------------------------------
"""
question 3.2:
        p(X) ==> (q(X) ==> r(X)).
        the correct:
        p(x) ==> (q(x) ^ r(x))
with python:
     
"""

p = Symbol("p(x)")
q = Symbol("q(x)")
r = Symbol("r(x)")
knowledge_for_question2 = And(Implication(p , And(q, r)))
# print(knowledge_for_question2.formula())

# =============================================================================
#======================================================================

import utils
from logic import *

""""
    answer for question 4
"""


clauses = [expr("Man(John)"), expr("Women(Jia)"), expr("Healthy(John)"), expr("Wealthy(John)"), expr("Wealthy(Jia)")
    ,expr("(Wealthy(x) & Healthy(x)) ==> Traveler(x)")]

KB = FolKB(clauses)
wealthy = fol_bc_ask(KB, expr("Wealthy(x)"))
healthy = fol_bc_ask(KB, expr("Healthy(x)"))
traveler = fol_bc_ask(KB, expr("Traveler(x)"))
print('Who are healthy ?')
print(list(healthy), '\n')
print('Who are wealthy ?')
print(list(wealthy), '\n')
print('Who can travel ?')
print(list(traveler))
