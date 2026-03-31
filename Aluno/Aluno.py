from Dados import sistema
from AtualizarSistema import atualizar_status_automaticamente
from CalcularTempoRestante import calcular_tempo_restante
from ExibirHistorico import exibir_historico

def consultar_status():
    """
    Permite ao aluno consultar o status atual do fretado.
    """
    atualizar_status_automaticamente()

    print("\n" + "=" * 60)
    print("STATUS ATUAL DO FRETADO")
    print("=" * 60)
    print(f"Status: {sistema['status']}")

    if sistema["onibus_no_ponto"]:
        print("Ônibus disponível no ponto de encontro.")

        if sistema["hora_saida"] is not None:
            restante = calcular_tempo_restante(sistema["hora_saida"])

            if restante == (0, 0):
                print("Tempo para saída: 0 min 0 s")
                print("O ônibus já pode iniciar a viagem.")
            else:
                print(f"Tempo para saída: {restante[0]} min {restante[1]} s")
                print(f"Horário previsto de saída: {sistema['hora_saida'].strftime('%H:%M:%S')}")
        else:
            print("Temporizador de embarque ainda não foi iniciado.")
    else:
        print("Não há ônibus no ponto neste momento.")

        if sistema["hora_proximo_onibus"] is not None:
            restante = calcular_tempo_restante(sistema["hora_proximo_onibus"])

            if restante == (0, 0):
                print("Próximo ônibus previsto para chegar agora.")
            else:
                print(f"Próximo ônibus previsto em: {restante[0]} min {restante[1]} s")
                print(f"Horário previsto de chegada: {sistema['hora_proximo_onibus'].strftime('%H:%M:%S')}")
        else:
            print("Sem previsão cadastrada para o próximo ônibus.")


def menu_aluno():
    """
    Menu do aluno.
    """
    while True:
        print("\n" + "=" * 60)
        print("MENU DO ALUNO")
        print("=" * 60)
        print("1 - Consultar status do ônibus")
        print("2 - Ver histórico de eventos")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            consultar_status()
        elif opcao == "2":
            exibir_historico()
        elif opcao == "0":
            break
        else:
            print("[ERRO] Opção inválida.")