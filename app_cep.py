import streamlit as st
import pandas as pd
import requests

st.title("Busca CEP")

URL = "https://viacep.com.br/ws/{cep}/json"

cep = st.text_input("Digite seu CEP")

if cep != "":

    try: 
        resp = requests.get(URL.format(cep=cep))
        data = pd.DataFrame([resp.json()])
        st.dataframe(data, hide_index=True)
    except Exception as err:
        st.error("Insira um CEP válido.")