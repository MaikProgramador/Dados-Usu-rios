import json
import os

# Função para coletar dados do usuário
def coletar_dados():
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    telefone = input("Digite seu número de telefone: ")
    cep = input("Digite seu CEP: ")
    
    return {
        "email": email,
        "senha": senha,
        "telefone": telefone,
        "cep": cep
    }

# Função para salvar dados em um arquivo JSON
def salvar_dados(dados, arquivo="dados.json"):
    # Verifica se o arquivo existe
    if os.path.exists(arquivo):
        # Carrega dados existentes
        with open(arquivo, "r") as file:
            try:
                dados_existentes = json.load(file)
            except json.JSONDecodeError:
                dados_existentes = []
    else:
        dados_existentes = []

    # Adiciona os novos dados
    dados_existentes.append(dados)

    # Salva os dados atualizados
    with open(arquivo, "w") as file:
        json.dump(dados_existentes, file, indent=4)

# Main
if __name__ == "__main__":
    dados_usuario = coletar_dados()
    salvar_dados(dados_usuario)
    print("Dados salvos com sucesso!")
