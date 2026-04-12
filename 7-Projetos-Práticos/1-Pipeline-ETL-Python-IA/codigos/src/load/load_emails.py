from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")


if not all([DB_USER, DB_PASSWORD, DB_NAME]):
    raise ValueError("Variáveis de ambiente do banco não configuradas corretamente")


def ler_email_data_load(file_path):
    try:
        email_data = pd.read_csv(file_path)
        return email_data
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None


def get_engine():
    return create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


def normalize_schema(df):
    return df.rename(columns={
        "from": "sender",
        "date": "email_date"
    })


def load_to_postgres(df: pd.DataFrame):
    try:
        engine = get_engine()

        print(f"Inserindo {len(df)} registros no PostgreSQL...")

        df.to_sql(
            name="emails",
            con=engine,
            if_exists="append",
            index=False
        )

        print("✔ Dados carregados com sucesso no PostgreSQL!")

    except Exception as e:
        print(f"Erro ao carregar no banco: {e}")