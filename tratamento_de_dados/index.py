import pandas as pd

# Descomentar somente o passo a ser usado

# Primeiro passo - Retirar votos duplicados
# df = pd.read_excel('resultado_retirado_do_sql.xlsx')

# insuficiente = df['INSUFICIENTE']
# regular = df['REGULAR']
# bom = df['BOM']
# otimo = df['ÓTIMO']
# excelente = df['EXCELENTE']

# for indice, voto in insuficiente.iteritems():
#     if voto > 1:
#         df.at[indice, 'INSUFICIENTE'] = 1
# for indice, voto in regular.iteritems():
#     if voto > 1:
#         df.at[indice, 'REGULAR'] = 1
# for indice, voto in bom.iteritems():
#     if voto > 1:
#         df.at[indice, 'BOM'] = 1
# for indice, voto in otimo.iteritems():
#     if voto > 1:
#         df.at[indice, 'ÓTIMO'] = 1
# for indice, voto in excelente.iteritems():
#     if voto > 1:
#         df.at[indice, 'EXCELENTE'] = 1

# df.to_excel('repeticao_removida.xlsx')    

# Segundo passo - Agrupar
# df = pd.read_excel('repeticao_removida.xlsx')
# agrupado = df.groupby(['CURSO', 'idpergunta', 'Pergunta']).sum() # Necessário colocar cada nome de coluna do arquivo em questão
# agrupado.to_excel('agrupado.xlsx')

# Depois de agrupar é necessário abrir o arquivo e desmesclar as colunas mescladas

# Terceiro passo - Após desmesclar, completar células vazias
# df = pd.read_excel('agrupado.xlsx')
# df_filled = df.fillna(method='ffill')
# df_filled.to_excel('final.xlsx', index=False)