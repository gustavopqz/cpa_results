import streamlit as st
import codecs
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CPA - UNEF",
    page_icon="https://gruponobre.instructure.com/users/180/files/1876/preview?verifier=AL1J7B8hBrRCsXzwsiW9gydhXkLV2CzBCUdQHTHQ"
)

st.title("CPA - UNEF 2023.1")

#Código javascript embutido na estrutura html
arquivoJS = codecs.open('./scripts/index.js','r')
codeJS = arquivoJS.read()
components.html(f'<script>{codeJS}</script>')