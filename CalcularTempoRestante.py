from datetime import datetime, timedelta

def calcular_tempo_restante(horario_futuro):
    """
    Calcula o tempo restante até um horário futuro.
    Retorna (minutos, segundos) ou (0, 0) se já passou.
    """
    if horario_futuro is None:
        return None

    agora = datetime.now()
    diferenca = horario_futuro - agora

    if diferenca.total_seconds() <= 0:
        return (0, 0)

    total_segundos = int(diferenca.total_seconds())
    minutos = total_segundos // 60
    segundos = total_segundos % 60

    return (minutos, segundos)