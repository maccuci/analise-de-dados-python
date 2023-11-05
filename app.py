import pandas as pd
import matplotlib.pyplot as plt


def carregar_dados(arquivo="imoveis.csv") -> pd.DataFrame:
    try:
        dados_imoveis = pd.read_csv(
            arquivo, sep=",", encoding="utf-8", low_memory=False, index_col=0)
        return dados_imoveis
    except FileNotFoundError:
        print("O arquivo imoveis.csv não foi encontrado. Por favor, execute o arquivo export.py para gerar o arquivo.")
        exit(1)


def escolher_coluna(colunas_nova) -> str:
    input_coluna = str(input("Digite o nome da coluna: ").lower())

    if input_coluna in colunas_nova:
        return colunas_nova[input_coluna]
    else:
        print(
            f"A coluna '{input_coluna}' não foi encontrada. Escolha entre {', '.join(colunas_nova.keys())}")
        return None


def mostrar_histograma(dados_imoveis, coluna) -> None:
    media_coluna = dados_imoveis[coluna].mean()
    max_coluna = dados_imoveis[coluna].max()
    min_coluna = dados_imoveis[coluna].min()

    plt.figure(figsize=(10, 6))
    plt.hist(dados_imoveis[coluna], bins=30, edgecolor='k', alpha=0.7)

    plt.xlabel(coluna.capitalize())
    plt.ylabel('Contagem')
    plt.title(f'Distribuição de {coluna.capitalize()}')

    plt.axvline(media_coluna, color='red', linestyle='dashed',
                linewidth=2, label='Média')
    plt.axvline(max_coluna, color='green', linestyle='dashed',
                linewidth=2, label='Máximo')
    plt.axvline(min_coluna, color='blue', linestyle='dashed',
                linewidth=2, label='Mínimo')
    plt.legend()
    plt.show()


def mostrar_grafico_pizza(dados_imoveis, coluna) -> None:
    contagem_valores = dados_imoveis[coluna].value_counts()

    plt.figure(figsize=(10, 6))
    plt.pie(contagem_valores, labels=contagem_valores.index,
            autopct='%1.1f%%', startangle=140)

    plt.title(f'Distribuição de {coluna.capitalize()}')
    plt.show()


def gerar_grafico() -> None:
    dados_imoveis = carregar_dados()
    colunas_original = dados_imoveis.columns

    colunas_nova = {
        "preço": "price",
        "endereço": "address",
        "logradouro": "type",
        "quarto": "bedrooms",
        "banheiro": "bathrooms",
        "estacionamento": "parking",
    }

    print("Colunas disponíveis para análise: ")
    print(list(colunas_nova.keys()))

    coluna = escolher_coluna(colunas_nova)

    if coluna:
        if coluna in colunas_original:
            tipo_coluna = dados_imoveis[coluna].dtype

            if tipo_coluna == "float64" or tipo_coluna == "int64":
                mostrar_histograma(dados_imoveis, coluna)
            elif tipo_coluna == "object":
                mostrar_grafico_pizza(dados_imoveis, coluna)
        else:
            print(f"A coluna '{coluna}' não foi encontrada nos dados.")


gerar_grafico()