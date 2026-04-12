import os
import json
import re
import pandas as pd
import requests
from dotenv import load_dotenv

# =========================
# CONFIG
# =========================

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY não encontrada no .env")

URL = "https://api.deepseek.com/v1/chat/completions"


def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path, sep=";")
        print(f"Dataset carregado: {df.shape}")
        return df
    except Exception as e:
        print(f"Erro ao carregar CSV: {e}")
        return pd.DataFrame()


def build_prompt(row):
    return f"""
Você é um sistema de engenharia de dados responsável por limpar e normalizar dados de emails.

REGRAS OBRIGATÓRIAS:
- Retorne APENAS JSON puro
- NÃO use markdown
- NÃO use ```json
- NÃO escreva texto extra

TAREFA:
- from: extraia apenas o email válido
- subject: normalize e limpe texto
- date: converta para formato YYYY-MM-DD HH:MM:SS
- target: garanta 0 ou 1

ENTRADA:
from: {row['from']}
subject: {row['subject']}
date: {row['date']}
target: {row['target']}

SAÍDA:
{{
  "from": "",
  "subject": "",
  "date": "",
  "target": 0
}}
"""

def call_deepseek(prompt: str):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.1
    }

    response = requests.post(URL, headers=headers, json=payload, timeout=30)

    if response.status_code != 200:
        print("ERRO API:", response.status_code)
        print(response.text)
        return None

    return response.json()


def parse_response(response):
    try:
        content = response["choices"][0]["message"]["content"]

        if not content:
            return None

        # 🔥 remove markdown da IA
        content = re.sub(r"```json", "", content)
        content = re.sub(r"```", "", content)

        content = content.strip()

        return json.loads(content)

    except Exception as e:
        print("Erro ao parsear resposta:", e)
        print("RAW:", response)
        return None


def normalize_row(row):
    prompt = build_prompt(row)
    response = call_deepseek(prompt)

    if response is None:
        return {
            "from": None,
            "subject": None,
            "date": None,
            "target": row.get("target", None)
        }

    result = parse_response(response)

    if result is None:
        return {
            "from": None,
            "subject": None,
            "date": None,
            "target": row.get("target", None)
        }

    return result


def enrich_dataframe(df):
    results = []

    for i, row in df.iterrows():
        print(f"Processando linha {i+1}/{len(df)}")

        cleaned = normalize_row(row)
        results.append(cleaned)

    return pd.DataFrame(results)