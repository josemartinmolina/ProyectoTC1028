import streamlit as st

st.title("¿Par o impar?")

numero = st.number_input("Ingresa un número", step=1, format="%d")

if numero != 0 or numero == 0:  # Para mostrar resultado siempre que se haya ingresado algo
    if numero % 2 == 0:
        st.success(f"{int(numero)} es par.")
    else:
        st.info(f"{int(numero)} es impar.")
