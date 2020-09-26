from sympy import *
import pandas as pd

def biseccion(xl, xu, tolerance, function):
    x = Symbol('x')
    f = parse_expr(function)
    iteration = 0
    data = pd.DataFrame(columns=['iteration','xl','xu','xr','f(xl)','f(xu)','f(xr)','f(xl)f(xr)','error'])

    while abs(xu-xl)>=tolerance:
        xr = (xl + xu)/2
        fxl = f.subs(x, xl)
        fxu = f.subs(x, xu)
        fxr = f.subs(x, xr)

        data = data.append(pd.DataFrame({'iteration':[iteration], 'xl':[xl], 'xu':[xu], 'xr':[xr], 'f(xl)':[fxl], 'f(xu)':[fxu], 'f(xr)':[fxr], 'f(xl)f(xr)':[fxl*fxr], 'error':[abs(xu-xl)]}), ignore_index = True)

        if fxl*fxr<0:
            xu = xr
        elif fxl*fxr>0:
            xl = xr
    
        iteration += 1

    data.set_index('iteration', inplace=True)
    return data

print(biseccion(10, 50, 0.01, '3*x**2 - 120*x + 100'))