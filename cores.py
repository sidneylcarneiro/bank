def colorir(texto: str, cor: str) -> str:
    """
    Retorna a string formatada com a cor especificada usando códigos ANSI.

    Cores disponíveis:
    - vermelho
    - verde
    - amarelo
    - azul
    - magenta
    - ciano
    - branco
    - reset (sem cor)

    Exemplo:
        print(colorir("Olá, mundo!", "verde"))
    """
    cores = {
        "vermelho": "\033[91m",
        "verde": "\033[92m",
        "amarelo": "\033[93m",
        "azul": "\033[94m",
        "magenta": "\033[95m",
        "ciano": "\033[96m",
        "branco": "\033[97m",
        "reset": "\033[0m"
    }

    cor_code = cores.get(cor.lower(), cores["reset"])
    return f"{cor_code}{texto}{cores['reset']}"
