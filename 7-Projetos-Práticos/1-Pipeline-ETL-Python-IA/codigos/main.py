from src.extract.extract_emails import carregar_csv, gerar_amostra, salvar_amostra
from config.settings import RAW_DATA_PATH, SAMPLE_DATA_PATH, PROCESSED_DATA_PATH, ENRICHED_DATA_PATH
from src.transform.parse_email import ler_email_data, extrair_informacoes_email, salvar_resultados_csv
from src.enrich.enrich_emails import load_data, enrich_dataframe
from src.load.load_emails import ler_email_data_load, normalize_schema, load_to_postgres


def etapa_extracao():
    try:
        # ETAPA 1: Extração
        raw_df = carregar_csv(RAW_DATA_PATH, separador=',', encoding='utf-8')
        sample_df = gerar_amostra(raw_df)
        salvar_amostra(sample_df, SAMPLE_DATA_PATH)
    except Exception as e:
        print("Erro na etapa de extração:", e)


def etapa_transformacao():
    try:
        # ETAPA 2: Transformação
        email_data = ler_email_data(SAMPLE_DATA_PATH)
        resultados = extrair_informacoes_email(email_data)
        salvar_resultados_csv(resultados, PROCESSED_DATA_PATH)
    except Exception as e:
        print("Erro na etapa de transformação:", e)

def etapa_enriquecimento():
    try:
        # ETAPA 3: Enriquecimento
        enrich_df = load_data(PROCESSED_DATA_PATH)

        if enrich_df.empty:
            print("Dataset vazio. Abortando.")
            return

        df_clean = enrich_dataframe(enrich_df)
        df_clean.to_csv(ENRICHED_DATA_PATH, index=False)

        print(f"Processo finalizado! Arquivo salvo em: {ENRICHED_DATA_PATH}")
    except Exception as e:
        print("Erro na etapa de enriquecimento:", e)


def carregar_dados_banco():
    try:
        # ETAPA 4: Carregar no Banco
        df = ler_email_data_load("data/ai_processed/emails_enriched.csv")
        df = normalize_schema(df)
        load_to_postgres(df)
    except Exception as e:
        print("Erro ao carregar dados no banco:", e)


if __name__ == "__main__":

    etapa_extracao()

    etapa_transformacao()

    etapa_enriquecimento()

    carregar_dados_banco()