import pandas as pd
import re


def ler_email_data(file_path):
    try:
        email_data = pd.read_csv(file_path)
        return email_data
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

def extrair_informacoes_email(email_data):
    resultados = []
    
    for index, row in email_data.iterrows():
        email_text = str(row['text'])
        target = row['target']
        
        email_dict = {}
        
        match_from = re.search(r'From:\s*(.+?)(?=\s+[A-Za-z-]+:)', email_text)
        if match_from:
            email_dict['from'] = match_from.group(1).strip()
        else:
            email_dict['from'] = None
        
        match_subject = re.search(r'Subject:\s*(.+?)(?=\s+[A-Za-z-]+:)', email_text)
        if match_subject:
            email_dict['subject'] = match_subject.group(1).strip()
        else:
            email_dict['subject'] = None
        
        match_date = re.search(r'Date:\s*(.+?)(?=\s+[A-Za-z-]+:)', email_text)
        if match_date:
            email_dict['date'] = match_date.group(1).strip()
        else:
            email_dict['date'] = None
        
        email_dict['target'] = target
        
        resultados.append(email_dict)
    
    return resultados


def salvar_resultados_csv(resultados, output_path):
    try:
        df_resultados = pd.DataFrame(resultados)
        df_resultados.to_csv(output_path, sep=';', index=False)
        print(f"Arquivo salvo em {output_path}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")