import pandas as pd
import os

def carregar_csv(caminho_arquivo, separador=',', encoding='utf-8'):
    """Carrega um arquivo CSV em um DataFrame do pandas.

    Args:
        caminho_arquivo (str): _description_
        separador (str, optional): _description_. Defaults to ','.
        encoding (str, optional): _description_. Defaults to 'utf-8'.
    """

    try:
        df = pd.read_csv(caminho_arquivo, sep=separador, encoding=encoding)
        print("\nArquivo carregado com sucesso!")
        print(f"Linhas: {df.shape[0]}, Colunas: {df.shape[1]}")
        print("\nPrimeiras linhas do arquivo:")
        print(df.head())
        return df

    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
    except pd.errors.ParserError:
        print("Erro ao interpretar o CSV. Verifique o separador ou formato.")
    except UnicodeDecodeError:
        print("Erro de codificação. Tente mudar o parâmetro 'encoding'.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


def gerar_amostra(df, linhas=5):
    """Gera uma amostra de emails do DataFrame.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados dos emails.
        linhas (int, optional): Número de linhas na amostra. Defaults to 5.

    Returns:
        pd.DataFrame: Amostra de dados.
    """

    try:
        if df is not None and not df.empty:
            sample_df = df.sample(n=linhas)
            print("\nAmostra de dados extraída:")
            print(sample_df)
            return sample_df
        else:
            print("O DataFrame está vazio ou não foi carregado corretamente.")
            return None
        
    except Exception as e:
        print(f"Ocorreu um erro ao extrair a amostra: {e}")
        return None
    

def salvar_amostra(sample_df, caminho_saida):
    """Salva a amostra em um arquivo CSV, garantindo que o diretório exista.

    Args:
        sample_df (pd.DataFrame): Amostra de dados
        caminho_saida (str): Caminho para salvar o arquivo
    """

    try:
        if sample_df is not None and not sample_df.empty:

            diretorio = os.path.dirname(caminho_saida)

            if diretorio:
                os.makedirs(diretorio, exist_ok=True)

            sample_df.to_csv(caminho_saida, index=False, encoding='utf-8')

            print(f"Amostra salva com sucesso em '{caminho_saida}'")

        else:
            print("A amostra de dados está vazia ou não foi gerada corretamente.")

    except Exception as e:
        print(f"Ocorreu um erro ao salvar a amostra: {e}")