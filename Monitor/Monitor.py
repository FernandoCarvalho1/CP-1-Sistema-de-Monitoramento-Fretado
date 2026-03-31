from datetime import datetime, timedelta
from Dados import sistema
from Dados import monitor
from RegistrarEvento import registrar_evento
from ValidarInteiroPositivo import validar_inteiro_positivo
from ExibirHistorico import exibir_historico
from Aluno.Aluno import consultar_status


def login_monitor():
    """
    Realiza login simples do monitor.
    """
    print("\n" + "=" * 60)
    print("LOGIN DO MONITOR")
    print("=" * 60)

    matricula = input("Digite a matrícula: ").strip()
    senha = input("Digite a senha: ").strip()

    if matricula == monitor["matricula"] and senha == monitor["senha"]:
        print("[OK] Login realizado com sucesso.")
        registrar_evento("Monitor realizou login no sistema")
        return True
    else:
        print("[ERRO] Matrícula ou senha inválidas.")
        return False


def registrar_chegada():
    """
    Permite ao monitor registrar a chegada do ônibus.
    """
    if sistema["onibus_no_ponto"]:
        print("[ERRO] Já existe um ônibus no ponto.")
        return

    sistema["onibus_no_ponto"] = True
    sistema["hora_saida"] = None
    sistema["hora_proximo_onibus"] = None
    sistema["status"] = "Ônibus no ponto - aguardando início do embarque"

    registrar_evento("Chegada do ônibus registrada pelo monitor")
    print("[OK] Chegada do ônibus registrada com sucesso.")


def iniciar_temporizador():
    """
    Permite ao monitor iniciar o temporizador de embarque.
    """
    if not sistema["onibus_no_ponto"]:
        print("[ERRO] Não há ônibus no ponto para iniciar o temporizador.")
        return

    tempo = validar_inteiro_positivo("Digite o tempo de espera para saída (em minutos): ")
    if tempo is None:
        return

    sistema["hora_saida"] = datetime.now() + timedelta(minutes=tempo)
    sistema["status"] = "Ônibus no ponto - embarque em andamento"

    registrar_evento(f"Temporizador de embarque iniciado: {tempo} minuto(s)")
    print("[OK] Temporizador iniciado com sucesso.")
    print(f"Horário previsto de saída: {sistema['hora_saida'].strftime('%H:%M:%S')}")


def registrar_saida():
    """
    Permite ao monitor registrar a saída normal do ônibus.
    """
    if not sistema["onibus_no_ponto"]:
        print("[ERRO] Não há ônibus no ponto para registrar saída.")
        return

    sistema["onibus_no_ponto"] = False
    sistema["hora_saida"] = None
    sistema["status"] = "Ônibus em viagem"

    registrar_evento("Saída normal do ônibus registrada")
    print("[OK] Saída do ônibus registrada com sucesso.")

    resposta = input("Deseja informar a previsão do próximo ônibus agora? (s/n): ").strip().lower()
    if resposta == "s":
        informar_proximo_onibus()


def registrar_saida_lotacao():
    """
    Permite ao monitor registrar saída antecipada por lotação.
    """
    if not sistema["onibus_no_ponto"]:
        print("[ERRO] Não há ônibus no ponto para registrar saída antecipada.")
        return

    sistema["onibus_no_ponto"] = False
    sistema["hora_saida"] = None
    sistema["status"] = "Ônibus saiu antecipadamente por lotação"

    registrar_evento("Saída antecipada do ônibus por lotação")
    print("[OK] Saída antecipada por lotação registrada com sucesso.")

    resposta = input("Deseja informar a previsão do próximo ônibus agora? (s/n): ").strip().lower()
    if resposta == "s":
        informar_proximo_onibus()


def informar_proximo_onibus():
    """
    Permite ao monitor informar a previsão do próximo ônibus.
    """
    tempo = validar_inteiro_positivo("Digite em quantos minutos o próximo ônibus chegará: ")
    if tempo is None:
        return

    sistema["hora_proximo_onibus"] = datetime.now() + timedelta(minutes=tempo)

    if not sistema["onibus_no_ponto"]:
        sistema["status"] = "Aguardando próximo ônibus"

    registrar_evento(f"Previsão do próximo ônibus cadastrada: {tempo} minuto(s)")
    print("[OK] Previsão do próximo ônibus registrada com sucesso.")
    print(f"Horário previsto de chegada: {sistema['hora_proximo_onibus'].strftime('%H:%M:%S')}")


def menu_monitor():
    """
    Menu do monitor (somente após login).
    """
    if not login_monitor():
        return

    while True:
        print("\n" + "=" * 60)
        print("MENU DO MONITOR")
        print("=" * 60)
        print("1 - Registrar chegada do ônibus")
        print("2 - Iniciar temporizador de embarque")
        print("3 - Registrar saída do ônibus")
        print("4 - Registrar saída antecipada por lotação")
        print("5 - Informar previsão do próximo ônibus")
        print("6 - Consultar status atual")
        print("7 - Ver histórico de eventos")
        print("0 - Logout / Voltar ao menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            registrar_chegada()
        elif opcao == "2":
            iniciar_temporizador()
        elif opcao == "3":
            registrar_saida()
        elif opcao == "4":
            registrar_saida_lotacao()
        elif opcao == "5":
            informar_proximo_onibus()
        elif opcao == "6":
            consultar_status()
        elif opcao == "7":
            exibir_historico()
        elif opcao == "0":
            registrar_evento("Monitor encerrou sessão no sistema")
            print("[OK] Logout realizado com sucesso.")
            break
        else:
            print("[ERRO] Opção inválida.")