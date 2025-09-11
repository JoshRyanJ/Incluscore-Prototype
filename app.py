import streamlit as st
import pandas as pd

st.title("InkluScore Prototype")
st.write("Testing a simple scoring framework for digital inclusion.")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Raw Data Preview")
    st.dataframe(df)

    import streamlit as st

# --- APP TITLE ---
st.set_page_config(page_title="InkluScore Prototype", layout="wide")
st.title("🌍 InkluScore Prototype")
st.write("A simple framework to explore digital inclusion scoring.")

# --- SIDEBAR ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Upload & Score", "Dashboard", "Survey"])

# --- HOME PAGE ---
if page == "Home":
    st.header("Welcome 👋")
    st.write("""
        This is a prototype app for testing digital inclusion scoring.
        You can:
        - Upload a CSV with sample scores  
        - See how they are combined into an inclusion score  
        - Explore results in a dashboard view  
        - Try a simple survey experiment  
    """)

# --- UPLOAD & SCORE PAGE ---
elif page == "Upload & Score":
    st.header("📂 Upload Your Data")
    st.write("Upload a CSV file to calculate and view scores.")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# --- DASHBOARD PAGE ---
elif page == "Dashboard":
    st.header("📊 Dashboard")
    st.write("Visualize the results here (charts & tables coming soon).")

# --- SURVEY PAGE ---
elif page == "Survey":
    st.header("📝 Survey")
    st.write("A simple survey experiment will go here.")

    # --- FOOTER ---
st.markdown("---")
st.markdown(
    """
    💡 Prototype built by **Josiah Ryan Ofosuhene**  
    🔗 [View on GitHub](https://github.com/JoshRyanJ/Incluscore-Prototype)
    """,
    unsafe_allow_html=True
)

