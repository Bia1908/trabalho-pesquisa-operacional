from pulp import *

prob = LpProblem("Moveis_Modulados", LpMaximize)

x1 = LpVariable("Armarios", 0, None, LpInteger)
x2 = LpVariable("Estantes", 0, None, LpInteger)
x3 = LpVariable("Gaveteiros", 0, None, LpInteger)

prob += 150*x1 + 100*x2 + 80*x3

prob += 10*x1 + 5*x2 + 4*x3 <= 200  # Limite de MDF
prob += 6*x1 + 3*x2 + 2*x3 <= 120   # Limite de horas de montagem
prob += x1 >= 5                     # Mínimo de Armários
prob += x2 >= 5                     # Mínimo de Estantes
prob += x3 >= 5                     # Mínimo de Gaveteiros
prob += x1 <= 15                    # Máximo de Armários
prob += x2 + x3 <= 30               # Logística 

prob.solve()

print("Lucro Máximo:", value(prob.objective))
print("Armarios (x1):", x1.varValue)
print("Estantes (x2):", x2.varValue)
print("Gaveteiros (x3):", x3.varValue)