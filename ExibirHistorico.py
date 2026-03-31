from Dados import sistema

def exibir_historico():
    """
    Exibe o histórico de eventos do sistema.
    """
    print("\n" + "=" * 60)
    print("HISTÓRICO DE EVENTOS")
    print("=" * 60)

    if not sistema["historico"]:
        print("Nenhum evento registrado até o momento.")
    else:
        for evento in sistema["historico"]:
            print(evento)