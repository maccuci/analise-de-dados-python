
import pandas as pd
from sqlalchemy import create_engine

# use essa função para exportar o banco de dados em mysql para um arquivo csv.


def exportar_db() -> None:
    engine = create_engine('mysql+mysqlconnector://root:@localhost/mozart')
    consulta = 'SELECT * FROM imovel'

    df = pd.read_sql_query(consulta, engine)

    df.to_csv("imoveis.csv", index=False)
    print("O arquvio imoveis.csv foi criado com sucesso.")


exportar_db()
