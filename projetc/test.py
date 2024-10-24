# Lista para armazenar agendamentos
agendamentos = []

# Função para agendar uma visita ou batismo
def agendar(tipo, data, hora, nome, telefone, endereco):
    # Verificar se já existe um agendamento no mesmo horário
    for a in agendamentos:
        if a['data'] == data and a['hora'] == hora:
            print("Horário já ocupado. Por favor, escolha outro horário.")
            return
    agendamento = {
        'tipo': tipo,
        'data': data,
        'hora': hora,
        'nome': nome,
        'telefone': telefone,
        'endereco': endereco
    }
    agendamentos.append(agendamento)
    print(f"{tipo.capitalize()} agendado para {data} às {hora} por {nome}.")

# Função para cancelar um agendamento
def cancelar_agendamento(data, hora):
    global agendamentos
    # Verificar se existe um agendamento para cancelar
    agendamentos_anteriores = [a for a in agendamentos if a['data'] == data and a['hora'] == hora]
    
    if not agendamentos_anteriores:
        print("Não existem agendamentos para serem cancelados.")
        return

    # Remover agendamentos encontrados
    agendamentos = [a for a in agendamentos if not (a['data'] == data and a['hora'] == hora)]
    print(f"Agendamento para {data} às {hora} foi cancelado.")

# Função para ver as datas disponíveis do mês
def ver_dados_disponiveis(mes, ano):
    print(f"Datas disponíveis para {mes}/{ano}:")
    dias_disponiveis = {}
    for dia in range(1, 32):  # Considerando até 31 dias
        data_str = f"{dia:02d}/{mes:02d}/{ano}"  # Formato DD/MM/YYYY
        # Simulação de verificação se o dia é válido e se há agendamentos
        dias_disponiveis[data_str] = []
        for agendamento in agendamentos:
            if agendamento['data'] == data_str:
                dias_disponiveis[data_str].append(agendamento)

    # Impressão das datas e seus agendamentos
    for data, agendamentos_do_dia in dias_disponiveis.items():
        if agendamentos_do_dia:
            print(f"{data}: {agendamentos_do_dia}")
        else:
            print(f"{data}: Disponível")

# Função para gerar um relatório semanal
def gerar_relatorio_semanal():
    print("Relatório Semanal:")
    for agendamento in agendamentos:
        print(f"{agendamento['tipo'].capitalize()} - Data: {agendamento['data']}, Hora: {agendamento['hora']}, Nome: {agendamento['nome']}")

# Função para gerar um relatório mensal
def gerar_relatorio_mensal(mes, ano):
    print(f"Relatório Mensal para {mes}/{ano}:")
    for agendamento in agendamentos:
        dia, mes_agendamento, ano_agendamento = agendamento['data'].split('/')
        if int(mes_agendamento) == mes and int(ano_agendamento) == ano:
            print(f"{agendamento['tipo'].capitalize()} - Data: {agendamento['data']}, Hora: {agendamento['hora']}, Nome: {agendamento['nome']}")

# Função para o menu interativo
def menu():
    while True:
        print("\nMenu Principal:")
        print("1. Agenda Mensal – Visitas e Batismos")
        print("2. Relatório Semanal")
        print("3. Relatório Geral")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            while True:
                print("\n1. Agendar")
                print("2. Cancelar agendamento")
                print("3. Voltar")
                opcao1 = input("Escolha uma opção: ")

                if opcao1 == '1':
                    while True:
                        mes = input("Selecione o mês (1-12) ou digite 'voltar' para voltar: ")
                        if mes.lower() == 'voltar':
                            break
                        if mes.isdigit() and 1 <= int(mes) <= 12:
                            mes = int(mes)
                            ano = int(input("Selecione o ano: "))
                            ver_dados_disponiveis(mes, ano)

                            while True:
                                print("\n1. Ver datas disponíveis")
                                print("2. Selecionar data para agendamento")
                                print("3. Voltar")
                                subopcao = input("Escolha uma opção: ")

                                if subopcao == '1':
                                    ver_dados_disponiveis(mes, ano)

                                elif subopcao == '2':
                                    data = input("Selecione a data para agendamento (DD/MM/YYYY): ")
                                    hora = input("Selecione a hora para agendamento (HH:MM): ")
                                    tipo = input("Escolha o tipo de agendamento (Visita ou Batismo): ").lower()
                                    if tipo not in ['visita', 'batismo']:
                                        print("Tipo de agendamento inválido. Por favor, escolha 'Visita' ou 'Batismo'.")
                                        continue
                                    nome = input("Nome do visitante: ")
                                    telefone = input("Telefone do visitante: ")
                                    endereco = input("Endereço do visitante: ")
                                    agendar(tipo, data, hora, nome, telefone, endereco)

                                elif subopcao == '3':
                                    break
                        else:
                            print("Mês inválido. Tente novamente.")

                elif opcao1 == '2':
                    data = input("Digite a data do agendamento (DD/MM/YYYY): ")
                    hora = input("Digite a hora do agendamento (HH:MM): ")
                    cancelar_agendamento(data, hora)

                elif opcao1 == '3':
                    break

        elif opcao == '2':
            gerar_relatorio_semanal()
            input("Pressione Enter para continuar...")

        elif opcao == '3':
            mes = int(input("Selecione o mês para o relatório geral (1-12): "))
            ano = int(input("Selecione o ano: "))
            gerar_relatorio_mensal(mes, ano)
            input("Pressione Enter para continuar...")

        elif opcao == '4':
            print("Saindo do programa. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa
menu()
