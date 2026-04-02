from pulp import *

prob = LpProblem("Brinquedos", LpMaximize)

x1 = LpVariable("Carrinhos", 0, None, LpInteger)
x2 = LpVariable("Bonecas", 0, None, LpInteger)

prob += 12 * x1 + 10 * x2

prob += 3 * x1 + 2 * x2 <= 60
prob += 2 * x1 + 1 * x2 <= 40
prob += 1 * x1 + 1 * x2 <= 30

prob.solve()

print("Status:", LpStatus[prob.status])
print("Carrinhos:", x1.varValue)
print("Bonecas:", x2.varValue)
print("Lucro máximo:", value(prob.objective))