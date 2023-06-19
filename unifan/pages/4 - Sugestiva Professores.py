from email.policy import default
from winreg import EnableReflectionKey
from click import option
import streamlit as st
import pandas as pd
import codecs
import streamlit.components.v1 as components

#Configuração da página
st.set_page_config(
    page_title="CPA - SUGESTIVAS PROFESSORES",
    page_icon="https://gruponobre.instructure.com/users/180/files/1877/preview?verifier=qCq2GTN60sBAtUP2PrK5JyK4i6RuFYrmWrJJF6gE"
)

df2 = pd.read_excel(
    io='dados/unifan.xlsx',
    engine='openpyxl',
    sheet_name='sugestiva_professor'
)

st.sidebar.header("Filtros")
curso2 = st.sidebar.multiselect(
    "Cursos",
   options=df2["NOME"].unique()
)

df_selection2 = df2.query(
    "NOME == @curso2"
)

if not curso2:
    st.table(df2)
else:
    st.table(df_selection2)

#Código javascript embutido na estrutura html
arquivoJS = codecs.open('./scripts/pages.js','r')
codeJS = arquivoJS.read()
components.html(f'<script>{codeJS}</script>')