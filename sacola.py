# Inicializa a lista de itens da sacola
itens_sacola = []

# Pergunta quantos itens já estão na sacola
quantidade_itens = int(input("Quantos itens você tem na sacola de compras? "))

# Adiciona os itens iniciais à sacola
for i in range(quantidade_itens):
    item = input(f"Digite o nome do item {i + 1}: ")
    itens_sacola.append(item)

# Pergunta se deseja adicionar mais itens
while True:
    adicionar = input("Você gostaria de adicionar mais itens à sacola? (sim/não): ").strip().lower()
    
    if adicionar == 'sim':
        novo_item = input("Qual item você deseja adicionar? ")
        itens_sacola.append(novo_item)
    elif adicionar == 'não':
        break
    else:
        print("Resposta inválida. Por favor, digite 'sim' ou 'não'.")

# Imprime todos os itens da sacola
print("\nItens na sacola de compras:")
for item in itens_sacola:
    print("-", item)
