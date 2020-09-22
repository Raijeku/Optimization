from sympy import *
import pandas as pd

def seccion_dorada(xl, xu, tolerance, function):
    x = Symbol('x')
    f = parse_expr(function)
    iteration = 0
    data = pd.DataFrame(columns=['iteration','xl','xu','x1','x2','f(x1)','f(x2)','error'])

    while abs(xu-xl) > tolerance:
        fxl = f.subs(x, xl)
        fxu = f.subs(x, xu)
        d = 0.618*(xu-xl)
        x1 = xl + d
        x2 = xu - d
        fx1 = f.subs(x, x1)
        fx2 = f.subs(x, x2)

        data = data.append(pd.DataFrame({'iteration':[iteration],'xl':[xl], 'xu':[xu], 'x1':[x1], 'x2':[x2],'f(x1)':[fx1], 'f(x2)':[fx2], 'error':[abs(xu-xl)]}), ignore_index = True)

        if fx2>fx1:
            xu = x1
        elif fx1>=fx2:
            xl = x2
        iteration += 1
    
    data.set_index('iteration', inplace=True)
    return data
        
print(seccion_dorada(0,4,0.01,'2*sin(x)-((x**2)/10)'))
