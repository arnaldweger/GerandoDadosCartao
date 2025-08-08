import pandas as pd
import numpy as np
from faker import Faker

fake = Faker('pt_BR')

# Exemplo de valores possíveis para as colunas categóricas
produtos = ['VISA', 'MASTERCARD', 'ELO', 'PIX']
modalidades = ['CRÉDITO À VISTA', 'CRÉDITO PARCELADO', 'DEBITO INSTANTANEO']
options = ['PAGAMENTO', 'RECEBIMENTO', 'ESTORNO']

def gerar_linha_safra():
    valor_bruto = round(np.random.uniform(100, 5000), 2)
    taxa_admn = round(np.random.uniform(1.5, 3.0), 2)
    valor_liquido = round(valor_bruto * (1 - taxa_admn / 100), 2)
    
    return {
        "DATA VENDA": fake.date_between(start_date='-30d', end_date='today').strftime('%d/%m/%Y'),
        "VALOR BRUTO": valor_bruto,
        "TAXA ADMN": taxa_admn,
        "VALOR LIQUIDO": valor_liquido,
        "PRODUTO": np.random.choice(produtos),
        "MODALIDADE": np.random.choice(modalidades),
        "AUTORI": np.random.randint(100000, 999999),
        "TERMINAL": np.random.randint(0, 10),
        "PL": np.random.choice(options)
    }

# Gerar 100 linhas
dados = [gerar_linha_safra() for _ in range(100)]
df = pd.DataFrame(dados)

# Salvar como Excel

df.to_csv("banco.csv", sep=';', decimal=',', index=False )
