import math

def f3(C):
    return math.exp(-C) - C

# Usar a mesma função bissecao_completa
raiz3, iter3 = bissecao_completa(f3, 0, 1)
print(f"\nRaiz: {raiz3:.8f} | Iterações: {iter3}")