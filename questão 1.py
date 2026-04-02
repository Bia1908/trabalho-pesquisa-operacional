from pulp import *

prob = LpProblem("Confeitaria", LpMaximize)

x1 = LpVariable("Chocolate", 0, None, LpInteger)
x2 = LpVariable("Baunilha", 0, None, LpInteger)

prob += 20*x1 + 15*x2

prob += 2*x1 + 1*x2 <= 20  # Farinha
prob += 3*x1 + 3*x2 <= 36  # Ovos
prob += 1*x1 + 2*x2 <= 16  # Tempo

prob.solve()

print("Lucro:", value(prob.objective))
print("Quantidade de Bolos de Chocolate (x1):", x1.varValue)
print("Quantidade de Bolos de Baunilha (x2):", x2.varValue)