import streamlit as st
from PIL import Image

st.title("LOREX")

st.header("En este espacio comienzo a desarollar mis aplicaciones para interfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend")

image = Image.open ("silvestre.png")

st.image(image, caption="Silvestre y Piolín")


texto = st.text_input("Escribe algo", "Lorexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
st.write("el texto escrito es", texto)

st.subheader("ahora usemos 2 columnas")

with col1:
      st.subheader("Esta es la primera columna")
      st.write("Las interfaces multimodales mejoran la experiencia de usuario")
      resp=st.checkbox("Estoy de acuerdo")
      if resp:
            st.write("Correcto")

with col2
st.subheader("Esta es la segunda coulumna")
modo = st.radio("Que Modalidad es la principal en tu interfaz" , ("Visual"," auditiva","Táctil"))
if modo =="Visual";
      st.write("La vista es fundamental para tu interfaz")
