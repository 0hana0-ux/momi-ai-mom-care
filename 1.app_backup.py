import streamlit as st


# ==========================================
# 1. PAGE SETTING
# ==========================================

st.set_page_config(
    page_title="MOMI",
    page_icon="🌷",
    layout="centered"
)


# ==========================================
# 2. DESIGN
# ==========================================

st.markdown("""
<style>

@import url(
    'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Playfair+Display:wght@500;600&display=swap'
);


/* 전체 배경 */

.stApp {
    background: linear-gradient(
        180deg,
        #fff8fc 0%,
        #f6eef9 100%
    );
}


/* 화면 위쪽 기본 여백 */

.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
    max-width: 600px;
}


/* 기본 메뉴 숨기기 */

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* ==========================================
   MOMI LOGO
========================================== */

.logo {
    font-family: 'Playfair Display', serif;
    text-align: center;
    font-size: 24px;
    letter-spacing: 3px;
    color: #8d6fa0;
    margin-top: 10px;
}


/* ==========================================
   40 WEEK ADVENTURE
========================================== */

.adventure {
    font-family: 'Playfair Display', serif;
    text-align: center;
    font-size: 42px;
    line-height: 1.1;
    color: #5b4962;
    margin-top: 12px;
}


/* ==========================================
   DESCRIPTION
========================================== */

.description {
    text-align: center;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    color: #9b8fa0;
    margin-top: 12px;
    margin-bottom: 25px;
    line-height: 1.7;
}


/* ==========================================
   IMAGE
========================================== */

.stImage {
    border-radius: 28px;
}


/* ==========================================
   INPUT
========================================== */

.stTextInput label,
.stNumberInput label,
.stDateInput label {
    font-family: 'DM Sans', sans-serif !important;
    color: #76677d !important;
    font-size: 13px !important;
}


.stTextInput input,
.stNumberInput input,
.stDateInput input {
    border-radius: 14px !important;
    border: 1px solid #e5d9e7 !important;
    background-color: white !important;
}


/* ==========================================
   START BUTTON
========================================== */

.stButton > button {
    width: 100%;
    height: 54px;
    margin-top: 15px;

    border: none;
    border-radius: 16px;

    background: linear-gradient(
        135deg,
        #d0a9df,
        #b8a3d8
    );

    color: white;

    font-family: 'DM Sans', sans-serif;

    font-size: 15px;
    font-weight: 600;

    letter-spacing: 0.5px;
}


.stButton > button:hover {
    transform: translateY(-2px);
}


/* ==========================================
   BOTTOM TEXT
========================================== */

.bottom-text {
    text-align: center;

    font-family: 'DM Sans', sans-serif;

    font-size: 11px;

    color: #aaa0ad;

    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 3. MOMI LOGO
# ==========================================

st.markdown(
    '<div class="logo">🌷 MOMI</div>',
    unsafe_allow_html=True
)


# ==========================================
# 4. MAIN TITLE
# ==========================================

st.markdown(
    '<div class="adventure">'
    '40 WEEK<br>'
    'ADVENTURE'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================
# 5. INTRODUCTION
# ==========================================

st.markdown(
    '<div class="description">'
    'Your little journey begins here.'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================
# 6. PREGNANT MOM IMAGE
# ==========================================

st.image(
    "assets/pregnant_mom.png",
    width="stretch"
)


# ==========================================
# 7. MESSAGE
# ==========================================

st.markdown(
    '<div class="description">'
    'A little journey, a new little life. 🌷'
    '<br>'
    'Growing together, one week at a time.'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================
# 8. PROFILE INPUT
# ==========================================

mom_name = st.text_input(
    "Mom Name",
    placeholder="Your name"
)


baby_name = st.text_input(
    "Baby Name",
    placeholder="Your baby's name"
)


# 임신 주수와 출산 예정일

col1, col2 = st.columns(2)


with col1:

    pregnancy_week = st.number_input(
        "Pregnancy Week",
        min_value=1,
        max_value=40,
        value=18
    )


with col2:

    due_date = st.date_input(
        "Due Date"
    )


# ==========================================
# 9. START BUTTON
# ==========================================

if st.button("START YOUR JOURNEY  →"):

    st.session_state["mom_name"] = mom_name

    st.session_state["baby_name"] = baby_name

    st.session_state["pregnancy_week"] = pregnancy_week

    st.session_state["due_date"] = due_date

    st.success(
        f"Welcome, {mom_name}! 🌷"
    )


# ==========================================
# 10. BOTTOM MESSAGE
# ==========================================

st.markdown(
    '<div class="bottom-text">'
    '✦ MOMI will be with you through all 40 weeks ✦'
    '</div>',
    unsafe_allow_html=True
)