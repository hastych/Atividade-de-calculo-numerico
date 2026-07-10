import time
import math

# ============ FUNÇÕES ============
def f_questao1(x):
    return x**3 - 5*x - 9

def f_questao2(x):
    return x**3 - 4*x - 9

def f_questao3(x):
    return math.exp(-x) - x

def f_questao4(x):
    return x**3 - 6*x + 2

def f_questao5(x):
    return x**3 - 2*x - 5

# ============ MÉTODOS ============
def bissecao(f, a, b, tol=1e-6):
    start = time.time()
    iteracoes = 0
    
    if f(a) * f(b) >= 0:
        return None, iteracoes, float('inf'), 0
    
    while (b - a) / 2 > tol:
        xm = (a + b) / 2
        iteracoes += 1
        
        if f(xm) == 0:
            break
        
        if f(a) * f(xm) < 0:
            b = xm
        else:
            a = xm
    
    end = time.time()
    return (a + b) / 2, iteracoes, (b - a) / 2, (end - start) * 1000

def posicao_falsa(f, a, b, tol=1e-6):
    start = time.time()
    iteracoes = 0
    
    if f(a) * f(b) >= 0:
        return None, iteracoes, float('inf'), 0
    
    for i in range(1000):
        xm = (a*f(b) - b*f(a)) / (f(b) - f(a))
        iteracoes += 1
        erro = abs(f(xm))
        
        if erro < tol:
            break
        
        if f(a) * f(xm) < 0:
            b = xm
        else:
            a = xm
    
    end = time.time()
    return xm, iteracoes, erro, (end - start) * 1000

def ponto_fixo(g, x0, tol=1e-6):
    start = time.time()
    iteracoes = 0
    x = x0
    
    for i in range(1000):
        x_new = g(x)
        iteracoes += 1
        erro = abs(x_new - x)
        
        if erro < tol:
            break
        x = x_new
    
    end = time.time()
    return x, iteracoes, erro, (end - start) * 1000

def newton_raphson(f, df, x0, tol=1e-6):
    start = time.time()
    iteracoes = 0
    x = x0
    
    for i in range(1000):
        x_new = x - f(x) / df(x)
        iteracoes += 1
        erro = abs(x_new - x)
        
        if erro < tol:
            break
        x = x_new
    
    end = time.time()
    return x, iteracoes, erro, (end - start) * 1000

# ============ EXECUÇÃO ============
def f(x): return x**3 - 5*x - 9
def df(x): return 3*x**2 - 5
def g(x): return (1 - x)**(1/3)

print("="*85)
print("COMPARAÇÃO DE MÉTODOS NUMÉRICOS")
print("="*85)
print(f"{'Método':<20} {'Raiz':<20} {'Iterações':<12} {'Erro final':<15} {'Tempo (ms)':<12}")
print("-"*85)

# Bisseção
raiz_b, it_b, erro_b, tempo_b = bissecao(f, 2, 3)
print(f"{'Bisseção':<20} {raiz_b:<20.8f} {it_b:<12} {erro_b:<15.8f} {tempo_b:<12.4f}")

# Posição Falsa
raiz_pf, it_pf, erro_pf, tempo_pf = posicao_falsa(f, 2, 3)
print(f"{'Posição Falsa':<20} {raiz_pf:<20.8f} {it_pf:<12} {erro_pf:<15.8f} {tempo_pf:<12.4f}")

# Ponto Fixo
raiz_pf2, it_pf2, erro_pf2, tempo_pf2 = ponto_fixo(g, 0.5)
print(f"{'Ponto Fixo':<20} {raiz_pf2:<20.8f} {it_pf2:<12} {erro_pf2:<15.8f} {tempo_pf2:<12.4f}")

# Newton-Raphson
raiz_nr, it_nr, erro_nr, tempo_nr = newton_raphson(f, df, 2.5)
print(f"{'Newton-Raphson':<20} {raiz_nr:<20.8f} {it_nr:<12} {erro_nr:<15.8f} {tempo_nr:<12.4f}")

print("="*85)