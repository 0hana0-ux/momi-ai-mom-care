import streamlit as st
import streamlit.components.v1 as components
from datetime import date


# ==========================================
# 기본 설정
# ==========================================

st.set_page_config(
    page_title="MOMI",
    page_icon="✦",
    layout="centered"
)


# ==========================================
# Session State
# ==========================================

if "page" not in st.session_state:
    st.session_state.page = "signup"

if "mom_name" not in st.session_state:
    st.session_state.mom_name = ""

if "baby_name" not in st.session_state:
    st.session_state.baby_name = ""

if "pregnancy_week" not in st.session_state:
    st.session_state.pregnancy_week = 18

if "due_date" not in st.session_state:
    st.session_state.due_date = date(2027, 1, 20)

# 추가된 부분
if "selected_week" not in st.session_state:
    st.session_state.selected_week = 18


# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;500;600;700;800&family=Fredoka:wght@400;500;600;700&display=swap');


/* 전체 */

.stApp {

    background:
        radial-gradient(
            circle at 10% 10%,
            #FFE5F0 0%,
            transparent 25%
        ),

        radial-gradient(
            circle at 90% 20%,
            #E8DFFF 0%,
            transparent 25%
        ),

        radial-gradient(
            circle at 20% 90%,
            #DFF7F0 0%,
            transparent 25%
        ),

        linear-gradient(
            180deg,
            #FFF9FC 0%,
            #F9F3FC 100%
        );
}


/* 기본 글씨 */

* {

    font-family:
        'Baloo 2',
        sans-serif;

}


/* 전체 컨테이너 */

.block-container {

    max-width: 720px;

    padding-top: 35px;
    padding-bottom: 70px;

}


/* 제목 */

h1,
h2,
h3 {

    font-family:
        'Fredoka',
        sans-serif !important;

    color: #735579 !important;

    text-align: center;

}


/* 모든 일반 텍스트 가운데 */

.stMarkdown,
.stCaption {

    text-align: center;

}


/* ==========================================
   MOMI TITLE
   ========================================== */

.logo {

    text-align: center;

    font-family:
        'Fredoka',
        sans-serif;

    font-size: 24px;

    font-weight: 700;

    letter-spacing: 3px;

    color: #B87FA8;

    margin-bottom: 0;

}


.subtitle {

    text-align: center;

    font-size: 14px;

    font-weight: 600;

    letter-spacing: 2px;

    color: #A98DAE;

}


/* ==========================================
   입력창
   ========================================== */

.stTextInput,
.stNumberInput,
.stDateInput {

    text-align: center;

}


.stTextInput label,
.stNumberInput label,
.stDateInput label {

    text-align: center !important;

    width: 100%;

    font-family:
        'Fredoka',
        sans-serif !important;

    color: #85678C !important;

    font-size: 15px !important;

}


.stTextInput input,
.stNumberInput input,
.stDateInput input {

    border-radius: 18px !important;

    border:
        3px solid #E8D4E7 !important;

    background:
        rgba(255,255,255,0.9) !important;

    text-align: center !important;

    font-family:
        'Baloo 2',
        sans-serif !important;

    font-size: 16px !important;

}


/* ==========================================
   버튼
   ========================================== */

.stButton {

    text-align: center;

}


.stButton > button {

    width: 100%;

    border: none;

    border-radius: 22px;

    padding: 16px;

    font-family:
        'Fredoka',
        sans-serif !important;

    font-size: 18px;

    font-weight: 600;

    letter-spacing: 1px;

    color: white;

    background:
        linear-gradient(
            135deg,
            #F29AC2,
            #C5A5E8
        );

    box-shadow:
        0 8px 20px
        rgba(190,140,200,0.25);

}


.stButton > button:hover {

    transform: translateY(-2px);

    color: white;

}


/* ==========================================
   카드
   ========================================== */

div[data-testid="stVerticalBlockBorderWrapper"] {

    background:
        rgba(255,255,255,0.78);

    border:

        4px solid
        #E3CBE4 !important;

    border-radius:

        25px !important;

    box-shadow:

        0 8px 20px
        rgba(130,90,140,0.08);

    padding:

        8px;

}


/* ==========================================
   카드 안 글씨
   ========================================== */

div[data-testid="stVerticalBlockBorderWrapper"] p {

    text-align: center;

    color: #735F76;

    font-size: 15px;

}


/* ==========================================
   Caption
   ========================================== */

.stCaption {

    color: #A88AAA !important;

    font-family:
        'Fredoka',
        sans-serif !important;

    font-weight: 500;

}


/* ==========================================
   Week
   ========================================== */

div[data-testid="stVerticalBlockBorderWrapper"]
h1 {

    font-size: 60px !important;

    color: #C47EAB !important;

    margin: 0;

}


/* ==========================================
   구분
   ========================================== */

hr {

    border:

        none;

    border-top:

        2px dashed
        #E6D4E7;

}


/* ==========================================
   작은 포인트
   ========================================== */

.stAlert {

    border-radius: 20px;

}


/* ==========================================
   WELCOME 5 MENU
   ========================================== */

div[data-testid="stHorizontalBlock"] .stButton > button {

    font-size: 14px !important;

    padding: 12px 4px !important;

    min-height: 65px;

    white-space: pre-line;

}


/* ==========================================
   모바일 느낌
   ========================================== */

@media (max-width: 700px) {

    .block-container {

        padding-left: 25px;
        padding-right: 25px;

    }

}

</style>
""", unsafe_allow_html=True)


# ==========================================
# MOMI 캐릭터
# ==========================================

def show_momi():

    momi_svg = """
    <!DOCTYPE html>

    <html>

    <head>

    <style>

    body {

        margin: 0;

        padding: 0;

        background: transparent;

        display: flex;

        justify-content: center;

        align-items: center;

    }

    </style>

    </head>

    <body>

    <svg
        width="280"
        height="280"
        viewBox="0 0 280 280"
        xmlns="http://www.w3.org/2000/svg"
    >

        <circle
            cx="140"
            cy="140"
            r="120"
            fill="#F8EFF9"
        />

        <text
            x="48"
            y="80"
            font-size="22"
            fill="#B9A4D8"
        >✦</text>

        <text
            x="205"
            y="92"
            font-size="18"
            fill="#E5A9C7"
        >✧</text>

        <text
            x="215"
            y="195"
            font-size="21"
            fill="#B9A4D8"
        >✦</text>

        <text
            x="50"
            y="198"
            font-size="16"
            fill="#E5A9C7"
        >✧</text>


        <line
            x1="140"
            y1="88"
            x2="140"
            y2="65"
            stroke="#B9A4D8"
            stroke-width="3"
            stroke-linecap="round"
        />

        <circle
            cx="140"
            cy="60"
            r="6"
            fill="#E5A9C7"
        />


        <circle
            cx="94"
            cy="105"
            r="25"
            fill="#E7D8EE"
        />

        <circle
            cx="186"
            cy="105"
            r="25"
            fill="#E7D8EE"
        />


        <circle
            cx="94"
            cy="105"
            r="13"
            fill="#F3CFE0"
        />

        <circle
            cx="186"
            cy="105"
            r="13"
            fill="#F3CFE0"
        />


        <ellipse
            cx="140"
            cy="168"
            rx="59"
            ry="69"
            fill="#E7D7EE"
        />


        <circle
            cx="140"
            cy="135"
            r="48"
            fill="#FFF8FB"
        />


        <circle
            cx="123"
            cy="132"
            r="5"
            fill="#69566B"
        />

        <circle
            cx="157"
            cy="132"
            r="5"
            fill="#69566B"
        />


        <ellipse
            cx="113"
            cy="151"
            rx="11"
            ry="6"
            fill="#F1BBD0"
        />

        <ellipse
            cx="167"
            cy="151"
            rx="11"
            ry="6"
            fill="#F1BBD0"
        />


        <path
            d="M130 151 Q140 160 150 151"
            stroke="#69566B"
            stroke-width="3"
            fill="none"
            stroke-linecap="round"
        />


        <text
            x="140"
            y="207"
            text-anchor="middle"
            font-size="27"
            fill="#D88EAF"
        >♡</text>

    </svg>

    </body>

    </html>
    """

    components.html(
        momi_svg,
        height=290,
        scrolling=False
    )


# ==========================================
# SIGN UP
# ==========================================

def show_signup():

    st.markdown(
        '<div class="logo">✦ MOMI ✦</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">MOM CARE AI</div>',
        unsafe_allow_html=True
    )


    st.markdown(
        "# 40 WEEK ADVENTURE"
    )


    st.caption(
        "Your gentle AI companion throughout pregnancy"
    )


    show_momi()


    mom_name = st.text_input(
        "Mom Name",
        value=st.session_state.mom_name,
        placeholder="Enter your name"
    )


    baby_name = st.text_input(
        "Baby Name",
        value=st.session_state.baby_name,
        placeholder="Enter your baby name"
    )


    pregnancy_week = st.number_input(
        "Pregnancy Week",
        min_value=1,
        max_value=40,
        value=st.session_state.pregnancy_week
    )


    due_date = st.date_input(
        "Due Date",
        value=st.session_state.due_date,
        min_value=date(2026, 1, 1),
        max_value=date(2030, 12, 31)
    )


    st.write("")


    if st.button("START ✦"):

        st.session_state.mom_name = mom_name

        st.session_state.baby_name = baby_name

        st.session_state.pregnancy_week = pregnancy_week

        st.session_state.due_date = due_date

        st.session_state.page = "home"

        st.rerun()


# ==========================================
# HOME
# 기존 HOME 화면 그대로 유지
# ==========================================

def show_home():

    mom_name = st.session_state.mom_name
    baby_name = st.session_state.baby_name
    week = st.session_state.pregnancy_week
    due_date = st.session_state.due_date

    st.markdown(
        '<div class="logo">✦ MOMI ✦</div>',
        unsafe_allow_html=True
    )

    st.caption(
        f"Good morning, {mom_name} 🌷"
    )

    st.markdown(
        f"# Baby {baby_name}"
    )

    st.caption(
        f"Your pregnancy journey · Week {week}"
    )

    show_momi()


    # ==========================================
    # CURRENT WEEK
    # ==========================================

    with st.container(border=True):

        st.caption("CURRENT WEEK")

        st.markdown(
            f"# {week}"
        )

        st.caption("OF 40 WEEKS")


    st.write("")


    # ==========================================
    # HEALTH / BABY
    # ==========================================

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.caption("🌸 HEALTH")

            st.write("Sleep · 7.2 h")
            st.write("Stress · ●●○○○")
            st.write("Exercise · 30 min")


    with col2:

        with st.container(border=True):

            st.caption("🍼 BABY")

            st.write("Growth looks good")
            st.write("Weekly milestone")
            st.write("✦ Keep going")


    st.write("")


    # ==========================================
    # TODAY'S MILESTONE
    # ==========================================

    with st.container(border=True):

        st.caption("🌷 TODAY'S MILESTONE")

        st.write(
            "Baby is growing every day."
        )

        st.write(
            "Take a little time to rest,"
        )

        st.write(
            "hydrate and listen to your body."
        )


    st.write("")


    # ==========================================
    # AI CONSULTANT
    # ==========================================

    with st.container(border=True):

        st.caption("✨ AI CONSULTANT")

        st.write(
            "You're doing beautifully."
        )

        st.write(
            "Let's take care of you and baby,"
        )

        st.write(
            "one day at a time."
        )


    st.write("")


    # ==========================================
    # DUE DATE
    # ==========================================

    with st.container(border=True):

        st.caption("🎀 DUE DATE")

        st.write(
            due_date.strftime("%B %d, %Y")
        )


    st.write("")


    # ==========================================
    # EDIT PROFILE
    # ==========================================

    if st.button("EDIT PROFILE"):

        st.session_state.page = "signup"

        st.rerun()


    st.write("")


    # ==========================================
    # WELCOME
    # ==========================================

    if st.button("WELCOME 🌷"):

        st.session_state.page = "welcome"

        st.rerun()


# ==========================================
# WELCOME
# ==========================================

def show_welcome():

    st.markdown(
        '<div class="logo">✦ MOMI ✦</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        "# Welcome 🌷"
    )

    st.caption(
        "Your pregnancy journey starts here."
    )

    show_momi()

    st.write("")


    # ==========================================
    # 5개 버튼
    # 가로 한 줄
    # ==========================================

    col1, col2, col3, col4, col5 = st.columns(5)


    with col1:

        if st.button(
            "🌷\nTODAY",
            use_container_width=True
        ):

            st.session_state.page = "today"

            st.rerun()


    with col2:

        if st.button(
            "🌸\nHEALTH",
            use_container_width=True
        ):

            st.session_state.page = "health"

            st.rerun()


    with col3:

        if st.button(
            "🍼\nMILESTONE",
            use_container_width=True
        ):

            st.session_state.page = "milestone"

            st.rerun()


    with col4:

        if st.button(
            "✨\nAI",
            use_container_width=True
        ):

            st.session_state.page = "ai"

            st.rerun()


    with col5:

        if st.button(
            "🏥\nHOSPITAL",
            use_container_width=True
        ):

            st.session_state.page = "hospital"

            st.rerun()


# ==========================================
# TODAY
# ==========================================

def show_today():

    st.markdown(
        '<div class="logo">✦ MOMI ✦</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        "# 🌷 Today"
    )

    st.caption(
        "Your daily pregnancy journey"
    )

    show_momi()

    st.write("")


    # ==========================================
    # TODAY 3 MENU
    # ==========================================

    col1, col2, col3 = st.columns(3)


    with col1:

        if st.button(
            "📝 Daily Health Check",
            use_container_width=True
        ):

            st.session_state.page = "daily_health"

            st.rerun()


    with col2:

        if st.button(
            "🌸 Weekly Milestone",
            use_container_width=True
        ):

            st.session_state.page = "weekly_milestone"

            st.rerun()


    with col3:

        if st.button(
            "🏥 Next Hospital Visit",
            use_container_width=True
        ):

            st.session_state.page = "next_hospital"

            st.rerun()


    st.write("")


    if st.button("← BACK TO HOME"):

        st.session_state.page = "home"

        st.rerun()


# ==========================================
# HEALTH
# ==========================================

def show_health():

    st.markdown(
        '<div class="logo">✦ MOMI ✦</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        "# 🌸 Health"
    )

    st.caption(
        "Take care of you and baby"
    )

    show_momi()

    st.write("")


    # ==========================================
    # HEALTH 3 MENU
    # ==========================================

    col1, col2, col3 = st.columns(3)


    with col1:

        if st.button(
            "❤️ Health Dashboard",
            use_container_width=True
        ):

            st.session_state.page = "health_dashboard"

            st.rerun()


    with col2:

        if st.button(
            "👥 Peer Comparison",
            use_container_width=True
        ):

            st.session_state.page = "peer_comparison"

            st.rerun()


    with col3:

        if st.button(
            "📈 Health Trend AI",
            use_container_width=True
        ):

            st.session_state.page = "health_trend"

            st.rerun()


    st.write("")


    if st.button("← BACK TO HOME"):

        st.session_state.page = "home"

        st.rerun()


# ==========================================
# MILESTONE
# ==========================================

def show_milestone():

    st.markdown(
        '<div class="logo">✦ MOMI ✦</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        "# 🍼 Milestone"
    )

    st.caption(
        "See your baby's weekly journey"
    )

    show_momi()

    st.write("")


    # ==========================================
    # SELECT WEEK
    # ==========================================

    st.markdown(
        "### 🌸 SELECT WEEK"
    )

    st.write("")


    # 1~40 / 8개씩
    for row in range(5):

        cols = st.columns(8)

        for i in range(8):

            week_number = row * 8 + i + 1

            if week_number <= 40:

                with cols[i]:

                    if st.button(
                        str(week_number),
                        use_container_width=True,
                        key=f"week_{week_number}"
                    ):

                        st.session_state.selected_week = week_number

                        st.session_state.page = "milestone_week"

                        st.rerun()


    st.write("")


    if st.button("← BACK TO HOME"):

        st.session_state.page = "home"

        st.rerun()


# ==========================================
# 선택한 주차
# ==========================================

def show_milestone_week():

    week = st.session_state.selected_week

    st.markdown(
        '<div class="logo">✦ MOMI ✦</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"# Week {week} 🌸"
    )

    st.caption(
        f"Pregnancy information for Week {week}"
    )

    show_momi()

    st.write("")


    with st.container(border=True):

        st.caption(
            f"WEEK {week} MILESTONE"
        )

        st.write(
            "Baby development information"
        )

        st.write(
            "and weekly pregnancy guidance"
        )

        st.write(
            "will be added here."
        )


    st.write("")


    if st.button("← SELECT ANOTHER WEEK"):

        st.session_state.page = "milestone"

        st.rerun()


    if st.button("← BACK TO HOME"):

        st.session_state.page = "home"

        st.rerun()


# ==========================================
# AI
# ==========================================

def show_ai():

    st.markdown(
        '<div class="logo">✦ MOMI ✦</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        "# ✨ AI Consultant"
    )

    st.caption(
        "Your gentle AI pregnancy companion"
    )

    show_momi()

    st.write("")


    if st.button(
        "🤖 AI Consultation",
        use_container_width=True
    ):

        st.session_state.page = "ai_consultation"

        st.rerun()


    st.write("")


    if st.button("← BACK TO HOME"):

        st.session_state.page = "home"

        st.rerun()


# ==========================================
# HOSPITAL
# ==========================================

def show_hospital():

    st.markdown(
        '<div class="logo">✦ MOMI ✦</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        "# 🏥 Hospital"
    )

    st.caption(
        "Find and manage your hospital information"
    )

    show_momi()

    st.write("")


    # ==========================================
    # HOSPITAL 3 MENU
    # ==========================================

    col1, col2, col3 = st.columns(3)


    with col1:

        if st.button(
            "📅 Schedule",
            use_container_width=True
        ):

            st.session_state.page = "hospital_schedule"

            st.rerun()


    with col2:

        if st.button(
            "📋 Appointments",
            use_container_width=True
        ):

            st.session_state.page = "hospital_appointments"

            st.rerun()


    with col3:

        if st.button(
            "💌 Hospital Messages",
            use_container_width=True
        ):

            st.session_state.page = "hospital_messages"

            st.rerun()


    st.write("")


    if st.button("← BACK TO HOME"):

        st.session_state.page = "home"

        st.rerun()


# ==========================================
# 임시 세부 화면
# ==========================================

def show_empty_page(title, description):

    st.markdown(
        '<div class="logo">✦ MOMI ✦</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"# {title}"
    )

    st.caption(
        description
    )

    show_momi()

    st.write("")

    with st.container(border=True):

        st.markdown(
            "### Coming soon 🌷"
        )

        st.write(
            "This page will be ready soon."
        )

    st.write("")

    if st.button("← BACK TO HOME"):

        st.session_state.page = "home"

        st.rerun()


# ==========================================
# 화면 이동
# ==========================================

if st.session_state.page == "signup":

    show_signup()


elif st.session_state.page == "home":

    show_home()


elif st.session_state.page == "welcome":

    show_welcome()


# ==========================================
# TODAY
# ==========================================

elif st.session_state.page == "today":

    show_today()


elif st.session_state.page == "daily_health":

    show_empty_page(
        "📝 Daily Health Check",
        "Record your health today"
    )


elif st.session_state.page == "weekly_milestone":

    show_empty_page(
        "🌸 Weekly Milestone",
        "Check your current pregnancy week"
    )


elif st.session_state.page == "next_hospital":

    show_empty_page(
        "🏥 Next Hospital Visit",
        "Check your next hospital visit"
    )


# ==========================================
# HEALTH
# ==========================================

elif st.session_state.page == "health":

    show_health()


elif st.session_state.page == "health_dashboard":

    show_empty_page(
        "❤️ Health Dashboard",
        "View your health records"
    )


elif st.session_state.page == "peer_comparison":

    show_empty_page(
        "👥 Peer Comparison",
        "Compare general health indicators"
    )


elif st.session_state.page == "health_trend":

    show_empty_page(
        "📈 Health Trend AI",
        "AI analysis of your health trends"
    )


# ==========================================
# MILESTONE
# ==========================================

elif st.session_state.page == "milestone":

    show_milestone()


elif st.session_state.page == "milestone_week":

    show_milestone_week()


# ==========================================
# AI
# ==========================================

elif st.session_state.page == "ai":

    show_ai()


elif st.session_state.page == "ai_consultation":

    show_empty_page(
        "🤖 AI Consultation",
        "Ask MOMI about pregnancy and health"
    )


# ==========================================
# HOSPITAL
# ==========================================

elif st.session_state.page == "hospital":

    show_hospital()


elif st.session_state.page == "hospital_schedule":

    show_empty_page(
        "📅 Schedule",
        "Manage your hospital schedule"
    )


elif st.session_state.page == "hospital_appointments":

    show_empty_page(
        "📋 Appointments",
        "Check your hospital appointments"
    )


elif st.session_state.page == "hospital_messages":

    show_empty_page(
        "💌 Hospital Messages",
        "Check your hospital messages"
    )