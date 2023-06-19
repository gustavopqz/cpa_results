from email.policy import default
from winreg import EnableReflectionKey
from click import option
import streamlit as st
import pandas as pd
import codecs
import streamlit.components.v1 as components

#Configuração da página
st.set_page_config(
    page_title="CPA - SUGESTIVAS COORDENADORES",
    page_icon="https://gruponobre.instructure.com/users/180/files/1877/preview?verifier=qCq2GTN60sBAtUP2PrK5JyK4i6RuFYrmWrJJF6gE"
)

df = pd.read_excel(
    io='dados/unifan.xlsx',
    engine='openpyxl',
    sheet_name='sugestiva_coordenador'
)

st.sidebar.header("Filtros")
curso = st.sidebar.multiselect(
    "Cursos",
   options=df["NOME"].unique()
)

df_selection = df.query(
    "NOME == @curso"
)

if not curso:
    st.table(df)
else:
    st.table(df_selection)

#Código javascript embutido na estrutura html
arquivoJS = codecs.open('./scripts/pages.js','r')
codeJS = arquivoJS.read()
components.html(f'<script>{codeJS}</script>')