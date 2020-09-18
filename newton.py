from sympy import *
import pandas as pd

def newton(x0, tolerance, function):
    x = Symbol('x')
    parse_expr(function)
    f = x**3
    iteration = 0
    data = pd.DataFrame(columns=['iteration','x','df(x)','ddf(x)'])

    while abs(x0)>=tolerance:
        df = f.diff(x)
        ddf = df.diff(x)
        dfx = df.subs(x,x0)
        ddfx = ddf.subs(x,x0)
        x1 = x0 - dfx/ddfx
        data = data.append(pd.DataFrame({'iteration':[iteration],'x':[x0], 'df(x)':[dfx], 'ddf(x)':[ddfx]}), ignore_index = True)
        iteration = iteration + 1
        x0 = x1

    data.set_index('iteration', inplace=True)
    return data

print(newton(6,0.01,'x**3'))

