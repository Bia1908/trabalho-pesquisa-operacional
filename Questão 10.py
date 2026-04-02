from pulp import *

prob = LpProblem("Dieta_Gado", LpMinimize)

x1 = LpVariable("Milho", 0)
x2 = LpVariable("Soja", 0)
x3 = LpVariable("Suplemento", 0)

prob += 2*x1 + 5*x2 + 12*x3

prob += 5*x1 + 20*x2 + 10*x3 >= 400     # Mínimo de proteína
prob += 30*x1 + 10*x2 + 5*x3 >= 600     # Mínimo de energia 
prob += x1 + x2 + x3 <= 100             # Limite técnico de peso do lote
prob += x3 <= 0.10 * (x1 + x2 + x3)     # Toxicidade 
prob += x1 >= 2*x2                      # Palatabilidade 

prob.solve()

print("Custo Mínimo Total: R$", round(value(prob.objective), 2))
print("Quantidade de Milho (x1):", round(x1.varValue, 2), "kg")
print("Quantidade de Soja (x2):", round(x2.varValue, 2), "kg")
print("Quantidade de Suplemento (x3):", round(x3.varValue, 2), "kg")
