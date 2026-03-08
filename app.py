# app.py — IncluScore AI
# Streamlit prototype for evaluating EdTech platforms
# against WCAG 2.1, UDL, UNICEF child-safety standards, and UN SDG 4.
#
# Author: Josiah Ryan Ofosuhene
# Version: 2.0

import streamlit as st
import pandas as pd
import altair as alt
from scoring import (
    calculate_survey_score,
    calculate_csv_scores,
    print_score_report,
    PILLAR_WEIGHTS,
    ALL_CRITERIA,
    get_verdict,
)

# ── PAGE CONFIG ──────────────────────────────
st.set_page_config(
    page_title="IncluScore AI",
    page_icon="IS",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CUSTOM CSS ───────────────────────────────
st.markdown("""
<style>
    /* Main background */
    .stApp { background-color: #0D1B2A; }
    .main .block-container { padding-top: 2rem; }

    /* Sidebar */
    [data-testid="stSidebar"] { background-color: #132338; }
    [data-testid="stSidebar"] .stRadio label { color: #8BA3BC !important; font-size: 0.9rem; }

    /* Headers */
    h1 { color: #FFFFFF !important; font-size: 2rem !important; }
    h2 { color: #FFFFFF !important; font-size: 1.4rem !important; }
    h3 { color: #00C9A7 !important; font-size: 1.1rem !important; }

    /* Metric cards */
    [data-testid="stMetric"] {
        background: #152032;
        border: 1px solid rgba(139,163,188,0.15);
        border-radius: 10px;
        padding: 1rem;
    }
    [data-testid="stMetricValue"] { color: #00C9A7 !important; }
    [data-testid="stMetricLabel"] { color: #8BA3BC !important; }

    /* Success / warning / error */
    .stSuccess { background: rgba(0,201,167,0.1) !important; }
    .stWarning { background: rgba(244,197,66,0.1) !important; }
    .stError   { background: rgba(220,53,69,0.1) !important; }

    /* Slider labels */
    .stSlider label { color: #CBD5E1 !important; font-size: 0.88rem !important; }

    /* Expander */
    details summary { color: #8BA3BC !important; }

    /* Dataframe */
    .stDataFrame { background: #152032; }

    /* Score badge */
    .score-badge {
        display: inline-block;
        font-size: 3rem;
        font-weight: 800;
        color: #00C9A7;
        padding: 0.5rem 1.5rem;
        border: 3px solid rgba(0,201,167,0.4);
        border-radius: 12px;
        background: rgba(0,201,167,0.06);
        text-align: center;
    }
    .verdict-text {
        font-size: 1rem;
        color: #CBD5E1;
        margin-top: 0.5rem;
    }
    .pillar-header {
        background: rgba(0,201,167,0.08);
        border-left: 3px solid #00C9A7;
        padding: 0.6rem 1rem;
        border-radius: 0 6px 6px 0;
        color: #FFFFFF;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .standard-tag {
        font-size: 0.72rem;
        background: rgba(139,163,188,0.12);
        color: #8BA3BC;
        padding: 0.15rem 0.5rem;
        border-radius: 4px;
        margin-left: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)


# ── SIDEBAR ──────────────────────────────────
with st.sidebar:
    st.markdown("## IncluScore AI")
    st.markdown("<p style='color:#8BA3BC; font-size:0.82rem;'>Digital Inclusion Scorecard for EdTech</p>", unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio(
        "Navigation",
        ["Home", "Survey Evaluator", "CSV Upload", "Dashboard", "Framework Guide"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown("""
    <p style='color:#64748B; font-size:0.78rem;'>
    Framework standards:<br>
    WCAG 2.1 AA · UDL (CAST)<br>
    UNICEF CRC · COPPA · GDPR-K<br>
    UNESCO AI Ethics 2021<br>
    EU AI Act 2024 · SDG 4
    </p>
    """, unsafe_allow_html=True)
    st.markdown("""
    <p style='color:#64748B; font-size:0.78rem; margin-top:1rem;'>
    Built by <strong style='color:#8BA3BC'>Josiah Ryan Ofosuhene</strong><br>
    <a href='https://incluscoreai.netlify.app' style='color:#00C9A7;'>incluscoreai.netlify.app</a>
    </p>
    """, unsafe_allow_html=True)


# ════════════════════════════════════════════
# PAGE: HOME
# ════════════════════════════════════════════
if page == "Home":
    st.markdown("# IncluScore AI")
    st.markdown("<p style='color:#8BA3BC; font-size:1.1rem;'>Does this EdTech tool truly <strong style='color:#00C9A7;'>include</strong> every child?</p>", unsafe_allow_html=True)
    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Core Pillars", "3", "Accessibility · Safety · Equity")
    col2.metric("Scoring Criteria", "23", "Mapped to international standards")
    col3.metric("Score Range", "0 – 100", "Transparent composite score")
    col4.metric("SDG Alignment", "SDG 4", "Quality Education for all")

    st.markdown("---")
    st.markdown("## What is IncluScore AI?")
    st.markdown("""
    <p style='color:#8BA3BC; font-size:1rem; max-width:700px;'>
    IncluScore AI is a Digital Inclusion Scorecard that evaluates EdTech platforms for
    <strong style='color:#FFFFFF;'>accessibility, child safety, and equity</strong> — giving schools,
    policymakers, and child-rights advocates a transparent, defensible way to evaluate whether a
    digital learning tool truly serves every child.
    </p>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Accessibility")
        st.markdown("<p style='color:#8BA3BC; font-size:0.9rem;'>9 criteria mapped to WCAG 2.1 AA — screen readers, keyboard navigation, contrast ratios, captions, and more.</p>", unsafe_allow_html=True)
    with col2:
        st.markdown("### Child Safety")
        st.markdown("<p style='color:#8BA3BC; font-size:0.9rem;'>7 criteria covering COPPA, GDPR-K, UNICEF Digital Rights, and EU AI Act (2024) obligations for educational AI.</p>", unsafe_allow_html=True)
    with col3:
        st.markdown("### Equity & Inclusion")
        st.markdown("<p style='color:#8BA3BC; font-size:0.9rem;'>7 criteria based on UDL principles and SDG 4 — low-bandwidth support, multilingual access, and affordability.</p>", unsafe_allow_html=True)

    st.markdown("---")
    st.info("Use the sidebar to evaluate a platform with the **Survey Evaluator** or **CSV Upload**.")


# ════════════════════════════════════════════
# PAGE: SURVEY EVALUATOR
# ════════════════════════════════════════════
elif page == "Survey Evaluator":
    st.markdown("# Survey Evaluator")
    st.markdown("<p style='color:#8BA3BC;'>Score all 23 criteria across three pillars. Each input is on a 0–10 scale.</p>", unsafe_allow_html=True)
    st.markdown("---")

    platform_name = st.text_input("Platform name (optional)", placeholder="e.g. Khan Academy, Google Classroom...")

    # ── PILLAR 1: ACCESSIBILITY ──
    st.markdown("<div class='pillar-header'>Pillar 1 — Accessibility <span style='color:#8BA3BC; font-weight:400; font-size:0.85rem;'>(weight: 40%)</span></div>", unsafe_allow_html=True)
    with st.expander("WCAG 2.1 Criteria — click to expand", expanded=True):
        a_col1, a_col2, a_col3 = st.columns(3)
        with a_col1:
            text_alternatives = st.slider("Text Alternatives (WCAG 1.1.1)", 0, 10, 5, help="Non-text content has alt text, captions, or descriptions")
            captions_audio    = st.slider("Captions & Audio (WCAG 1.2.2)", 0, 10, 5, help="Captions provided for all audio and video content")
            color_contrast    = st.slider("Colour Contrast (WCAG 1.4.3)", 0, 10, 5, help="Text has at least 4.5:1 contrast ratio")
        with a_col2:
            resize_text          = st.slider("Text Resize (WCAG 1.4.4)", 0, 10, 5, help="Text resizable to 200% without loss of content")
            keyboard_navigation  = st.slider("Keyboard Navigation (WCAG 2.1.1)", 0, 10, 5, help="All functions accessible via keyboard alone")
            no_seizure_content   = st.slider("No Seizure Content (WCAG 2.3.1)", 0, 10, 5, help="No content flashes more than 3 times per second")
        with a_col3:
            readable_language    = st.slider("Readable Language (WCAG 3.1.1)", 0, 10, 5, help="Page language is programmatically identified")
            error_identification = st.slider("Error Identification (WCAG 3.3.1)", 0, 10, 5, help="Input errors are clearly identified and described")
            screen_reader_compat = st.slider("Screen Reader Compat (WCAG 4.1.2)", 0, 10, 5, help="Compatible with NVDA, JAWS, VoiceOver")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── PILLAR 2: CHILD SAFETY ──
    st.markdown("<div class='pillar-header'>Pillar 2 — Child Safety <span style='color:#8BA3BC; font-weight:400; font-size:0.85rem;'>(weight: 35%)</span></div>", unsafe_allow_html=True)
    with st.expander("COPPA / GDPR-K / UNICEF Criteria — click to expand", expanded=True):
        s_col1, s_col2 = st.columns(2)
        with s_col1:
            data_minimization  = st.slider("Data Minimization (GDPR-K / COPPA)", 0, 10, 5, help="Only collects data strictly necessary for education")
            parental_consent   = st.slider("Parental Consent (COPPA Art.5)", 0, 10, 5, help="Verifiable parental consent before collecting child data")
            data_encryption    = st.slider("Data Encryption (GDPR Art.32)", 0, 10, 5, help="All stored and transmitted child data is encrypted")
            content_moderation = st.slider("Content Moderation (UNICEF CRC Art.17)", 0, 10, 5, help="Effective moderation preventing harmful material")
        with s_col2:
            age_appropriateness = st.slider("Age Appropriateness (UNICEF Digital Rights)", 0, 10, 5, help="Content and interface appropriate for target age group")
            no_dark_patterns    = st.slider("No Dark Patterns (EU AI Act Art.5)", 0, 10, 5, help="No manipulative design exploiting child vulnerabilities")
            safe_communication  = st.slider("Safe Communication (UNICEF CRC Art.19)", 0, 10, 5, help="No unsupervised messaging between unknown users")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── PILLAR 3: EQUITY ──
    st.markdown("<div class='pillar-header'>Pillar 3 — Equity & Inclusion <span style='color:#8BA3BC; font-weight:400; font-size:0.85rem;'>(weight: 25%)</span></div>", unsafe_allow_html=True)
    with st.expander("UDL / SDG 4 Criteria — click to expand", expanded=True):
        e_col1, e_col2 = st.columns(2)
        with e_col1:
            multiple_formats = st.slider("Multiple Formats (UDL Guideline 1)", 0, 10, 5, help="Content in text, audio, visual, and video formats")
            language_support = st.slider("Language Support (UDL Guideline 2)", 0, 10, 5, help="Supports learners' home language or multilingual interface")
            flexible_input   = st.slider("Flexible Input (UDL Guideline 4)", 0, 10, 5, help="Accepts voice, touch, keyboard, drawing inputs")
            learner_autonomy = st.slider("Learner Autonomy (UDL Guideline 7)", 0, 10, 5, help="Learners can set goals and work at own pace")
        with e_col2:
            low_bandwidth  = st.slider("Low-Bandwidth Support (SDG 4 / ITU)", 0, 10, 5, help="Functions on slow or intermittent internet connections")
            device_agnostic = st.slider("Device Agnostic (SDG 4)", 0, 10, 5, help="Works on low-cost devices and older browsers")
            affordability  = st.slider("Affordability (SDG 4.1)", 0, 10, 5, help="Free tier or affordable pricing for low-income schools")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── CALCULATE ──
    if st.button("Calculate IncluScore", type="primary", use_container_width=True):
        result = calculate_survey_score(
            text_alternatives=text_alternatives,
            captions_audio=captions_audio,
            color_contrast=color_contrast,
            resize_text=resize_text,
            keyboard_navigation=keyboard_navigation,
            no_seizure_content=no_seizure_content,
            readable_language=readable_language,
            error_identification=error_identification,
            screen_reader_compat=screen_reader_compat,
            data_minimization=data_minimization,
            parental_consent=parental_consent,
            data_encryption=data_encryption,
            content_moderation=content_moderation,
            age_appropriateness=age_appropriateness,
            no_dark_patterns=no_dark_patterns,
            safe_communication=safe_communication,
            multiple_formats=multiple_formats,
            language_support=language_support,
            flexible_input=flexible_input,
            learner_autonomy=learner_autonomy,
            low_bandwidth=low_bandwidth,
            device_agnostic=device_agnostic,
            affordability=affordability,
        )

        st.session_state["last_result"] = result
        st.session_state["last_platform"] = platform_name or "Evaluated Platform"

        st.markdown("---")
        st.markdown("## Results")

        # Score display
        score = result["composite_score"]
        verdict = result["verdict"]

        r_col1, r_col2 = st.columns([1, 2])
        with r_col1:
            st.markdown(f"""
            <div style='text-align:center; padding:2rem;'>
                <div class='score-badge'>{score}</div>
                <div class='verdict-text'>{verdict}</div>
                <div style='color:#64748B; font-size:0.8rem; margin-top:0.5rem;'>out of 100</div>
            </div>
            """, unsafe_allow_html=True)
        with r_col2:
            ps = result["pillar_scores"]
            pillar_df = pd.DataFrame({
                "Pillar": ["Accessibility", "Child Safety", "Equity & Inclusion"],
                "Score":  [ps["accessibility"], ps["child_safety"], ps["equity"]],
                "Weight": ["40%", "35%", "25%"],
            })
            chart = alt.Chart(pillar_df).mark_bar(cornerRadiusTopRight=4, cornerRadiusBottomRight=4).encode(
                x=alt.X("Score:Q", scale=alt.Scale(domain=[0, 100]), title="Score (0–100)"),
                y=alt.Y("Pillar:N", sort=None, title=""),
                color=alt.condition(
                    alt.datum.Score >= 70,
                    alt.value("#00C9A7"),
                    alt.condition(alt.datum.Score >= 50, alt.value("#F4C542"), alt.value("#E53E3E"))
                ),
                tooltip=["Pillar", "Score", "Weight"],
            ).properties(height=140).configure_view(
                strokeOpacity=0
            ).configure_axis(
                labelColor="#8BA3BC", gridColor="#1E2D40", domainColor="#1E2D40"
            ).configure_background(color="#0D1B2A")
            st.altair_chart(chart, use_container_width=True)

        # Pillar detail
        st.markdown("### Pillar Breakdown")
        p_col1, p_col2, p_col3 = st.columns(3)
        p_col1.metric("Accessibility", f"{ps['accessibility']:.1f}/100", help="Weight: 40%")
        p_col2.metric("Child Safety",  f"{ps['child_safety']:.1f}/100",  help="Weight: 35%")
        p_col3.metric("Equity",        f"{ps['equity']:.1f}/100",        help="Weight: 25%")

        # Flags
        flags = []
        detail = result["detail"]
        for key, val in detail["child_safety"].items():
            if val <= 3:
                flags.append(f"**Child Safety — {key.replace('_',' ').title()}** scored {val}/10. Immediate review recommended.")
        for key, val in detail["accessibility"].items():
            if val <= 3:
                flags.append(f"**Accessibility — {key.replace('_',' ').title()}** scored {val}/10. May exclude students with disabilities.")
        for key, val in detail["equity"].items():
            if val <= 3:
                flags.append(f"**Equity — {key.replace('_',' ').title()}** scored {val}/10. May exclude low-resource learners.")

        if flags:
            st.markdown("### Flagged Issues")
            for f in flags:
                st.warning(f)
        else:
            st.success("No critical flags raised across all 23 criteria.")


# ════════════════════════════════════════════
# PAGE: CSV UPLOAD
# ════════════════════════════════════════════
elif page == "CSV Upload":
    st.markdown("# CSV Upload")
    st.markdown("<p style='color:#8BA3BC;'>Upload a CSV to score multiple platforms at once.</p>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("### CSV Format")
    tab1, tab2 = st.tabs(["Full Format (23 columns)", "Simple Format (3 columns)"])
    with tab1:
        st.markdown("<p style='color:#8BA3BC; font-size:0.88rem;'>Use all 23 criterion columns for full weighted scoring. Download the sample below.</p>", unsafe_allow_html=True)
        sample_cols = (
            ["Platform"] +
            ["text_alternatives","captions_audio","color_contrast","resize_text",
             "keyboard_navigation","no_seizure_content","readable_language",
             "error_identification","screen_reader_compat"] +
            ["data_minimization","parental_consent","data_encryption",
             "content_moderation","age_appropriateness","no_dark_patterns","safe_communication"] +
            ["multiple_formats","language_support","flexible_input",
             "learner_autonomy","low_bandwidth","device_agnostic","affordability"]
        )
        sample_full = pd.DataFrame([
            ["Platform A"] + [7,6,8,7,5,9,8,6,5] + [4,3,6,5,7,6,4] + [6,4,5,6,3,4,5],
            ["Platform B"] + [9,8,9,8,9,9,9,8,9] + [9,9,8,9,9,9,8] + [8,7,8,7,8,8,9],
            ["Platform C"] + [4,3,5,4,2,7,6,3,2] + [3,2,4,3,5,4,3] + [5,3,4,5,2,3,4],
        ], columns=sample_cols)
        st.dataframe(sample_full, use_container_width=True)
        csv_full = sample_full.to_csv(index=False).encode("utf-8")
        st.download_button("Download Full Sample CSV", csv_full, "sample_data_full.csv", "text/csv")
    with tab2:
        st.markdown("<p style='color:#8BA3BC; font-size:0.88rem;'>Simplified 3-column format. Uses average scoring per pillar.</p>", unsafe_allow_html=True)
        sample_simple = pd.DataFrame([
            {"Platform": "Platform A", "Accessibility": 7, "Safety": 5, "Equity": 4},
            {"Platform": "Platform B", "Accessibility": 9, "Safety": 9, "Equity": 8},
            {"Platform": "Platform C", "Accessibility": 4, "Safety": 3, "Equity": 3},
        ])
        st.dataframe(sample_simple, use_container_width=True)
        csv_simple = sample_simple.to_csv(index=False).encode("utf-8")
        st.download_button("Download Simple Sample CSV", csv_simple, "sample_data_simple.csv", "text/csv")

    st.markdown("---")
    uploaded = st.file_uploader("Upload your CSV", type="csv")

    if uploaded:
        try:
            df = pd.read_csv(uploaded)
            st.markdown("### Raw Data")
            st.dataframe(df, use_container_width=True)

            scored_df = calculate_csv_scores(df)
            st.session_state["scored_df"] = scored_df

            st.markdown("### Scored Results")
            display_cols = [c for c in ["Platform", "InkluScore", "Verdict",
                                        "Accessibility_Score", "ChildSafety_Score", "Equity_Score"]
                           if c in scored_df.columns]
            st.dataframe(scored_df[display_cols], use_container_width=True)

            csv_out = scored_df.to_csv(index=False).encode("utf-8")
            st.download_button("Download Results CSV", csv_out, "IncluScore_results.csv", "text/csv")

            st.info("Go to the **Dashboard** tab to visualize these results.")

        except Exception as e:
            st.error(f"Error: {e}")


# ════════════════════════════════════════════
# PAGE: DASHBOARD
# ════════════════════════════════════════════
elif page == "Dashboard":
    st.markdown("# Dashboard")
    st.markdown("---")

    if "scored_df" in st.session_state:
        df = st.session_state["scored_df"]

        # Summary metrics
        avg = df["IncluScore"].mean()
        top = df["IncluScore"].max()
        bot = df["IncluScore"].min()

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Platforms Evaluated", len(df))
        m2.metric("Average IncluScore", f"{avg:.1f}")
        m3.metric("Highest Score", f"{top:.1f}")
        m4.metric("Lowest Score", f"{bot:.1f}")

        st.markdown("---")

        # Score distribution
        st.markdown("### Score Distribution")
        hist = alt.Chart(df).mark_bar(color="#00C9A7", opacity=0.8).encode(
            x=alt.X("InkluScore:Q", bin=alt.Bin(maxbins=10), title="InkluScore"),
            y=alt.Y("count()", title="Number of Platforms"),
            tooltip=["count()"]
        ).configure_axis(
            labelColor="#8BA3BC", gridColor="#1E2D40"
        ).configure_background(color="#0D1B2A").configure_view(strokeOpacity=0)
        st.altair_chart(hist, use_container_width=True)

        # Pillar comparison (if pillar scores exist)
        if all(c in df.columns for c in ["Accessibility_Score", "ChildSafety_Score", "Equity_Score"]):
            st.markdown("### Pillar Comparison")
            name_col = "Platform" if "Platform" in df.columns else df.columns[0]
            melt_df = df[[name_col, "Accessibility_Score", "ChildSafety_Score", "Equity_Score"]].melt(
                id_vars=name_col, var_name="Pillar", value_name="Score"
            )
            melt_df["Pillar"] = melt_df["Pillar"].str.replace("_Score", "").str.replace("ChildSafety", "Child Safety")
            bar = alt.Chart(melt_df).mark_bar().encode(
                x=alt.X(f"{name_col}:N", title=""),
                y=alt.Y("Score:Q", scale=alt.Scale(domain=[0, 100])),
                color=alt.Color("Pillar:N", scale=alt.Scale(
                    domain=["Accessibility", "Child Safety", "Equity"],
                    range=["#00C9A7", "#F4C542", "#63B3ED"]
                )),
                xOffset="Pillar:N",
                tooltip=[name_col, "Pillar", "Score"]
            ).configure_axis(
                labelColor="#8BA3BC", gridColor="#1E2D40"
            ).configure_background(color="#0D1B2A").configure_view(strokeOpacity=0)
            st.altair_chart(bar, use_container_width=True)

        # Full table
        st.markdown("### Full Results Table")
        st.dataframe(df, use_container_width=True)

    elif "last_result" in st.session_state:
        result = st.session_state["last_result"]
        name   = st.session_state.get("last_platform", "Platform")
        ps     = result["pillar_scores"]

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Platform", name)
        m2.metric("IncluScore", f"{result['composite_score']:.1f}")
        m3.metric("Verdict", result["verdict"].split(" — ")[0])
        m4.metric("Criteria Evaluated", "23")

        st.markdown("### Pillar Scores")
        pillar_df = pd.DataFrame({
            "Pillar": ["Accessibility", "Child Safety", "Equity"],
            "Score": [ps["accessibility"], ps["child_safety"], ps["equity"]],
        })
        bar = alt.Chart(pillar_df).mark_bar(cornerRadiusTopRight=4, cornerRadiusBottomRight=4).encode(
            x=alt.X("Score:Q", scale=alt.Scale(domain=[0, 100])),
            y=alt.Y("Pillar:N", sort=None),
            color=alt.condition(
                alt.datum.Score >= 70, alt.value("#00C9A7"),
                alt.condition(alt.datum.Score >= 50, alt.value("#F4C542"), alt.value("#E53E3E"))
            ),
            tooltip=["Pillar", "Score"]
        ).properties(height=120).configure_axis(
            labelColor="#8BA3BC", gridColor="#1E2D40"
        ).configure_background(color="#0D1B2A").configure_view(strokeOpacity=0)
        st.altair_chart(bar, use_container_width=True)
    else:
        st.info("No data yet. Run the **Survey Evaluator** or **CSV Upload** first.")


# ════════════════════════════════════════════
# PAGE: FRAMEWORK GUIDE
# ════════════════════════════════════════════
elif page == "Framework Guide":
    st.markdown("# Framework Guide")
    st.markdown("<p style='color:#8BA3BC;'>The IncluScore AI evaluation framework — every criterion, standard, and weight.</p>", unsafe_allow_html=True)
    st.markdown("---")

    for pillar_key, criteria in ALL_CRITERIA.items():
        weight_pct = int(PILLAR_WEIGHTS[pillar_key] * 100)
        icons = {"accessibility": "", "child_safety": "", "equity": ""}
        st.markdown(f"### {icons[pillar_key]} {pillar_key.replace('_', ' ').title()} — {weight_pct}% of final score")

        rows = []
        for key, meta in criteria.items():
            rows.append({
                "Criterion": key.replace("_", " ").title(),
                "Standard": meta["standard"],
                "Description": meta["description"],
                "Weight": f"{int(meta['weight'] * 100)}%",
            })
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
        st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Global Standards Referenced")
    standards = [
        ("WCAG 2.1 AA", "Web Content Accessibility Guidelines", "W3C", "web.dev/accessibility"),
        ("UDL Guidelines", "Universal Design for Learning", "CAST", "udlguidelines.cast.org"),
        ("UNESCO AI Ethics 2021", "Recommendation on the Ethics of AI", "UNESCO", "unesdoc.unesco.org"),
        ("EU AI Act (2024)", "High-Risk AI in Education provisions", "European Union", "artificial-intelligence-act.com"),
        ("UNICEF CRC", "Convention on the Rights of the Child", "UNICEF", "unicef.org"),
        ("COPPA", "Children's Online Privacy Protection Act", "FTC (USA)", "ftc.gov/coppa"),
        ("GDPR-K", "GDPR provisions for children's data", "EU / ICO", "ico.org.uk"),
        ("SDG 4", "Sustainable Development Goal 4 — Quality Education", "UN", "sdgs.un.org"),
    ]
    st.dataframe(pd.DataFrame(standards, columns=["Standard", "Full Name", "Body", "Reference"]),
                 use_container_width=True, hide_index=True)


# ── FOOTER ───────────────────────────────────
st.markdown("---")
st.markdown("""
<p style='color:#64748B; font-size:0.8rem; text-align:center;'>
IncluScore AI · Built by <strong style='color:#8BA3BC;'>Josiah Ryan Ofosuhene</strong> ·
<a href='https://incluscoreai.netlify.app' style='color:#00C9A7;'>incluscoreai.netlify.app</a> ·
<a href='https://github.com/JoshRyanJ/Incluscore-Prototype' style='color:#00C9A7;'>GitHub</a>
</p>
""", unsafe_allow_html=True)
