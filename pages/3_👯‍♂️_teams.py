import streamlit as st

st.set_page_config(
    page_title="Fifa 2023",
    page_icon="🧊",  # Usando um emoji
    layout="wide"
)

df_dados = st.session_state["dados"]

clubes = df_dados["Club"].unique()
clube_sel = st.sidebar.selectbox("Clube", clubes)

df_filtered = df_dados[(df_dados["Club"] == clube_sel)].set_index("Name")

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {clube_sel}")

columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", "Joined", "Height(cm.)", "Weight(lbs.)",
           "Contract Valid Until", "Release Clause(£)"]

st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d", min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn(
                     "Weekly Wage", format="£%f", min_value=0, max_value=df_filtered["Wage(£)"].max()
                 ),
    "Photo": st.column_config.ImageColumn(),
    "Flag": st.column_config.ImageColumn("Country"),
})
