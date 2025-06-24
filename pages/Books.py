import streamlit as st
import pandas as pd

# Inject custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📖 Our Books Collection")

books = pd.read_csv("data/books.csv")

for index, row in books.iterrows():
    st.markdown(f"""
    <div class="book-box">
        <h2>{row["Title"]}</h2>
        <p><strong>Author:</strong> {row["Author"]}</p>
        <p>{row["Description"]}</p>
        <img src="assets/covers/{row['Image']}" width="150">
    </div>
    """, unsafe_allow_html=True)
