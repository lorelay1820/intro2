import streamlit as st
from PIL import Image

st.title("LOREX")

st.header("En este espacio comienzo a desarollar mis aplicaciones para interfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend")

image = Image.open ("silvestre.png")

st.image(image, caption="Silvestre y Piolín")


texto = st.text_input("Escribe algo", "este es mi text")
st.write("el texto escrito es", texto)

st.subheader("ahora usemos 2 columnas")
      
