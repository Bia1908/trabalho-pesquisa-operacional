from pulp import *

prob = LpProblem("Sucos", LpMaximize)

x1 = LpVariable("Laranja", 0, None, LpInteger)
x2 = LpVariable("Melancia", 0, None, LpInteger)

prob += 8 * x1 + 6 * x2

prob += 10 * x1 + 2 * x2 <= 100
prob += 5 * x1 + 10 * x2 <= 120
prob += x1 + x2 <= 20

prob.solve()

print("Status:", LpStatus[prob.status])
print("Laranja:", x1.varValue)
print("Melancia:", x2.varValue)
print("Lucro máximo:", value(prob.objective))
