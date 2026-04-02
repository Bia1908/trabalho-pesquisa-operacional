from pulp import *

prob = LpProblem("Uniformes", LpMaximize)

x1 = LpVariable("Futebol", 0, None, LpInteger)
x2 = LpVariable("Basquete", 0, None, LpInteger)

prob += 40 * x1 + 30 * x2

prob += 3 * x1 + 2 * x2 <= 30
prob += 2 * x1 + 3 * x2 <= 24
prob += x1 >= 2
prob += x1 + x2 <= 10
prob += x2 <= 6 

prob.solve()

print("Status:", LpStatus[prob.status])
print("Futebol:", x1.varValue)
print("Basquete:", x2.varValue)
print("Lucro máximo:", value(prob.objective))