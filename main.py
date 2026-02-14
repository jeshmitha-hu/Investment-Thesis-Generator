import streamlit as st

st.set_page_config(
    page_title="Investment Thesis Generator",
    layout="wide"
)

st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(180deg, #050c12 0%, #08141b 50%, #0d1f2a 100%);
    color: white;
}

/* MAIN TITLE */
.main-title {
    text-align: center;
    font-size: 90px;
    font-weight: 1000;
    color: white;
    text-shadow: 0 0 40px #00F5FF, 0 0 80px #00F5FF;
    margin-bottom: 30px;
}

/* SUB TITLE */
.sub-title {
    text-align: center;
    font-size: 42px;
    font-weight: 1000;
    color: #00F5FF;
    margin-bottom: 70px;
}

/*FORCE ALL WIDGET LABEL TEXT */
div[data-testid="stMarkdownContainer"] p {
    font-size: 42px !important;
    font-weight: 1000 !important;
    color: #00F5FF !important;
    opacity: 1 !important;
    text-shadow: 0 0 15px #00F5FF, 0 0 30px #00F5FF;
}

/* INPUT TEXT BIGGER */
input, textarea, select {
    font-size: 26px !important;
    font-weight: 900 !important;
}

/* BUTTON */
.stButton>button {
    background: linear-gradient(90deg, #00F5FF, #00FF9C);
    color: black;
    font-weight: 1000;
    border-radius: 16px;
    height: 85px;
    width: 100%;
    font-size: 30px;
    box-shadow: 0 0 30px #00F5FF, 0 0 60px #00FF9C;
}

/* Selected value (closed dropdown box) */
div[data-baseweb="select"] span {
    font-weight: 900 !important;
    font-size: 24px !important;
    color: #ffffff !important;
}

/* Dropdown popup menu container */
div[role="listbox"] {
    font-weight: 900 !important;
}

/* Each option inside dropdown */
div[role="option"] {
    font-weight: 900 !important;
    font-size: 22px !important;
    color: #111111 !important;
}

/* Hover effect (clean, no neon) */
div[role="option"]:hover {
    background-color: #e6f7f7 !important;
    font-weight: 1000 !important;
}


/* ---------------- NEON GLASS REPORT CARD ---------------- */

.glass-card {
    background: rgba(0, 20, 30, 0.85);
    backdrop-filter: blur(18px);
    padding: 70px;
    border-radius: 22px;
    margin-top: 60px;
    border: 1px solid rgba(0,255,255,0.4);
    box-shadow:
        0 0 40px rgba(0,255,255,0.6),
        0 0 80px rgba(0,255,255,0.3);
}

/* REPORT TITLE */
.report-title {
    font-size: 60px;
    font-weight: 1000;
    text-align: center;
    color: #00F5FF;
    margin-bottom: 50px;
    text-shadow:
        0 0 15px #00F5FF,
        0 0 40px #00F5FF,
        0 0 80px #00F5FF;
}

/* SECTION HEADINGS */
.report-heading {
    font-size: 38px;
    font-weight: 1000;
    color: #00F5FF;
    margin-top: 35px;
    margin-bottom: 15px;
    text-shadow:
        0 0 10px #00F5FF,
        0 0 25px #00F5FF;
}

/* BODY TEXT */
.report-text {
    font-size: 26px;
    font-weight: 800;
    line-height: 1.9;
    color: #ffffff;
}

/* RISK BOX */
.risk-box {
    margin-top: 30px;
    padding: 25px;
    border-radius: 14px;
    font-size: 28px;
    font-weight: 1000;
    text-align: center;
    box-shadow:
        0 0 25px currentColor,
        0 0 50px currentColor;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>Automated Thesis Generator</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>AI-Powered Startup Evaluation</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    startup_name = st.text_input("Startup Name")
    industry = st.selectbox("Industry",
        ["FinTech", "HealthTech", "EdTech", "AI", "Engineering", "E-commerce", "SaaS", "Other"])
    revenue = st.number_input("Annual Revenue (USD)", min_value=0.0, format="%.2f")
    market_size = st.number_input("Market Size (USD)", min_value=0.0, format="%.2f")

with col2:
    growth_rate = st.slider("Market Growth Rate (%)", 0, 100, 15)
    stage = st.selectbox("Startup Stage",
        ["Pre-Seed", "Seed", "Series A", "Series B", "Growth Stage"])
    advantage = st.text_area("Competitive Advantage")
    problem = st.text_area("Problem Being Solved")

st.markdown("<br><br>", unsafe_allow_html=True)

def calculate_score(revenue, market_size, growth_rate, stage):
    score = 0
    
    # Revenue weight
    if revenue > 5_000_000:
        score += 3
    elif revenue > 1_000_000:
        score += 2
    elif revenue > 100_000:
        score += 1

    # Market size weight
    if market_size > 5_000_000_000:
        score += 3
    elif market_size > 1_000_000_000:
        score += 2
    elif market_size > 500_000_000:
        score += 1

    # Growth weight
    if growth_rate > 30:
        score += 2
    elif growth_rate > 15:
        score += 1

    # Stage maturity
    if stage in ["Series B", "Growth Stage"]:
        score += 2
    elif stage == "Series A":
        score += 1

    return score

generate = st.button("Generate Investment Thesis")

if generate:

    score = calculate_score(revenue, market_size, growth_rate, stage)

    if score >= 6:
        risk_color = "#00FF9C"
        risk_text = "LOW RISK"
    elif score >= 3:
        risk_color = "#FFD700"
        risk_text = "MODERATE RISK"
    else:
        risk_color = "#FF3B3B"
        risk_text = "HIGH RISK"

    st.markdown(
        f"Considering its current {stage} maturity and risk-adjusted score of {score}/10..."
    )

    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<div class='report-title'>📄 Investment Thesis Report</div>", unsafe_allow_html=True)

    st.markdown("<div class='report-heading'>1️⃣ Market Opportunity</div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='report-text'>The {industry} industry is experiencing an annual growth rate of {growth_rate}%. "
        f"This growth trajectory signals expanding demand and strong future market potential. "
        f"With continued innovation and scalability opportunities, the sector presents attractive conditions for capital deployment.</div>",
        unsafe_allow_html=True
    )

    st.markdown("<div class='report-heading'>2️⃣ Problem & Strategic Positioning</div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='report-text'><b>{startup_name}</b> addresses the following core challenge: {problem}. "
        f"The company differentiates itself through {advantage}, establishing competitive defensibility and long-term positioning within the market.</div>",
        unsafe_allow_html=True
    )

    st.markdown("<div class='report-heading'>3️⃣ Financial Strength & Traction</div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='report-text'>The company reports annual revenue of ${revenue:,.0f}. "
        f"This revenue performance indicates measurable traction and operational validation of the business model.</div>",
        unsafe_allow_html=True
    )

    st.markdown("<div class='report-heading'>4️⃣ Startup Stage & Risk Profile</div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='report-text'>Currently operating at the <b>{stage}</b> stage, "
        f"the company exhibits characteristics typical of this maturity level, including scaling potential and associated execution risks.</div>",
        unsafe_allow_html=True
    )

    st.markdown("<div class='report-heading'>5️⃣ Investment Risk Assessment</div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='report-text'>Overall Investment Score: {score}/10</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='risk-box' style='background:{risk_color}; color:black;'>{risk_text}</div>",
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)