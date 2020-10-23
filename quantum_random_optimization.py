from sympy import *
import pandas as pd
from qiskit import execute, IBMQ, circuit, QuantumCircuit
from qiskit.tools.monitor import job_monitor

def quantum_random_optimization(xl, xu, n, function, backend_name):
    x = Symbol('x')
    f = parse_expr(function)
    iteration = 0
    data = pd.DataFrame(columns=['iteration','xl','xu','x','f(x)','max_x','max_f(x)','error'])
    rs = generate_random(n, backend_name)

    max_f = -1E9
    max_x = -1E9
    for i in range(n):
        r = rs[i]
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

def generate_random(n, backend_name):
    provider = IBMQ.load_account()
    provider = IBMQ.get_provider(hub='ibm-q-ornl', group='ornl', project='phy141')
    backend = provider.get_backend(backend_name)
    backend_config = backend.configuration()
    num_qubits = backend_config.n_qubits

    circuit = QuantumCircuit(num_qubits,num_qubits)
    for i in range(num_qubits):
        circuit.h(i)
    circuit.measure([i for i in range(num_qubits)],[i for i in range(num_qubits)])
    job = execute(circuit, backend, shots = 8192)
    job_monitor(job)
    result = job.result()
    counts = result.get_counts()

    random_numbers = []
    for key in counts:
        if len(random_numbers) < n:
            random_numbers.append(int(key, 2)/(2**num_qubits))
        else:
            break
    
    return random_numbers

print(quantum_random_optimization(-3,2,100,'-x**2','ibmq_manhattan'))