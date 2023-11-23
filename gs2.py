import json

def validar_entrada(pergunta, opcoes_validas):
    while True:
        entrada = input(pergunta).strip().lower()
        if entrada in opcoes_validas:
            return entrada
        else:
            print("Opção inválida. Tente novamente.")

def coletar_respostas():
    print("Realizando triagem de saúde mental...")
    nome_completo = input("Por favor, digite seu nome completo: ")
    
    perguntas = {
    "tristeza": "Você tem sentido tristeza constante? (s/n): ",
    "sono": "Você tem dificuldade em dormir? (s/n): ",
    "ansiedade": "Você tem sentido ansiedade excessiva? (s/n): ",
    "apetite": "Sua alimentação tem sido afetada? (s/n): ",
    }
    respostas = {"Nome Completo": nome_completo}

    for chave, pergunta in perguntas.items():
        resposta = validar_entrada(pergunta, ['s', 'n'])
        respostas[chave] = resposta

    return respostas

def salvar_respostas(respostas):
    try:
        with open('registros.json', 'r') as file:
            registros = json.load(file)
    except FileNotFoundError:
        registros = []

    registros.append(respostas)

    with open('registros.json', 'w') as file:
        json.dump(registros, file)

    print("Triagem concluída. Respostas salvas com sucesso.")

def visualizar_registros():
    try:
        with open('registros.json', 'r') as file:
            registros = json.load(file)
            print("=== Registros de Triagem ===")
            for i, registro in enumerate(registros, 1):
                print(f"Registro {i}: {registro}")
    except FileNotFoundError:
        print("Nenhum registro encontrado.")

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Realizar Triagem")
        print("2. Visualizar Registros")
        print("3. Sair")

        opcao = validar_entrada("Escolha uma opção: ", ['1', '2', '3'])

        if opcao == '1':
            respostas = coletar_respostas()
            salvar_respostas(respostas)
        elif opcao == '2':
            visualizar_registros()
        elif opcao == '3':
            print("Saindo do programa...")
            break

if __name__ == "__main__":
    menu()