# Análise de Dados

## Atenção
Para a aplicação ocorrer sem problemas é necessário fazer esse passo primeiro.


## Passo 1
Para exportar os dados do banco de dados para um arquivo CSV, execute o seguinte comando:

```bash
python export.py
```

Ele irá gerar um arquivo chamado `imoveis.csv` na raiz do projeto.

## Passo 2
Após isso, o arquivo `app.py` poderá ser usado sem problemas. Uso o comando para iniciar a aplicação:

```bash
python app.py
```

Ele mostrar as opções diponíveis de colunas para serem analisadas, e depois irá gerar um gráfico com os dados.

## Passo 3

Exemplo do output e input esperado:

```bash
Colunas disponíveis para análise:
['preço', 'endereço', 'logadouro', 'quarto', 'banheiro', 'estacionamento']
Digite o nome da coluna: preço
```
