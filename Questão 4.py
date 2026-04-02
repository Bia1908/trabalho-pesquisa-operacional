from pulp import *

prob = LpProblem("Oficina_Bicicletas", LpMaximize)

x1 = LpVariable("Montanha", 0, None, LpInteger)
x2 = LpVariable("Passeio", 0, None, LpInteger)

prob += 80*x1 + 60*x2

prob += 2*x1 + 1*x2 <= 20  # Kits de engrenagem
prob += 3*x1 + 3*x2 <= 45  # Tempo de montagem (horas)
prob += 1*x1 + 1*x2 <= 12  # Espaço no galpão (m²)

prob.solve()

print("Lucro Máximo:", value(prob.objective))
print("Bicicletas de Montanha (x1):", x1.varValue)
print("Bicicletas de Passeio (x2):", x2.varValue)
