from sympy import *
import pandas as pd
from random import random

def random_optimization(xl, xu, n, function):
    x = Symbol('x')
    f = parse_expr(function)
    iteration = 0
    data = pd.DataFrame(columns=['iteration','xl','xu','x','f(x)','max_x','max_f(x)'])

    max_f = -1E9
    for i in range(n):
        r = random()
        x0 = xl + (xu - xl)*r
        df = f.diff(x)
        fx = f.subs(x, x0)
        dfx = df.subs(x, x0)
        if fx > max_f:
            max_f = fx
            max_x = x0
        data = data.append(pd.DataFrame({'iteration':[iteration], 'xl':[xl], 'xu':[xu], 'x':[x0], 'f(x)':[fx], 'max_x':[max_x], 'max_f(x)':[max_f], 'error':[dfx]}), ignore_index = True)
        iteration += 1

    return data

def multivariable_random_optimization(xl, xu, yl, yu, n, function):
    x = Symbol('x')
    y = Symbol('y')
    f = parse_expr(function)
    iteration = 0
    data = pd.DataFrame(columns=['iteration','xl','xu','x','yl','yu','y','f(x,y)','max_x','max_y','max_f(x,y)'])

    max_f = -1E9
    for i in range(n):
        r = random()
        x0 = xl + (xu - xl)*r
        r = random()
        y0 = yl + (yu - yl)*r
        df = f.diff(x)
        fx = f.subs(x, x0)
        fxy = fx.subs(y, y0)
        if fxy > max_f:
            max_f = fxy
            max_x = x0
            max_y = y0
        data = data.append(pd.DataFrame({'iteration':[iteration], 'xl':[xl], 'xu':[xu], 'x':[x0], 'yl':[yl], 'yu':[yu], 'y':[y0], 'f(x,y)':[fxy], 'max_x':[max_x], 'max_y':[max_y], 'max_f(x,y)':[max_f]}), ignore_index = True)
        iteration += 1

    return data

print(random_optimization(-3,2,100,'-x**2'))
print(multivariable_random_optimization(-2,2,-2,2,100,'4*x+2*y+x**2-2*x**4+2*x*y-3*y**2'))
