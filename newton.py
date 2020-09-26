from sympy import *
import pandas as pd

def newton(x0, tolerance, function):
    x = Symbol('x')
    f = parse_expr(function)
    iteration = 0
    data = pd.DataFrame(columns=['iteration','x','df(x)','ddf(x)'])
    dfx = 1000

    while abs(dfx)>=tolerance:
        df = f.diff(x)
        ddf = df.diff(x)
        dfx = df.subs(x,x0)
        ddfx = ddf.subs(x,x0)
        x1 = x0 - dfx/ddfx
        data = data.append(pd.DataFrame({'iteration':[iteration],'x':[x0], 'df(x)':[dfx], 'ddf(x)':[ddfx], 'error':[abs(dfx)]}), ignore_index = True)
        iteration = iteration + 1
        x0 = x1

    data.set_index('iteration', inplace=True)
    return data

print(newton(6,0.01,'x**3'))

