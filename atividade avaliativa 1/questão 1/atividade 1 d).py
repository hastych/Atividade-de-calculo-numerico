import math

def f(x):
    return x**3 - 5*x - 9

def bissecao(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Teorema de Bolzano não satisfeito!")
        return None
    
    print("="*70)
    print(f"{'Iteração':<10} {'a':<12} {'b':<12} {'xm':<12} {'f(xm)':<14} {'Erro':<10}")
    print("-"*70)
    
    for i in range(max_iter):
        xm = (a + b) / 2
        erro = (b - a) / 2
        
        print(f"{i+1:<10} {a:<12.6f} {b:<12.6f} {xm:<12.6f} {f(xm):<14.8f} {erro:<10.8f}")
        
        if erro < tol or f(xm) == 0:
            return xm, i+1
        
        if f(a) * f(xm) < 0:
            b = xm
        else:
            a = xm
    
    return xm, max_iter

# Execução
raiz, iteracoes = bissecao(f, 2, 3, 1e-6)
print(f"\nRaiz aproximada: {raiz:.8f}")
print(f"Número de iterações: {iteracoes}")