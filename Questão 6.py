from pulp import *

prob = LpProblem("Tintas", LpMaximize)

x1 = LpVariable("Fachadas", 0, None, LpInteger)
x2 = LpVariable("Interiores", 0, None, LpInteger)

prob += 10 * x1 + 8 * x2

prob += 6 * x1 + 4 * x2 <= 24
prob += 1 * x1 + 2 * x2 <= 6
prob += x2 <= x1 + 1
prob += x2 <= 2
prob += x1 + x2 <= 5
prob.solve()

print("Status:", LpStatus[prob.status])
print("Fachadas:", x1.varValue)
print("Interiores:", x2.varValue)
print("Lucro máximo:", value(prob.objective))
