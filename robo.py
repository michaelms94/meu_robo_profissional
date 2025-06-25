import datetime
import pandas as pd

#simulação de coleta de dados

def coletar_dados():
    return [
        {"data": datetime.date.today(), "evento": "Processamento finalizado","status": "OK"},
    ]

#salvar um csv
def salvar_relatorio(dados):
    df = pd.DataFrame(dados)
    df.to_csv('dados/relatorio.csv', index=False)
    print("Relatório Salvo com sucesso!")