def validar_inteiro_positivo(mensagem):
    """
    Solicita um número inteiro positivo ao usuário.
    """
    try:
        valor = int(input(mensagem))
        if valor <= 0:
            print("[ERRO] O valor deve ser maior que zero.")
            return None
        return valor
    except ValueError:
        print("[ERRO] Digite um número inteiro válido.")
        return None