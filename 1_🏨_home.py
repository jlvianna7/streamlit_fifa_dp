import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime


st.set_page_config(
    page_title="Fifa 2023",
    page_icon="🧊",  # Usando um emoji
    layout="wide"
)


if "dados" not in st.session_state:
    df_dados = pd.read_csv(
        "./datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_dados = df_dados[df_dados["Contract Valid Until"]
                        >= datetime.today().year]
    df_dados = df_dados[df_dados["Value(£)"] > 0]
    df_dados = df_dados.sort_values(by="Overall", ascending=False)
    st.session_state["dados"] = df_dados


st.markdown('# FIFA 2023 OFFICIAL DATASET! :soccer:')
st.sidebar.markdown(":soccer: Desenvolvido por [Joao](https://www.google.com)")

btn = st.button("Acesse os dados no Keggle :soccer:")
if btn:
    webbrowser.open_new_tab(
        "https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database")

st.markdown(
    """
**Conjunto de dados**

O conjunto de dados contém **mais de 17 mil jogadores** únicos e mais de 60 colunas , 
incluindo informações gerais e todos os KPIs que o famoso videogame oferece. 
Como o cenário de e-sports continua crescendo, especialmente no FIFA, 
achei que poderia ser útil para a comunidade (participantes do Kaggle e/ou jogadores.

**Contexto**

Os dados foram obtidos graças a um rastreador que implementei para realizar a coleta:
Dados agregados , como nome dos jogadores , idade , país.
Dados detalhados como potencial ofensivo , defensivo e de aceleração. Eu gosto muito de futebol e este conjunto de dados é para mim uma oportunidade de contribuir para a realização de projetos que podem ir desde uma simples análise até a elaboração de estratégias para a composição ideal da equipe sob certas restrições.
Agradecimentos
Não estaríamos aqui sem a ajuda de outros. Gostaria de agradecer a @karangadiya , de quem me inspirei. Confira o repositório dele aqui !
    """
)
