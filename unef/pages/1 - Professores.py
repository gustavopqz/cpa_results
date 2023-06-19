import streamlit as st
import pandas as pd
import altair as alt
import dados.dados_professores as dados
import codecs
import streamlit.components.v1 as components

#Configuração da página
st.set_page_config(
    page_title="CPA - PROFESSORES",
    page_icon="https://gruponobre.instructure.com/users/180/files/1876/preview?verifier=AL1J7B8hBrRCsXzwsiW9gydhXkLV2CzBCUdQHTHQ"
)

# IMPORTAÇÃO DA PLANILHA RESPOSTAS
df = pd.read_excel(
    io='dados/unef.xlsx',
    engine='openpyxl',
    sheet_name='professor'
)
# IMPORTAÇÃO DA PLANILHA PERGUNTAS
df_perguntas = pd.read_excel(
    io='dados/unef.xlsx',
    engine='openpyxl',
    sheet_name='perguntas_professor'
)
df_perguntas.set_index('id', inplace=True)
# CABEÇALHO DO FILTRO
st.sidebar.header("Filtros")

# CARREGA FILTRO PROFESSOR 
professor = st.sidebar.multiselect(
    "Professor",
   options=df["resp_teacher_name"].unique()
)

# TRATA FILTRO TURMAS DE ACORDO COM O PROFESSOR SELECIONADO
if professor:
    prof_select = df.query(
    "(resp_teacher_name == @professor)"
    )
    turma = st.sidebar.multiselect(
        "Turma",
    options=prof_select["TURMA"].unique()
    )
else:
    turma = st.sidebar.multiselect(
        "Turma",
    options=df["TURMA"].unique()
    )

# SOMA DAS RESPOSTAS, VALIDANDO O PREENCHIMENTO DOS FILTROS PROFESSOR E TURMA
if not (professor) and not (turma):
    dtframe = dados.detalhe_perguntas(df)
    total_excelente = int(df["EXCELENTE"].sum())
    total_otimo = int(df["ÓTIMO"].sum())
    total_bom= int(df["BOM"].sum())
    total_regular= int(df["REGULAR"].sum())
    total_insuficiente= int(df["INSUFICIENTE"].sum())
    total_respostas = (total_insuficiente+total_regular+total_bom+ total_otimo+ total_excelente)
elif not (professor):
    df_selection = df.query(
    "(TURMA == @turma)"
    )
    dtframe = dados.detalhe_perguntas(df_selection)
    total_excelente = int(df_selection["EXCELENTE"].sum())
    total_otimo = int(df_selection["ÓTIMO"].sum())
    total_bom= int(df_selection["BOM"].sum())
    total_regular= int(df_selection["REGULAR"].sum())
    total_insuficiente= int(df_selection["INSUFICIENTE"].sum())
    total_respostas = (total_insuficiente+total_regular+total_bom+ total_otimo+ total_excelente)
elif not (turma):
    df_selection = df.query(
    "(resp_teacher_name == @professor)"
    )
    dtframe = dados.detalhe_perguntas(df_selection)
    total_excelente = int(df_selection["EXCELENTE"].sum())
    total_otimo = int(df_selection["ÓTIMO"].sum())
    total_bom= int(df_selection["BOM"].sum())
    total_regular= int(df_selection["REGULAR"].sum())
    total_insuficiente= int(df_selection["INSUFICIENTE"].sum())
    total_respostas = (total_insuficiente+total_regular+total_bom+ total_otimo+ total_excelente)
else:
    df_selection = df.query(
    "(resp_teacher_name == @professor & TURMA == @turma)"
    )
    dtframe = dados.detalhe_perguntas(df_selection)
    total_excelente = int(df_selection["EXCELENTE"].sum())
    total_otimo = int(df_selection["ÓTIMO"].sum())
    total_bom= int(df_selection["BOM"].sum())
    total_regular= int(df_selection["REGULAR"].sum())
    total_insuficiente= int(df_selection["INSUFICIENTE"].sum())
    total_respostas = (total_insuficiente+total_regular+total_bom+ total_otimo+ total_excelente)

#TÍTULO DAS PORCENTAGENS
st.markdown('PERCENTUAL GERAL')

# CRIAÇÃO DAS COLUNAS
col1, col2, col3, col4, col5 = st.columns(5)

# CRIANDO VARIÁVEIS DOS CAMPOS DE PORCENTAGEM
percent_insuficiente = ((total_insuficiente*100)/total_respostas)
percent_regular = ((total_regular*100)/total_respostas)
percent_bom = ((total_bom*100)/total_respostas)
percent_otimo = ((total_otimo*100)/total_respostas)
percent_excelente = ((total_excelente*100)/total_respostas)

# EXIBINDO MÉTRICAS DE PORCENTAGEM
col1.metric("Insuficiente (%)", '{0:.2f}'.format(percent_regular))
col2.metric("Regular (%)", '{0:.2f}'.format(percent_insuficiente))
col3.metric("Bom (%)", '{0:.2f}'.format(percent_bom))
col4.metric("Ótimo (%)", '{0:.2f}'.format(percent_otimo))
col5.metric("Excelente (%)", '{0:.2f}'.format(percent_excelente))


#TÍTULO DO GRÁFICO POR QUANTIDADE
st.markdown('AVALIAÇÕES POR QUANTIDADE')

# EXIBINDO GRAFICO DE QUANTIDADE DE RESPOSTAS POR AVALIAÇÃO
source = pd.DataFrame({
    'Respostas':[total_insuficiente,total_regular,total_bom,total_otimo,total_excelente],
    'Avaliação':['1 - Insuficiente','2 - Regular','3 - Bom','4 - Ótimo','5 - Excelente']
    
    })

bar_chart = alt.Chart(source).mark_bar().encode(
    y = 'Respostas',
    x = 'Avaliação'
)
st.altair_chart(bar_chart, use_container_width=True)


bars = alt.Chart(dtframe).mark_bar().encode(
    x=alt.X('sum(Respostas):Q', stack='zero'),
    y=alt.Y('Pergunta:N'),
    color=alt.Color('Avaliação')
)

#TÍTULO DO GRÁFICO POR PERCENTUAL
st.markdown('PERCENTUAL POR PERGUNTA')

text = alt.Chart(dtframe).mark_text(dx=-15, dy=3, color='white').encode(
    x=alt.X('sum(Respostas):Q',  stack='zero'),
    y=alt.Y('Pergunta:N'),
    detail='Avaliação:N',
    text=alt.Text('sum(Respostas):Q', format='.2f')
)
st.altair_chart(bars+text, use_container_width=True)


#TÍTULO DA LEGENDA DAS PERGUNTAS
st.markdown('PERGUNTAS')

# EXIBE LEGENDA DAS PERGUNTAS
st.table(df_perguntas)
# st.table(dtframe)


#Código javascript embutido na estrutura html
arquivoJS = codecs.open('./scripts/pages.js','r')
codeJS = arquivoJS.read()
components.html(f'<script>{codeJS}</script>')