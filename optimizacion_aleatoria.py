from sympy import *
import pandas as pd
from random import random

def optimizacion_aleatoria(xl, xu, n, function):
    x = Symbol('x')
    f = parse_expr(function)
    iteration = 0
    data = pd.DataFrame(columns=['iteration','xl','xu','x','f(x)','max_x','max_f(x)','error'])

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

print(optimizacion_aleatoria(-3,2,100,'-x**2'))