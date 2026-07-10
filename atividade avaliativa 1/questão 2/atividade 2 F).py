def f2(I):
    return I**3 - 4*I - 9

def bissecao_completa(f, a, b, tol=1e-6):
    if f(a) * f(b) >= 0:
        return None
    
    print("="*80)
    print(f"{'Iter':<6} {'a':<14} {'b':<14} {'xm':<14} {'f(xm)':<16} {'Erro':<12}")
    print("-"*80)
    
    i = 1
    x_anterior = a
    
    while True:
        xm = (a + b) / 2
        erro = abs(xm - x_anterior)
        
        print(f"{i:<6} {a:<14.8f} {b:<14.8f} {xm:<14.8f} {f(xm):<16.8f} {erro:<12.8f}")
        
        if (b - a) / 2 < tol or f(xm) == 0:
            return xm, i
        
        if f(a) * f(xm) < 0:
            b = xm
        else:
            a = xm
        
        x_anterior = xm
        i += 1

# Execução
raiz2, iter2 = bissecao_completa(f2, 2, 3)
print(f"\nRaiz: {raiz2:.8f} | Iterações: {iter2}")