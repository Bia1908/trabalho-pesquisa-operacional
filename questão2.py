from pulp import *

prob = LpProblem("Marcenaria", LpMaximize)

x1 = LpVariable("Mesas", 0, None, LpInteger)
x2 = LpVariable("Cadeiras", 0, None, LpInteger)

prob += 50*x1 + 30*x2

prob += 5*x1 + 2*x2 <= 100  # Madeira
prob += 4*x1 + 2*x2 <= 60   # Mão de Obra
prob += 1*x1 + 1*x2 <= 25   # Verniz


prob.solve()

print("Lucro Máximo:", value(prob.objective))
print("Quantidade de Mesas (x1):", x1.varValue)
print("Quantidade de Cadeiras (x2):", x2.varValue)