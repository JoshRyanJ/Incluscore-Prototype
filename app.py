import streamlit as st
import pandas as pd
import altair as alt
from scoring import calculate_csv_scores, calculate_survey_score

# --- APP SETTINGS ---
st.set_page_config(page_title="IncluScore Prototype", layout="wide")

# --- TITLE ---
st.title("🌍 IncluScore Prototype")
st.write("A simple framework to explore digital inclusion scoring.")

# --- SIDEBAR ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Upload & Score", "Dashboard", "Survey"])

# --- HOME PAGE ---
if page == "Home":
    st.header("Hey There! 👋")
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
    st.write("Upload a CSV file with columns: Accessibility, Affordability, Safety.")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("### Raw Data Preview")
            st.dataframe(df)

            # Calculate scores
            scored_df = calculate_csv_scores(df)
            st.write("### Scored Data")
            st.dataframe(scored_df)

            # Save results in session state for dashboard use
            st.session_state["scored_df"] = scored_df

        except Exception as e:
            st.error(f"Error processing file: {e}")

# --- DASHBOARD PAGE ---
elif page == "Dashboard":
    st.header("📊 Dashboard")
    if "scored_df" in st.session_state:
        scored_df = st.session_state["scored_df"]

        st.write("### Average IncluScore")
        avg_score = scored_df["IncluScore"].mean()
        st.metric("Overall Average", f"{avg_score:.2f}")

        st.write("### Score Distribution")
        chart = (
            alt.Chart(scored_df)
            .mark_bar()
            .encode(
                x=alt.X("IncluScore:Q", bin=alt.Bin(maxbins=10)),
                y="count()",
                tooltip=["count()"]
            )
        )
        st.altair_chart(chart, use_container_width=True)
    else:
        st.warning("Please upload data first in the 'Upload & Score' page.")

# --- SURVEY PAGE ---
elif page == "Survey":
    st.header("📝 Survey")
    st.write("Answer the questions to generate your IncluScore.")

    accessibility = st.slider("Accessibility (0–10)", 0, 10, 5)
    affordability = st.slider("Affordability (0–10)", 0, 10, 5)
    safety = st.slider("Safety (0–10)", 0, 10, 5)

    if st.button("Calculate My Score"):
        score = calculate_survey_score(accessibility, affordability, safety)
        st.success(f"Your IncluScore is: {score}")

# --- FOOTER ---
st.markdown("---")
st.markdown(
    """
    💡 Prototype built by **Josiah Ryan Ofosuhene**  
    🔗 [View on GitHub](https://github.com/JoshRyanJ/Incluscore-Prototype)
    """,
    unsafe_allow_html=True
)
