import numpy as np
import matplotlib.pyplot as plt
import math

# ============ FUNÇÕES PRÉ-DEFINIDAS ============
def f_poli1(x): return x**3 - 5*x - 9
def f_poli2(x): return x**3 - 4*x - 9
def f_exp(x): return math.exp(-x) - x
def f_poli3(x): return x**3 - 6*x + 2
def f_poli4(x): return x**3 - 2*x - 5
def f_poli5(x): return x**3 + x - 1

def g_ponto_fixo(x): return (1 - x)**(1/3)

funcoes = {
    '1': {'f': f_poli1, 'nome': 'x³ - 5x - 9', 'intervalo': (2, 3)},
    '2': {'f': f_poli2, 'nome': 'x³ - 4x - 9', 'intervalo': (2, 3)},
    '3': {'f': f_exp, 'nome': 'e^(-x) - x', 'intervalo': (0, 1)},
    '4': {'f': f_poli3, 'nome': 'x³ - 6x + 2', 'intervalo': (0, 1)},
    '5': {'f': f_poli4, 'nome': 'x³ - 2x - 5', 'intervalo': (2, 3)},
    '6': {'f': f_poli5, 'nome': 'x³ + x - 1', 'intervalo': (0, 1)}
}

# ============ MÉTODOS ============
def bissecao_completo(f, a, b, tol, max_iter):
    tabela = []
    
    if f(a) * f(b) >= 0:
        print("Teorema de Bolzano não satisfeito!")
        return tabela, None
    
    for i in range(max_iter):
        xm = (a + b) / 2
        erro_abs = (b - a) / 2
        erro_rel = erro_abs / abs(xm) if xm != 0 else float('inf')
        
        tabela.append({
            'iter': i+1,
            'x': xm,
            'f(x)': f(xm),
            'erro_abs': erro_abs,
            'erro_rel': erro_rel
        })
        
        if erro_abs < tol or f(xm) == 0:
            break
        
        if f(a) * f(xm) < 0:
            b = xm
        else:
            a = xm
    
    return tabela, xm

def posicao_falsa_completo(f, a, b, tol, max_iter):
    tabela = []
    
    if f(a) * f(b) >= 0:
        print("Teorema de Bolzano não satisfeito!")
        return tabela, None
    
    for i in range(max_iter):
        xm = (a*f(b) - b*f(a)) / (f(b) - f(a))
        erro_abs = abs(b - a)
        erro_rel = erro_abs / abs(xm) if xm != 0 else float('inf')
        
        tabela.append({
            'iter': i+1,
            'x': xm,
            'f(x)': f(xm),
            'erro_abs': erro_abs,
            'erro_rel': erro_rel
        })
        
        if abs(f(xm)) < tol or erro_abs < tol:
            break
        
        if f(a) * f(xm) < 0:
            b = xm
        else:
            a = xm
    
    return tabela, xm

def ponto_fixo_completo(g, x0, tol, max_iter):
    tabela = []
    x = x0
    
    for i in range(max_iter):
        x_new = g(x)
        erro_abs = abs(x_new - x)
        erro_rel = erro_abs / abs(x_new) if x_new != 0 else float('inf')
        
        tabela.append({
            'iter': i+1,
            'x': x_new,
            'f(x)': x_new - g(x_new),
            'erro_abs': erro_abs,
            'erro_rel': erro_rel
        })
        
        if erro_abs < tol:
            break
        x = x_new
    
    return tabela, x

# ============ PLOTAGEM ============
def plotar_grafico(f, raiz, intervalo, metodo, nome_funcao):
    x = np.linspace(intervalo[0] - 1, intervalo[1] + 1, 1000)
    y = [f(i) for i in x]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label=f'f(x) = {nome_funcao}')
    plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    plt.axvline(x=raiz, color='r', linestyle='--', linewidth=1.5, label=f'Raiz ≈ {raiz:.6f}')
    plt.plot(raiz, f(raiz), 'ro', markersize=10)
    plt.grid(True, alpha=0.3)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Método: {metodo} | Raiz: {raiz:.8f}')
    plt.legend()
    plt.show()

# ============ MENU PRINCIPAL ============
def main():
    print("\n" + "="*70)
    print("  SOLUCIONADOR NUMÉRICO DE EQUAÇÕES")
    print("="*70)
    
    # Seleção da função
    print("\nEscolha a função:")
    for key, func in funcoes.items():
        print(f"  {key}. {func['nome']}")
    print("  7. Digitar minha própria função")
    
    escolha = input("\nOpção: ")
    
    if escolha == '7':
        expr = input("Digite f(x) em Python (ex: x**3 - 5*x - 9): ")
        f = eval(f"lambda x: {expr}")
        nome_funcao = expr
        a = float(input("Limite inferior (a): "))
        b = float(input("Limite superior (b): "))
        intervalo = (a, b)
    else:
        f = funcoes[escolha]['f']
        nome_funcao = funcoes[escolha]['nome']
        a, b = funcoes[escolha]['intervalo']
        intervalo = (a, b)
    
    # Seleção do método
    print("\nEscolha o método:")
    print("  1. Bisseção")
    print("  2. Posição Falsa")
    print("  3. Ponto Fixo")
    metodo = input("Opção: ")
    
    # Parâmetros
    tol = float(input("\nTolerância (ex: 1e-6): "))
    max_iter = int(input("Número máximo de iterações: "))
    
    # Execução
    if metodo == '1':
        tabela, raiz = bissecao_completo(f, a, b, tol, max_iter)
        nome_metodo = "Bisseção"
    elif metodo == '2':
        tabela, raiz = posicao_falsa_completo(f, a, b, tol, max_iter)
        nome_metodo = "Posição Falsa"
    else:
        x0 = float(input("Chute inicial: "))
        # Definir g(x) = x - f(x) para Ponto Fixo
        g = eval(f"lambda x: {x0} - {nome_funcao.replace('x', 'x')}")
        # Melhor usar g(x) = (1-x)^(1/3) para a função x³+x-1=0
        if escolha == '6':
            g = lambda x: (1 - x)**(1/3)
        else:
            g = lambda x: x - f(x)
        tabela, raiz = ponto_fixo_completo(g, x0, tol, max_iter)
        nome_metodo = "Ponto Fixo"
    
    # Exibir tabela
    if tabela:
        print("\n" + "="*80)
        print(f"Método: {nome_metodo} | Função: {nome_funcao}")
        print("="*80)
        print(f"{'Iteração':<10} {'x':<20} {'f(x)':<20} {'Erro Abs':<15} {'Erro Rel':<15}")
        print("-"*80)
        
        for row in tabela:
            print(f"{row['iter']:<10} {row['x']:<20.8f} {row['f(x)']:<20.8f} {row['erro_abs']:<15.8f} {row['erro_rel']:<15.8f}")
        
        print(f"\nRaiz aproximada: {raiz:.8f}")
        print(f"Iterações realizadas: {len(tabela)}")
        
        # Plotar gráfico
        plotar = input("\nDeseja plotar o gráfico? (s/n): ")
        if plotar.lower() == 's':
            plotar_grafico(f, raiz, intervalo, nome_metodo, nome_funcao)
    
if __name__ == "__main__":
    main()