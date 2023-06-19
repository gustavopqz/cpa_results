import pandas as pd
def detalhe_perguntas(dtframe):
    p1_insuficiente = retornap1_insuficiente(dtframe)
    p1_regular = retornap1_regular(dtframe)
    p1_bom = retornap1_bom(dtframe)
    p1_otimo = retornap1_otimo(dtframe)
    p1_excelente = retornap1_excelente(dtframe)
    p2_insuficiente = retornap2_insuficiente(dtframe)
    p2_regular = retornap2_regular(dtframe)
    p2_bom = retornap2_bom(dtframe)
    p2_otimo = retornap2_otimo(dtframe)
    p2_excelente = retornap2_excelente(dtframe)
    newframe = [
    {'Pergunta': '1',
     'Avaliação': '5 - Excelente',
     'Respostas': p1_excelente},
     {'Pergunta': '1',
     'Avaliação': '4 - Ótimo',
     'Respostas': p1_otimo},
     {'Pergunta': '1',
     'Avaliação': '3 - Bom',
     'Respostas': p1_bom},
     {'Pergunta': '1',
     'Avaliação': '2 - Regular',
     'Respostas': p1_regular},
     {'Pergunta': '1',
     'Avaliação': '1 - Insuficiente',
     'Respostas': p1_insuficiente},
     {'Pergunta': '2',
     'Avaliação': '5 - Excelente',
     'Respostas': p2_excelente},
     {'Pergunta': '2',
     'Avaliação': '4 - Ótimo',
     'Respostas': p2_otimo},
     {'Pergunta': '2',
     'Avaliação': '3 - Bom',
     'Respostas': p2_bom},
     {'Pergunta': '2',
     'Avaliação': '2 - Regular',
     'Respostas': p2_regular},
     {'Pergunta': '2',
     'Avaliação': '1 - Insuficiente',
     'Respostas': p2_insuficiente}
    ]
    df = pd.DataFrame(newframe)
    # df_semzeros = df[df['Respostas'] > "0.00"]
    return df

# CÁLCULO PERGUNTA 1
def retorna_total_p1(frame):
    p1 = pd.DataFrame(frame)
    total_p1 = int(p1["INSUFICIENTE"].sum() + p1["REGULAR"].sum() + p1["BOM"].sum() + p1["ÓTIMO"].sum() + p1["EXCELENTE"].sum())
    return total_p1

def retornap1_excelente(frame):
    data = pd.DataFrame(frame)
    p1 = data.query("idpergunta == 1")
    total_p1 = retorna_total_p1(p1)
    total_excelente = int(p1["EXCELENTE"].sum())
    percent = ((total_excelente * 100) / total_p1)
    return percent
 
def retornap1_otimo(frame):
    data = pd.DataFrame(frame)
    p1 = data.query("idpergunta == 1")
    total_p1 = retorna_total_p1(p1)
    total_otimo = int(p1["ÓTIMO"].sum())
    percent = ((total_otimo * 100) / total_p1)
    return percent

def retornap1_bom(frame):
    data = pd.DataFrame(frame)
    p1 = data.query("idpergunta == 1")
    total_p1 = retorna_total_p1(p1)
    total_bom = int(p1["BOM"].sum())
    percent = ((total_bom * 100) / total_p1)
    return percent

def retornap1_regular(frame):
    data = pd.DataFrame(frame)
    p1 = data.query("idpergunta == 1")
    total_p1 = retorna_total_p1(p1)
    total_regular = int(p1["REGULAR"].sum())
    percent = ((total_regular * 100) / total_p1)
    return percent

def retornap1_insuficiente(frame):
    data = pd.DataFrame(frame)
    p1 = data.query("idpergunta == 1")
    total_p1 = retorna_total_p1(p1)
    total_insuficiente = int(p1["INSUFICIENTE"].sum())
    percent = ((total_insuficiente * 100) / total_p1)
    return percent

# CÁLCULO PERGUNTA 2
def retorna_total_p2(frame):
    p2 = pd.DataFrame(frame)
    total_p2 = int(p2["INSUFICIENTE"].sum() + p2["REGULAR"].sum() + p2["BOM"].sum() + p2["ÓTIMO"].sum() + p2["EXCELENTE"].sum())
    return total_p2

def retornap2_excelente(frame):
    data = pd.DataFrame(frame)
    p2 = data.query("idpergunta == 2")
    total_p2 = retorna_total_p2(p2)
    total_excelente = int(p2["EXCELENTE"].sum())
    percent = ((total_excelente * 100) / total_p2)
    return percent
 
def retornap2_otimo(frame):
    data = pd.DataFrame(frame)
    p2 = data.query("idpergunta == 2")
    total_p2 = retorna_total_p2(p2)
    total_otimo = int(p2["ÓTIMO"].sum())
    percent = ((total_otimo * 100) / total_p2)
    return percent

def retornap2_bom(frame):
    data = pd.DataFrame(frame)
    p2 = data.query("idpergunta == 2")
    total_p2 = retorna_total_p2(p2)
    total_bom = int(p2["BOM"].sum())
    percent = ((total_bom * 100) / total_p2)
    return percent

def retornap2_regular(frame):
    data = pd.DataFrame(frame)
    p2 = data.query("idpergunta == 2")
    total_p2 = retorna_total_p2(p2)
    total_regular = int(p2["REGULAR"].sum())
    percent = ((total_regular * 100) / total_p2)
    return percent

def retornap2_insuficiente(frame):
    data = pd.DataFrame(frame)
    p2 = data.query("idpergunta == 2")
    total_p2 = retorna_total_p2(p2)
    total_insuficiente = int(p2["INSUFICIENTE"].sum())
    percent = ((total_insuficiente * 100) / total_p2)
    return percent

