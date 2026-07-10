def f4(v):
    return v**3 - 6*v + 2

def posicao_falsa(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Teorema de Bolzano não satisfeito!")
        return None
    
    print("="*80)
    print(f"{'Iter':<6} {'a':<14} {'b':<14} {'xm':<14} {'f(xm)':<16} {'Erro':<12}")
    print("-"*80)
    
    for i in range(max_iter):
        xm = (a*f(b) - b*f(a)) / (f(b) - f(a))
        erro = abs(b - a)
        
        print(f"{i+1:<6} {a:<14.8f} {b:<14.8f} {xm:<14.8f} {f(xm):<16.8f} {erro:<12.8f}")
        
        if abs(f(xm)) < tol or erro < tol:
            return xm, i+1
        
        if f(a) * f(xm) < 0:
            b = xm
        else:
            a = xm
    
    return xm, max_iter

# Execução
raiz4, iter4 = posicao_falsa(f4, 0, 1)
print(f"\nRaiz: {raiz4:.8f} | Iterações: {iter4}")