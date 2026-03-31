from datetime import datetime, timedelta
from Dados import sistema

def atualizar_status_automaticamente():
    """
    Atualiza o status automaticamente com base no tempo real.
    """
    agora = datetime.now()

    # Se existe previsão do próximo ônibus e ele ainda não chegou
    if not sistema["onibus_no_ponto"] and sistema["hora_proximo_onibus"] is not None:
        if agora >= sistema["hora_proximo_onibus"]:
            sistema["status"] = "Próximo ônibus previsto para chegar agora"

    # Se existe ônibus no ponto e o tempo de saída chegou
    if sistema["onibus_no_ponto"] and sistema["hora_saida"] is not None:
        if agora >= sistema["hora_saida"]:
            sistema["status"] = "Ônibus pronto para sair"