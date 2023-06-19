import streamlit as st
import codecs
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CPA - UNIFAN",
    page_icon="https://gruponobre.instructure.com/users/180/files/1877/preview?verifier=qCq2GTN60sBAtUP2PrK5JyK4i6RuFYrmWrJJF6gE"
)

st.title("CPA - UNIFAN 2023.1")

#Código javascript embutido na estrutura html
arquivoJS = codecs.open('./scripts/index.js','r')
codeJS = arquivoJS.read()
components.html(f'<script>{codeJS}</script>')