from datetime import datetime, timedelta
from Dados import sistema

def registrar_evento(descricao):
    """
    Registra um evento no histórico com data e hora.
    """
    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    sistema["historico"].append(f"[{horario}] {descricao}")