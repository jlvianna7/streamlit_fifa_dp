import streamlit as st

st.set_page_config(
    page_title="Fifa 2023",
    page_icon="🧊",  # Usando um emoji
    layout="wide"
)


df_dados = st.session_state["dados"]

# clubes = df_dados["Club"].value_counts().index
# ou conforme abaixo
clubes = df_dados["Club"].unique()
clube_sel = st.sidebar.selectbox("Clube", clubes)

df_jogadores = df_dados[(df_dados["Club"] == clube_sel)]
jogadores = df_jogadores["Name"].unique()
jogador = st.sidebar.selectbox("Jogador", jogadores)

dados_jogador = df_dados[df_dados["Name"] == jogador].iloc[0]

st.image(dados_jogador["Photo"])
st.title(dados_jogador["Name"])
st.markdown(f"**Clube:** {dados_jogador['Club']}")
st.markdown(f"**Posição:** {dados_jogador['Position']}")

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"**Idade:** {dados_jogador['Age']}")

# col2.markdown(f"**Altura:** {dados_jogador['Height(cm.)']}")
# col3.markdown(f"**Peso:** {dados_jogador['Weight(lbs.)']}")

# Com foramatação ajustada formatação
col2.markdown(f"**Altura:** {dados_jogador['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {dados_jogador['Weight(lbs.)']*0.453:0.2f}")

# Seção inferior
st.divider()
st.subheader(f"Overall: {dados_jogador['Overall']}")
st.progress(int(dados_jogador["Overall"]))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£{dados_jogador['Value(£)']:,}")
col2.metric(label="Remuneração semanal",
            value=f"£{dados_jogador['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão",
            value=f"£{dados_jogador['Release Clause(£)']:,}")
