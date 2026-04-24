import pandas as pd
import duckdb
import os


# Caminho da Origem
PATH_ORIGEM = "../data/landing"

# Caminho raw
PATH_RAW = "../data/raw"

def ingest_data():
    print("Iniciando Download dos dados..")

    arquivo_origem = f"{PATH_ORIGEM}/electronics_sales_raw.csv"

    if not os.path.exists(arquivo_origem):
        print(f"Aguardando arquivo em {arquivo_origem}")
        return

    df = pd.read_csv(arquivo_origem)
    
    arquivo_destino = f"{PATH_RAW}/dados_brutos.parquet"

    duckdb.sql(f"COPY (SELECT * FROM df) TO '{arquivo_destino}' (FORMAT PARQUET)")

    print(f"Sucesso! Dados salvos na cama Raw em: {arquivo_destino}")

if __name__ == "__main__":
    ingest_data()
