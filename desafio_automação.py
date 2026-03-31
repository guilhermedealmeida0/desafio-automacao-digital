# ==========================================
# SISTEMA DE AUTOMAÇÃO DE QUALIDADE
# Trabalho de Algoritmos e Lógica de Programação
# ==========================================

# Listas principais do sistema
pecas = []
caixas = []


def converter_entrada(entrada, tipo):
    """
    Converte valores digitados com unidade para uma unidade padrão:
    - peso -> gramas (g)
    - comprimento -> centímetros (cm)

    Exemplos aceitos:
    Peso: 15g | 0,015kg | 15000mg
    Comprimento: 10cm | 100mm | 0,10m | 1,80m
    """

    entrada = entrada.strip().lower().replace(" ", "")
    entrada = entrada.replace(",", ".")

    numero = ""
    unidade = ""

    for caractere in entrada:
        if caractere.isdigit() or caractere == ".":
            numero += caractere
        else:
            unidade += caractere

    if numero == "":
        raise ValueError("Nenhum valor numérico foi informado.")

    valor = float(numero)

    if tipo == "peso":
        if unidade == "mg":
            return valor / 1000  # mg -> g
        elif unidade == "g" or unidade == "":
            return valor         # g -> g
        elif unidade == "kg":
            return valor * 1000  # kg -> g
        else:
            raise ValueError("Unidade de peso inválida. Use mg, g ou kg.")

    elif tipo == "comprimento":
        if unidade == "mm":
            return valor / 10    # mm -> cm
        elif unidade == "cm" or unidade == "":
            return valor         # cm -> cm
        elif unidade == "m":
            return valor * 100   # m -> cm
        else:
            raise ValueError("Unidade de comprimento inválida. Use mm, cm ou m.")

    else:
        raise ValueError("Tipo de conversão inválido.")


def cadastrar_peca():
    """Cadastra uma peça e verifica se ela foi aprovada ou reprovada."""
    print("\n--- CADASTRO DE PEÇA ---")

    try:
        peso = converter_entrada(input("Digite o peso (mg, g ou kg): "), "peso")
        cor = input("Digite a cor: ").strip().lower()
        comprimento = converter_entrada(input("Digite o comprimento (mm, cm ou m): "), "comprimento")

        # Critérios de aprovação
        if 10 <= peso <= 20 and cor == "azul" and 5 <= comprimento <= 15:
            status = "Aprovada"
        else:
            status = "Reprovada"

        peca = {
            "peso_g": peso,
            "cor": cor,
            "comprimento_cm": comprimento,
            "status": status
        }

        pecas.append(peca)

        print(f"\nPeça cadastrada com sucesso.")
        print(f"Status da peça: {status}")

    except ValueError as erro:
        print(f"\nErro: {erro}")


def listar_pecas():
    """Exibe todas as peças cadastradas."""
    print("\n--- LISTA DE PEÇAS ---")

    if not pecas:
        print("Nenhuma peça cadastrada.")
        return

    for i, peca in enumerate(pecas):
        print(
            f"{i} | Peso: {peca['peso_g']:.2f} g | "
            f"Cor: {peca['cor']} | "
            f"Comprimento: {peca['comprimento_cm']:.2f} cm | "
            f"Status: {peca['status']}"
        )


def remover_peca():
    """Remove uma peça pelo índice informado."""
    print("\n--- REMOVER PEÇA ---")

    if not pecas:
        print("Nenhuma peça cadastrada para remover.")
        return

    listar_pecas()

    try:
        indice = int(input("\nDigite o índice da peça que deseja remover: "))

        if 0 <= indice < len(pecas):
            pecas.pop(indice)
            print("Peça removida com sucesso.")
        else:
            print("Índice inválido.")

    except ValueError:
        print("Digite um número inteiro válido.")


def organizar_caixas():
    """
    Organiza peças aprovadas em caixas com capacidade para 5 peças.
    Limpa e reorganiza sempre que a função é executada.
    """
    print("\n--- ORGANIZAR CAIXAS ---")

    caixas.clear()
    aprovadas = [peca for peca in pecas if peca["status"] == "Aprovada"]

    while len(aprovadas) >= 5:
        caixa = aprovadas[:5]
        caixas.append(caixa)
        aprovadas = aprovadas[5:]

    print(f"Quantidade de caixas fechadas: {len(caixas)}")
    print(f"Peças aprovadas restantes fora das caixas: {len(aprovadas)}")


def listar_caixas():
    """Mostra as caixas fechadas e as peças dentro delas."""
    print("\n--- LISTA DE CAIXAS ---")

    if not caixas:
        print("Nenhuma caixa fechada.")
        return

    for i, caixa in enumerate(caixas, start=1):
        print(f"\nCaixa {i}:")
        for j, peca in enumerate(caixa, start=1):
            print(
                f"  Peça {j} | "
                f"Peso: {peca['peso_g']:.2f} g | "
                f"Cor: {peca['cor']} | "
                f"Comprimento: {peca['comprimento_cm']:.2f} cm"
            )


def relatorio():
    """Gera um relatório geral do sistema."""
    print("\n--- RELATÓRIO FINAL ---")

    total = len(pecas)
    aprovadas = len([peca for peca in pecas if peca["status"] == "Aprovada"])
    reprovadas = len([peca for peca in pecas if peca["status"] == "Reprovada"])

    print(f"Total de peças cadastradas: {total}")
    print(f"Total de peças aprovadas: {aprovadas}")
    print(f"Total de peças reprovadas: {reprovadas}")
    print(f"Total de caixas fechadas: {len(caixas)}")


def menu():
    """Exibe o menu principal do sistema."""
    while True:
        print("\n===================================")
        print(" SISTEMA DE AUTOMAÇÃO DE QUALIDADE ")
        print("===================================")
        print("1. Cadastrar peça")
        print("2. Listar peças")
        print("3. Remover peça")
        print("4. Organizar caixas")
        print("5. Listar caixas")
        print("6. Exibir relatório")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            organizar_caixas()
        elif opcao == "5":
            listar_caixas()
        elif opcao == "6":
            relatorio()
        elif opcao == "7":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Início do programa
menu()