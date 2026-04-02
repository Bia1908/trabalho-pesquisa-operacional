from pulp import *

prob = LpProblem("Dispositivos_Eletronicos", LpMaximize)

x1 = LpVariable("Tablets", 0, None, LpInteger)
x2 = LpVariable("Smartphones", 0, None, LpInteger)

prob += 100*x1 + 120*x2

prob += 4*x1 + 2*x2 <= 40   # Tempo de montagem
prob += 1*x1 + 2*x2 <= 16   # Teste de qualidade
prob += x2 <= 2*x1          # Diversidade do catálogo 
prob += x1 <= 8             # Limite do contrato de telas para tablets
prob += x1 + x2 >= 5        # Otimização de frete 

prob.solve()

print("Lucro Máximo:", value(prob.objective))
print("Tablets (x1):", x1.varValue)
print("Smartphones (x2):", x2.varValue)
