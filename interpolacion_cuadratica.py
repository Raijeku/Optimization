from sympy import *
import pandas as pd

def interpolacion_cuadratica(x0, x1, x2, tolerance, function):
    x = Symbol('x')
    f = parse_expr(function)
    iteration = 0
    data = pd.DataFrame(columns=['iteration','x0','x1','x2','x3','f(x0)','f(x1)','f(x2)','f(x3)'])
    fx0 = float(f.subs(x, x0))
    fx1 = float(f.subs(x, x1))
    fx2 = float(f.subs(x, x2))
    x3 = float((fx0*((x1**2)-(x2**2)) + fx1*((x2**2)-(x1**2)) + fx2*((x0**2)-(x1**2)))/(2*(fx0*(x1-x2) + fx1*(x2-x1) + fx2*(x0-x1))))
    fx3 = float(f.subs(x, x3))

    while abs(x3-x1) >=0.01:  
        previous_x3 = x3

        data = data.append(pd.DataFrame({'iteration':[iteration], 'x0':[x0], 'x1':[x1], 'x2':[x2], 'x3':[x3], 'f(x0)':[fx0], 'f(x1)':[fx1], 'f(x2)':[fx2], 'f(x3)':[fx3], 'error':[abs(x3-x1)]}), ignore_index = True)
        if fx3>fx1:
            if x3>x1:
                x0 = x1
                x1 = x3
            elif x3<x1:
                x2 = x1
                x1 = x3
        iteration += 1
        
        fx0 = float(f.subs(x, x0))
        fx1 = float(f.subs(x, x1))
        fx2 = float(f.subs(x, x2))
        nx3 = fx0*((x1**2)-(x2**2)) + fx1*((x2**2)-(x1**2)) + fx2*((x0**2)-(x1**2))
        dx3 = 2*(fx0*(x1-x2) + fx1*(x2-x1) + fx2*(x0-x1))
        x3 = float(nx3/dx3)
        fx3 = float(f.subs(x, x3))
        
        if previous_x3==x3:
          print("No se encontró solución con los puntos iniciales dados.")
          break

    data.set_index('iteration', inplace=True)
    return data

print(interpolacion_cuadratica(1.75, 2, 2.5, 0.01, '4*x-1.8*x**2+1.2*x**3-0.3*x**4'))