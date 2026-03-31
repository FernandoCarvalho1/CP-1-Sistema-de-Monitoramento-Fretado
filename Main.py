# ============================================================
# SISTEMA DE MONITORAMENTO DE FRETADO UNIVERSITÁRIO
# Simulação via Terminal
# ============================================================
# Funcionalidades principais:
# - Menu Aluno
# - Menu Monitor com login
# - Consulta de status em tempo real
# - Registro de chegada do ônibus
# - Temporizador real para saída
# - Registro de saída normal
# - Registro de saída antecipada por lotação
# - Previsão real do próximo ônibus
# - Histórico de eventos
# ============================================================

from Aluno.Aluno import menu_aluno
from Monitor.monitor import menu_monitor
from RegistrarEvento import registrar_evento

def menu_principal():
    """
    Menu principal do sistema.
    """
    while True:
        print("\n" + "=" * 60)
        print("SISTEMA DE MONITORAMENTO DE FRETADO UNIVERSITÁRIO")
        print("=" * 60)
        print("1 - Acessar como Aluno")
        print("2 - Acessar como Monitor")
        print("0 - Encerrar sistema")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu_aluno()
        elif opcao == "2":
            menu_monitor()
        elif opcao == "0":
            print("\nSistema encerrado. Até logo!")
            break
        else:
            print("[ERRO] Opção inválida. Escolha uma opção válida.")


# ============================================================
# EXECUÇÃO DO SISTEMA
# ============================================================

if __name__ == "__main__":
    registrar_evento("Sistema iniciado")
    menu_principal()