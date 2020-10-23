from sympy import *
import pandas as pd

def polynomial_interpolation(x0, x1, x2, tolerance, function, criteria = 'max'):
    x = Symbol('x')
    f = parse_expr(function)
    iteration = 0
    data = pd.DataFrame(columns=['iteration','x0','x1','x2','x3','f(x0)','f(x1)','f(x2)','f(x3)'])
    fx0 = float(f.subs(x, x0))
    fx1 = float(f.subs(x, x1))
    fx2 = float(f.subs(x, x2))
    
    if criteria == 'max':
        nx3 = fx0*((x1**2)-(x2**2)) + fx1*((x2**2)-(x0**2)) + fx2*((x0**2)-(x1**2))
        dx3 = 2*(fx0*(x1-x2) + fx1*(x2-x0) + fx2*(x0-x1))
        x3 = float(nx3/dx3)
    elif criteria == 'min':
        nx3 = (((x1-x0)**2)*(fx1-fx2)-((x1-x2)**2)*(fx1-fx0))
        dx3 = 2*((x1-x0)*(fx1-fx2)-(x1-x2)*(fx1-fx0))
        x3 = float(x1-nx3/dx3)
    fx3 = float(f.subs(x, x3))
    data = data.append(pd.DataFrame({'iteration':[iteration], 'x0':[x0], 'x1':[x1], 'x2':[x2], 'x3':[x3], 'f(x0)':[fx0], 'f(x1)':[fx1], 'f(x2)':[fx2], 'f(x3)':[fx3], 'error':[abs(x3-x1)]}), ignore_index = True)

    while abs(x3-x1) >=tolerance:  
        previous_x3 = x3

        if criteria == 'max':
            if fx3>fx1:
                if x3>x1:
                    x0 = x1
                    x1 = x3
                elif x3<x1:
                    x2 = x1
                    x1 = x3
            else:
                x1 = x3
        elif criteria == 'min':
            if fx3<fx1:
                if x3>x1:
                    x0 = x1
                    x1 = x3
                elif x3<x1:
                    x2 = x1
                    x1 = x3
            else:
                x1 = x3
        iteration += 1
        
        fx0 = float(f.subs(x, x0))
        fx1 = float(f.subs(x, x1))
        fx2 = float(f.subs(x, x2))
        if criteria == 'max':
            nx3 = fx0*((x1**2)-(x2**2)) + fx1*((x2**2)-(x0**2)) + fx2*((x0**2)-(x1**2))
            dx3 = 2*(fx0*(x1-x2) + fx1*(x2-x0) + fx2*(x0-x1))
            x3 = float(nx3/dx3)
        elif criteria == 'min':
            nx3 = (((x1-x0)**2)*(fx1-fx2)-((x1-x2)**2)*(fx1-fx0))
            dx3 = 2*((x1-x0)*(fx1-fx2)-(x1-x2)*(fx1-fx0))
            x3 = float(x1-nx3/dx3)
        fx3 = float(f.subs(x, x3))

        data = data.append(pd.DataFrame({'iteration':[iteration], 'x0':[x0], 'x1':[x1], 'x2':[x2], 'x3':[x3], 'f(x0)':[fx0], 'f(x1)':[fx1], 'f(x2)':[fx2], 'f(x3)':[fx3], 'error':[abs(x3-x1)]}), ignore_index = True)
        
        if previous_x3==x3:
            print("No se encontró solución con los puntos iniciales dados.")
            break

    data.set_index('iteration', inplace=True)
    return data

print(polynomial_interpolation(0.1, 0.5, 5, 0.01, '2*x + 3/x', 'min'))