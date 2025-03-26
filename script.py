import streamlit as st
from bs4 import BeautifulSoup

# Streamlit text area to input HTML code
input_text = st.text_area("Paste your HTML code here...", height=200)

# Function to process HTML when the button is clicked
def process_html():
    html_content = input_text
    soup = BeautifulSoup(html_content, "html.parser")

    # Remove <span> tags
    for span in soup.find_all("span"):
        span.unwrap()

    # Display updated HTML
    st.text_area("Updated HTML will appear here...", value=str(soup.prettify()), height=200)

# Button to trigger the processing
if st.button("Remove <span> Tags"):
    process_html()
