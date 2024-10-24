def menu_principal():
    while True:
        print("1. Agenda Mensal – Visitas e Batismos")
        print("2. Relatório Semanal")
        print("3. Relatório Geral")
        print("4. Ajuda")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            agenda_mensal()
        elif opcao == "2":
            relatorio_semanal()
        elif opcao == "3":
            relatorio_geral()
        elif opcao == "4":
            ajuda()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def agenda_mensal():
    while True:
        print("1. Agendar")
        print("2. Cancelar agendamento")
        print("3. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            agendar()
        elif opcao == "2":
            cancelar_agendamento()
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

def agendar():
    # Lógica para agendar visita ou batismo
    print("Selecionar mês:")
    # Implementar seleção de mês e ver datas disponíveis
    # Mostrar calendário com dias agendados e disponíveis
    # Implementar agendamento

def cancelar_agendamento():
    # Lógica para cancelar um agendamento
    print("Cancelar agendamento:")
    # Implementar cancelamento

def relatorio_semanal():
    # Lógica para gerar relatório semanal
    print("Gerar relatório semanal:")
    # Implementar geração de relatório

def relatorio_geral():
    # Lógica para gerar relatório geral
    print("Gerar relatório geral:")
    # Implementar geração de relatório

def ajuda():
    # Lógica para mostrar ajuda e instruções
    print("Instruções de uso do programa.")

# Execução do programa
menu_principal()
