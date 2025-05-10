from enum import Enum

class TipoTransacao(Enum):
    SAQUE = "saque"
    DEPOSITO = "deposito"

extrato = []
proximo_id = 0

def registrar_transacao(tipo: str, valor: float):
    global proximo_id
    extrato.append({
        "id": proximo_id,
        "tipo": tipo,
        "valor": valor
    })
    proximo_id += 1

def calcular_saldo():
    saldo = 0.0
    for t in extrato:
        if t["tipo"] == "deposito":
            saldo += t["valor"]
        elif t["tipo"] == "saque":
            saldo -= t["valor"]
    return saldo  # ✅ Retorna o saldo como float, não formatado

def converter_reais(valor: float) -> str:
    """
    Converte um valor em reais para uma string formatada com o símbolo de real.
    """
    return f"R$ {valor:.2f}".replace('.', ',')

def consultar_extrato():
    """
    Retorna o extrato formatado como uma string.
    """
    extrato_formatado = ""
    for t in extrato:
        extrato_formatado += f"{t['tipo'].capitalize()} - {converter_reais(t['valor'])}\n"
    return extrato_formatado if extrato else "Nenhuma transação registrada."

# depositar valores não pode aceitar valores menores ou iguais a 0 contém tratamento de erros para string e float
def depositar(valor: float):
    if valor <= 0:
        raise ValueError("O valor do depósito deve ser maior que zero.")
    registrar_transacao(TipoTransacao.DEPOSITO.value, valor)
    return f"Depósito de {converter_reais(valor)} realizado com sucesso!"

# sacar valores não pode aceitar valores menores ou iguais a 0 contém tratamento de erros para string e float
# limite 3 saques por dia e limite de 500 reais por saque
def sacar(valor: float):
    if valor <= 0:
        raise ValueError("O valor do saque deve ser maior que zero.")
    if valor > 500:
        raise ValueError("O valor do saque não pode ser maior que R$ 500,00.")
    if len([t for t in extrato if t["tipo"] == TipoTransacao.SAQUE.value]) >= 3:
        raise ValueError("Limite de 3 saques por dia atingido.")
    if valor > calcular_saldo():
        raise ValueError("Saldo insuficiente para realizar o saque.")
    registrar_transacao(TipoTransacao.SAQUE.value, valor)
    return f"Saque de {converter_reais(valor)} realizado com sucesso!"


