from sympy import *
import pandas as pd

def simplex(function, expressions):
    x0 = 0
    y0 = 0
    function = parse_expr(function)
    coefficients = function.as_coefficients_dict()
    greatest_var = ''
    greatest_coefficient = -1E9
    for coefficient in coefficients:
        if coefficients[coefficient] > greatest_coefficient:
            greatest_coefficient = coefficients[coefficient]
            greatest_var = coefficient
    print(greatest_var)
    print(coefficients)
    x = Symbol('x')
    y = Symbol('y')
    operators = ['<=','>=','<','>']
    inequalities = [[] for operator in operators]
    for expression in expressions:
        for i, operator in enumerate(operators):
            if operator in expression:
                expression_list = expression.split(operator)
                inequalities[i].append((parse_expr(expression_list[0]).as_coefficients_dict(),operator,float(expression_list[1])))
                break
    print(inequalities)

simplex('5*x+3*y',['5*x+3*y>4','2*x-5*y<3','45+x>=5'])
