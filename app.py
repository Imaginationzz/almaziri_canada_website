import streamlit as st
st.set_page_config(page_title="Publishing House", layout="wide")
# Inject custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



st.title("📚 Welcome to Our Publishing House")
st.write("Discover our latest and most popular titles. Visit the **Books** page to explore our collection.")
st.image("assets/covers/banner.jpg", use_container_width=True)

