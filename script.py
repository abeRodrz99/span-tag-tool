import streamlit as st
from bs4 import BeautifulSoup

st.title("HTML <span> Tag Remover")
st.write("Paste your HTML below. This tool will remove all `<span>` tags but keep the content inside.")

html_input = st.text_area("Paste HTML Here:", height=200)

if st.button("Remove <span> Tags"):
    soup = BeautifulSoup(html_input, "html.parser")
    
    for span in soup.find_all("span"):
        span.unwrap()
    
    st.text_area("Cleaned HTML:", value=soup.prettify(), height=200)

