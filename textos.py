def titulo(texto: str) -> str:
    """
    Formata o texto como um título, adicionando uma linha de separação acima e abaixo.
    """
    tamanho = len(texto) + 4
    linha = "=" * tamanho
    return f"{linha}\n{texto}\n{linha}"
