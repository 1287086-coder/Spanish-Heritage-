import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="Word Cloud Generator", page_icon="☁️")

st.title("☁️ Word Cloud Generator")
st.write("Enter some text below and generate a word cloud!")

# User input
text = st.text_area("Paste your text here:", height=200)

if st.button("Generate Word Cloud"):
    if text.strip():
        wc = WordCloud(width=800, height=400, background_color="white").generate(text)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wc, interpolation="bilinear")
        ax.axis("off")

        st.pyplot(fig)
    else:
        st.warning("⚠️ Please enter some text before generating.")
