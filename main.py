from cores import colorir
from textos import titulo
from operacoes import *
import os

TITULO = colorir(titulo("SISTEMA BANCÁRIO"), "vermelho")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def opcao1():
    print(TITULO)
    print(colorir("Executando opção Saldo...", "verde"))
    print("Seu saldo é de: ", converter_reais(calcular_saldo()))
    input("Pressione Enter para voltar ao menu.")

def opcao2():
    print(TITULO)
    print(colorir("Executando opção Extrato...", "verde"))
    print(consultar_extrato())
    print("Seu saldo é de: ", converter_reais(calcular_saldo()))
    input("Pressione Enter para voltar ao menu.")

def opcao3():
    print(TITULO)
    print(colorir("Executando opção Depositar...", "verde"))
    valor = input("Digite o valor a ser depositado: R$ ")
    try:
        valor = float(valor.replace(",", "."))
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        print(depositar(valor))
    except ValueError as e:
        print(colorir(f"Erro: {e}", "vermelho"))
    except Exception as e:
        print(colorir(f"Erro inesperado: {e}", "vermelho"))
    finally:
        input("Pressione Enter para voltar ao menu.")

def opcao4():
    print(TITULO)
    print(colorir("Executando opção Sacar...", "verde"))
    valor = input("Digite o valor a ser sacado: R$ ")
    try:
        valor = float(valor.replace(",", "."))
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        print(sacar(valor))
    except ValueError as e:
        print(colorir(f"Erro: {e}", "vermelho"))
    except Exception as e:
        print(colorir(f"Erro inesperado: {e}", "vermelho"))
    finally:
        input("Pressione Enter para voltar ao menu.")

def sair():
    print(TITULO)
    print("Saindo do programa...")
    exit()

menu_opcoes = {
    "1": (colorir("Saldo","verde"), opcao1),
    "2": (colorir("Extrato","verde"), opcao2),
    "3": (colorir("Depositar","verde"), opcao3),
    "4": (colorir("Sacar","verde"), opcao4),

    "0": (colorir("Sair","vermelho"), sair)
}

def menu():
    while True:
        limpar_tela()  # <- Mantém o menu sempre "no mesmo lugar"
        print(TITULO)
        print("=== Menu Principal ===")

        for chave, (descricao, _) in menu_opcoes.items():
            print(f"{chave} - {descricao}")
        
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha in menu_opcoes:
            _, funcao = menu_opcoes[escolha]
            limpar_tela()
            funcao()
        else:
            limpar_tela()
            print(TITULO)
            print(colorir("Opção inválida.","amarelo"))
            input("Pressione Enter para tentar novamente.")

menu()
