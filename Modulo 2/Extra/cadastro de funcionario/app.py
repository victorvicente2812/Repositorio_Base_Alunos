import streamlit as st
st.title("Victor RH")
### Coloque uma logo na barra lateral
st.sidebar.image("Victor RH.png")
###
nome = st.text_input("Digite o nome do Funcionário")
idade= st.text_input("Digite a idade do Funcionário")
email= st.text_input("Digite o email do Funcionário")
salario= st.text_input("Digite o salário do Funcionário")
cargo= st.text_input("Digite o cargo do Funcionário")

if st.button("Cadastrar"):
    st.warning(f"O Funcionário {nome}, foi cadastrado com sucesso")
    st.balloons()
    st.image('https://thispersondoesnotexist.com/')