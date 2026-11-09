
print("=== SISTEMA DE CHAMADOS DE TI ===")

ids = []
usuarios = []
problemas = []
prioridades = []
status = []

proximo_id = 1

while True:
    print("\n========== HELP DESK ==========")
    print("1 - Abrir chamado")
    print("2 - Listar chamados")
    print("3 - Consultar chamado")
    print("4 - Atualizar status")
    print("5 - Excluir chamado")
    print("6 - Relatório de chamados")
    print("7 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        print("\n--- ABRIR CHAMADO ---")

        usuario = input("Nome do solicitante: ")
        problema = input("Descreva o problema: ")

        print("\nPrioridade:")
        print("1 - Baixa")
        print("2 - Média")
        print("3 - Alta")

        escolha = input("Escolha a prioridade: ")

        if escolha == "1":
            prioridade = "Baixa"
        elif escolha == "2":
            prioridade = "Média"
        elif escolha == "3":
            prioridade = "Alta"
        else:
            prioridade = "Não definida"

        if usuario != "" and problema != "":
            ids.append(proximo_id)
            usuarios.append(usuario)
            problemas.append(problema)
            prioridades.append(prioridade)
            status.append("Aberto")

            print("\nChamado aberto com sucesso!")
            print("Número do chamado:", proximo_id)

            proximo_id = proximo_id + 1
        else:
            print("Erro: preencha todos os campos!")

    elif opcao == "2":
        print("\n--- LISTA DE CHAMADOS ---")

        if len(ids) == 0:
            print("Nenhum chamado registrado.")
        else:
            for i in range(len(ids)):
                print("--------------------------")
                print("ID:", ids[i])
                print("Usuário:", usuarios[i])
                print("Problema:", problemas[i])
                print("Prioridade:", prioridades[i])
                print("Status:", status[i])

    elif opcao == "3":
        print("\n--- CONSULTAR CHAMADO ---")

        numero = int(input("Digite o ID: "))
        encontrado = False

        for i in range(len(ids)):
            if ids[i] == numero:
                print("\nID:", ids[i])
                print("Usuário:", usuarios[i])
                print("Problema:", problemas[i])
                print("Prioridade:", prioridades[i])
                print("Status:", status[i])
                encontrado = True
                break

        if encontrado == False:
            print("Chamado não encontrado!")

    elif opcao == "4":
        print("\n--- ATUALIZAR STATUS ---")

        numero = int(input("ID do chamado: "))
        encontrado = False

        for i in range(len(ids)):
            if ids[i] == numero:
                encontrado = True

                print("\n1 - Aberto")
                print("2 - Em andamento")
                print("3 - Resolvido")

                escolha = input("Novo status: ")

                if escolha == "1":
                    status[i] = "Aberto"
                elif escolha == "2":
                    status[i] = "Em andamento"
                elif escolha == "3":
                    status[i] = "Resolvido"
                else:
                    print("Status inválido!")
                    break

                print("Status atualizado!")
                break

        if encontrado == False:
            print("Chamado não encontrado!")

    elif opcao == "5":
        print("\n--- EXCLUIR CHAMADO ---")

        numero = int(input("ID do chamado: "))
        encontrado = False

        for i in range(len(ids)):
            if ids[i] == numero:
                ids.pop(i)
                usuarios.pop(i)
                problemas.pop(i)
                prioridades.pop(i)
                status.pop(i)

                print("Chamado excluído!")
                encontrado = True
                break

        if encontrado == False:
            print("Chamado não encontrado!")

    elif opcao == "6":
        print("\n--- RELATÓRIO DE TI ---")

        abertos = 0
        andamento = 0
        resolvidos = 0
        alta_prioridade = 0

        for i in range(len(ids)):
            if status[i] == "Aberto":
                abertos = abertos + 1
            elif status[i] == "Em andamento":
                andamento = andamento + 1
            elif status[i] == "Resolvido":
                resolvidos = resolvidos + 1

            if prioridades[i] == "Alta":
                alta_prioridade = alta_prioridade + 1

        print("Total de chamados:", len(ids))
        print("Chamados abertos:", abertos)
        print("Em andamento:", andamento)
        print("Resolvidos:", resolvidos)
        print("Alta prioridade:", alta_prioridade)

    elif opcao == "7":
        print("\nEncerrando Help Desk...")
        break

    else:
        print("Opção inválida!")
