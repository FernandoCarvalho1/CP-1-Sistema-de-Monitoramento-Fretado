# Dados de acesso do monitor 
monitor = {
    "matricula": "12345",
    "senha": "fiap123"
}

# Estado atual do sistema
sistema = {
    "onibus_no_ponto": False,
    "status": "Sem ônibus no ponto",
    "hora_saida": None,             # Horário real previsto para saída
    "hora_proximo_onibus": None,    # Horário real previsto para chegada do próximo ônibus
    "historico": []                 # Lista de eventos do sistema
}