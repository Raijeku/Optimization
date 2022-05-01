from sympy import *
import pandas as pd

def gradient_descent(x0, learn_rate, tolerance, function):
    x = Symbol('x')
    f = parse_expr(function)
    iteration = 0
    data = pd.DataFrame(columns=['iteration','x','f(x)','df(x)'])
    step_size = 1000
    x1 = x0

    while abs(step_size)>=tolerance:
        df = f.diff(x)
        dfx = df.subs(x,x1)
        fx = f.subs(x,x1)
        step_size = learn_rate * dfx
        data = data.append(pd.DataFrame({'iteration':[iteration],'x':[x1], 'f(x)':[fx], 'df(x)':[dfx]}), ignore_index = True)
        x1 -= step_size
        #print(data) 
        iteration += 1

    data.set_index('iteration', inplace=True)
    return data

#gradient_descent(9,0.1,0.01,'x**2-4*x+1')

