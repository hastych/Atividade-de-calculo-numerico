import math

def g_forma1(x):
    return 1 - x**3

def g_forma2(x):
    return (1 - x)**(1/3)

def g_forma3(x):
    return 1/(x**2 + 1)

def ponto_fixo(g, x0, tol=1e-6, max_iter=100):
    print("="*70)
    print(f"{'Iteração':<10} {'x':<18} {'g(x)':<18} {'Erro':<12}")
    print("-"*70)
    
    x = x0
    print(f"{0:<10} {x:<18.8f} {'-':<18} {'-':<12}")
    
    for i in range(max_iter):
        x_new = g(x)
        erro = abs(x_new - x)
        print(f"{i+1:<10} {x_new:<18.8f} {g(x_new):<18.8f} {erro:<12.8f}")
        
        if erro < tol:
            return x_new, i+1
        
        x = x_new
    
    return x, max_iter

print("Forma 2: x = (1-x)^(1/3)")
raiz6, iter6 = ponto_fixo(g_forma2, 0.5)
print(f"\nRaiz aproximada: {raiz6:.8f}")