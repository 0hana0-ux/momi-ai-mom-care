import streamlit as st
import streamlit.components.v1 as components
from datetime import date


# --------------------------------------------------
# PAGE SETTING
# --------------------------------------------------

st.set_page_config(
    page_title="MOMI",
    page_icon="✦",
    layout="centered"
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

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

if "selected_week" not in st.session_state:
    st.session_state.selected_week = 18


# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;500;600;700;800&family=Fredoka:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Baloo 2', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 20% 20%, #fff7fb 0%, transparent 30%),
        radial-gradient(circle at 80% 30%, #f8f0ff 0%, transparent 30%),
        linear-gradient(135deg, #fffafd 0%, #f8f1ff 50%, #fff7fb 100%);
}

/* 전체 폭 */
.block-container {
    max-width: 900px;
    padding-top: 40px;
    padding-bottom: 60px;
}


/* LOGO */
.logo {
    text-align: center;
    font-family: 'Fredoka', sans-serif;
    font-size: 32px;
    font-weight: 600;
    color: #8d6eaa;
    letter-spacing: 2px;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #b39ac4;
    font-size: 15px;
    letter-spacing: 2px;
    margin-bottom: 20px;
}


/* INPUT */
.stTextInput input {
    border-radius: 18px !important;
    border: 2px solid #eadcf2 !important;
    background: rgba(255,255,255,0.8) !important;
    padding: 14px !important;
    font-family: 'Baloo 2', sans-serif !important;
}

.stNumberInput input {
    border-radius: 18px !important;
    border: 2px solid #eadcf2 !important;
    background: rgba(255,255,255,0.8) !important;
    font-family: 'Baloo 2', sans-serif !important;
}

.stDateInput input {
    border-radius: 18px !important;
    border: 2px solid #eadcf2 !important;
    background: rgba(255,255,255,0.8) !important;
    font-family: 'Baloo 2', sans-serif !important;
}


/* BUTTON */
.stButton > button {
    width: 100%;
    border: none !important;
    border-radius: 22px !important;
    padding: 14px 20px !important;
    background: linear-gradient(135deg, #e8c8ef, #d9c1ef) !important;
    color: #6e557f !important;
    font-family: 'Fredoka', sans-serif !important;
    font-size: 16px !important;
    font-weight: 500 !important;
    box-shadow: 0 8px 18px rgba(160, 120, 180, 0.12);
    transition: 0.2s;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 22px rgba(160, 120, 180, 0.18);
}


/* WELCOME MENU */
div[data-testid="stHorizontalBlock"] .stButton > button {
    font-size: 14px !important;
    padding: 12px 4px !important;
    min-height: 65px;
    white-space: pre-line;
}


/* CARD */
.card {
    background: rgba(255,255,255,0.78);
    border: 1px solid rgba(225,205,235,0.7);
    border-radius: 28px;
    padding: 24px;
    margin: 12px 0;
    box-shadow: 0 10px 30px rgba(160,120,180,0.08);
}

.card-title {
    font-family: 'Fredoka', sans-serif;
    color: #8b6b9e;
    font-size: 18px;
    font-weight: 600;
}

.card-text {
    color: #9b87a8;
    font-size: 14px;
}


/* CAPTION */
.small-caption {
    text-align: center;
    color: #b5a1bd;
    font-size: 14px;
}


/* WEEK */
.week {
    text-align: center;
    color: #8c6ba0;
    font-family: 'Fredoka', sans-serif;
    font-size: 30px;
    font-weight: 600;
}


/* MOBILE */
@media (max-width: 600px) {

    .block-container {
        padding-left: 18px;
        padding-right: 18px;
    }

    .logo {
        font-size: 28px;
    }

}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# MOMI CHARACTER
# --------------------------------------------------

def show_momi():

    momi_svg = """
    <div style="display:flex; justify-content:center; margin:20px 0 25px 0;">

    <svg width="220" height="250" viewBox="0 0 220 250"
         xmlns="http://www.w3.org/2000/svg">

        <!-- shadow -->
        <ellipse
            cx="110"
            cy="220"
            rx="55"
            ry="10"
            fill="#E8D8E8"
        />

        <!-- body -->
        <ellipse
            cx="110"
            cy="125"
            rx="62"
            ry="82"
            fill="#DCCCF0"
        />

        <!-- head -->
        <circle
            cx="110"
            cy="78"
            r="48"
            fill="#E7D9F5"
        />

        <!-- ears -->
        <circle
            cx="68"
            cy="68"
            r="14"
            fill="#D5C2E8"
        />

        <circle
            cx="152"
            cy="68"
            r="14"
            fill="#D5C2E8"
        />

        <!-- eyes -->
        <circle
            cx="94"
            cy="78"
            r="5"
            fill="#6D597A"
        />

        <circle
            cx="126"
            cy="78"
            r="5"
            fill="#6D597A"
        />

        <!-- nose -->
        <ellipse
            cx="110"
            cy="91"
            rx="5"
            ry="4"
            fill="#A98BBD"
        />

        <!-- smile -->
        <path
            d="M103 99 Q110 105 117 99"
            stroke="#8D729E"
            stroke-width="3"
            fill="none"
            stroke-linecap="round"
        />

        <!-- arms -->
        <ellipse
            cx="55"
            cy="135"
            rx="13"
            ry="30"
            fill="#D5C2E8"
        />

        <ellipse
            cx="165"
            cy="135"
            rx="13"
            ry="30"
            fill="#D5C2E8"
        />

        <!-- belly -->
        <ellipse
            cx="110"
            cy="145"
            rx="35"
            ry="42"
            fill="#F5ECFA"
        />

        <!-- heart -->
        <path
            d="M110 164
               C94 149 82 160 88 173
               C94 185 110 194 110 194
               C110 194 126 185 132 173
               C138 160 126 149 110 164Z"
            fill="#CBA9D9"
        />

    </svg>

    </div>
    """

    components.html(momi_svg, height=290)


# --------------------------------------------------
# SIGN UP
# --------------------------------------------------

def show_signup():

    st.markdown("<div class='logo'>✦ MOMI ✦</div>", unsafe_allow_html=True)

    st.markdown(
        "<div class='subtitle'>MOM CARE AI</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h1 style='text-align:center; color:#8B6B9E; font-family:Fredoka;'>"
        "40 WEEK ADVENTURE"
        "</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p class='small-caption'>Your gentle AI companion throughout pregnancy</p>",
        unsafe_allow_html=True
    )

    show_momi()

    mom_name = st.text_input(
        "Mom Name",
        value=st.session_state.mom_name
    )

    baby_name = st.text_input(
        "Baby Name",
        value=st.session_state.baby_name
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

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("START ✦", use_container_width=True):

        st.session_state.mom_name = mom_name
        st.session_state.baby_name = baby_name
        st.session_state.pregnancy_week = pregnancy_week
        st.session_state.due_date = due_date
        st.session_state.page = "home"

        st.rerun()


# --------------------------------------------------
# HOME
# --------------------------------------------------

def show_home():

    st.markdown("<div class='logo'>✦ MOMI ✦</div>", unsafe_allow_html=True)

    st.markdown(
        "<div class='subtitle'>MOM CARE AI</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h2 style='text-align:center; color:#8B6B9E;'>Good morning 🌷</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p class='small-caption'>"
        f"{st.session_state.mom_name or 'Mom'} & "
        f"{st.session_state.baby_name or 'Baby'}"
        f"</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='week'>WEEK {st.session_state.pregnancy_week}</div>",
        unsafe_allow_html=True
    )

    show_momi()

    # CURRENT WEEK
    st.markdown(
        f"""
        <div class='card'>
            <div class='card-title'>🌷 CURRENT WEEK</div>
            <div class='card-text'>
                You are currently in Week {st.session_state.pregnancy_week}.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # HEALTH / BABY
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class='card'>
                <div class='card-title'>❤️ HEALTH</div>
                <div class='card-text'>
                    Check your health journey.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class='card'>
                <div class='card-title'>🍼 BABY</div>
                <div class='card-text'>
                    See your baby's journey.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # TODAY'S MILESTONE
    st.markdown(
        """
        <div class='card'>
            <div class='card-title'>🌸 TODAY'S MILESTONE</div>
            <div class='card-text'>
                Discover what's happening this week.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # AI CONSULTANT
    st.markdown(
        """
        <div class='card'>
            <div class='card-title'>✨ AI CONSULTANT</div>
            <div class='card-text'>
                Ask MOMI anything about your pregnancy.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # DUE DATE
    st.markdown(
        f"""
        <div class='card'>
            <div class='card-title'>🏥 DUE DATE</div>
            <div class='card-text'>
                {st.session_state.due_date.strftime("%B %d, %Y")}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("EDIT PROFILE", use_container_width=True):
        st.session_state.page = "signup"
        st.rerun()

    if st.button("WELCOME 🌷", use_container_width=True):
        st.session_state.page = "welcome"
        st.rerun()


# --------------------------------------------------
# WELCOME
# --------------------------------------------------

def show_welcome():

    st.markdown("<div class='logo'>✦ MOMI ✦</div>", unsafe_allow_html=True)

    st.markdown(
        "<h1 style='text-align:center; color:#8B6B9E;'>Welcome 🌷</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p class='small-caption'>Your pregnancy journey starts here.</p>",
        unsafe_allow_html=True
    )

    show_momi()

    # 5 MENU BUTTONS
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("🌷\nTODAY", use_container_width=True):
            st.session_state.page = "today"
            st.rerun()

    with col2:
        if st.button("🌸\nHEALTH", use_container_width=True):
            st.session_state.page = "health"
            st.rerun()

    with col3:
        if st.button("🍼\nMILESTONE", use_container_width=True):
            st.session_state.page = "milestone"
            st.rerun()

    with col4:
        if st.button("✨\nAI", use_container_width=True):
            st.session_state.page = "ai"
            st.rerun()

    with col5:
        if st.button("🏥\nHOSPITAL", use_container_width=True):
            st.session_state.page = "hospital"
            st.rerun()


# --------------------------------------------------
# TODAY
# --------------------------------------------------

def show_today():

    st.markdown("<div class='logo'>✦ MOMI ✦</div>", unsafe_allow_html=True)

    st.markdown("# TODAY 🌷")

    st.caption("Your little check-in for today.")

    show_momi()

    # TODAY MENU
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

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("← BACK TO HOME", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()


# --------------------------------------------------
# HEALTH
# --------------------------------------------------

def show_health():

    st.markdown("<div class='logo'>✦ MOMI ✦</div>", unsafe_allow_html=True)

    st.markdown("# HEALTH 🌸")

    st.caption("Your pregnancy health at a glance.")

    show_momi()

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

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("← BACK TO HOME", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()


# --------------------------------------------------
# MILESTONE
# --------------------------------------------------

def show_milestone():

    st.markdown("<div class='logo'>✦ MOMI ✦</div>", unsafe_allow_html=True)

    st.markdown("# MILESTONE 🍼")

    st.caption("Choose a week to explore your pregnancy journey.")

    show_momi()

    st.markdown(
        "<div class='week'>SELECT WEEK</div>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # 1 ~ 40
    for row in range(5):

        cols = st.columns(8)

        for col_index in range(8):

            week = row * 8 + col_index + 1

            if week <= 40:

                with cols[col_index]:

                    if st.button(
                        str(week),
                        use_container_width=True,
                        key=f"week_{week}"
                    ):
                        st.session_state.selected_week = week
                        st.session_state.page = "milestone_week"
                        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("← BACK TO HOME", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()


# --------------------------------------------------
# SELECTED WEEK
# --------------------------------------------------

def show_milestone_week():

    week = st.session_state.selected_week

    st.markdown("<div class='logo'>✦ MOMI ✦</div>", unsafe_allow_html=True)

    st.markdown(
        f"<h1 style='text-align:center; color:#8B6B9E;'>"
        f"WEEK {week} 🌸"
        f"</h1>",
        unsafe_allow_html=True
    )

    st.caption("Your weekly pregnancy guide.")

    show_momi()

    st.markdown(
        f"""
        <div class='card'>
            <div class='card-title'>🌸 WEEK {week} MILESTONE</div>
            <div class='card-text'>
                Baby development and pregnancy information for Week {week}
                will appear here.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='card'>
            <div class='card-title'>💡 WHAT TO KNOW</div>
            <div class='card-text'>
                Weekly information, helpful tips, and things to watch for
                will be added here.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("← SELECT ANOTHER WEEK", use_container_width=True):
        st.session_state.page = "milestone"
        st.rerun()

    if st.button("← BACK TO HOME", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()


# --------------------------------------------------
# AI
# --------------------------------------------------

def show_ai():

    st.markdown("<div class='logo'>✦ MOMI ✦</div>", unsafe_allow_html=True)

    st.markdown("# AI ✨")

    st.caption("Your gentle AI pregnancy companion.")

    show_momi()

    if st.button(
        "🤖 AI Consultation",
        use_container_width=True
    ):
        st.session_state.page = "ai_consultation"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("← BACK TO HOME", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()


# --------------------------------------------------
# HOSPITAL
# --------------------------------------------------

def show_hospital():

    st.markdown("<div class='logo'>✦ MOMI ✦</div>", unsafe_allow_html=True)

    st.markdown("# HOSPITAL 🏥")

    st.caption("Keep your hospital journey organized.")

    show_momi()

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

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("← BACK TO HOME", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()


# --------------------------------------------------
# SUB PAGE
# --------------------------------------------------

def show_sub_page(title, description):

    st.markdown("<div class='logo'>✦ MOMI ✦</div>", unsafe_allow_html=True)

    st.markdown(
        f"<h1 style='text-align:center; color:#8B6B9E;'>"
        f"{title}"
        f"</h1>",
        unsafe_allow_html=True
    )

    st.caption(description)

    show_momi()

    st.markdown(
        """
        <div class='card'>
            <div class='card-title'>🌷 COMING SOON</div>
            <div class='card-text'>
                This feature will be added here.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("← BACK TO HOME", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()


# --------------------------------------------------
# ROUTER
# --------------------------------------------------

if st.session_state.page == "signup":
    show_signup()

elif st.session_state.page == "home":
    show_home()

elif st.session_state.page == "welcome":
    show_welcome()

elif st.session_state.page == "today":
    show_today()

elif st.session_state.page == "health":
    show_health()

elif st.session_state.page == "milestone":
    show_milestone()

elif st.session_state.page == "milestone_week":
    show_milestone_week()

elif st.session_state.page == "ai":
    show_ai()

elif st.session_state.page == "hospital":
    show_hospital()

elif st.session_state.page == "daily_health":
    show_sub_page(
        "Daily Health Check 📝",
        "Record your health today."
    )

elif st.session_state.page == "weekly_milestone":
    show_sub_page(
        "Weekly Milestone 🌸",
        "Check what is happening during your current pregnancy week."
    )

elif st.session_state.page == "next_hospital":
    show_sub_page(
        "Next Hospital Visit 🏥",
        "Check your next hospital visit."
    )

elif st.session_state.page == "health_dashboard":
    show_sub_page(
        "Health Dashboard ❤️",
        "View your health records and health check results."
    )

elif st.session_state.page == "peer_comparison":
    show_sub_page(
        "Peer Comparison 👥",
        "Compare general health indicators by pregnancy week."
    )

elif st.session_state.page == "health_trend":
    show_sub_page(
        "Health Trend AI 📈",
        "AI analysis of your health record trends."
    )

elif st.session_state.page == "ai_consultation":
    show_sub_page(
        "AI Consultation 🤖",
        "Ask MOMI about pregnancy and health."
    )

elif st.session_state.page == "hospital_schedule":
    show_sub_page(
        "Schedule 📅",
        "Manage your hospital schedule."
    )

elif st.session_state.page == "hospital_appointments":
    show_sub_page(
        "Appointments 📋",
        "Check your hospital appointments."
    )

elif st.session_state.page == "hospital_messages":
    show_sub_page(
        "Hospital Messages 💌",
        "Check your hospital messages."
    )
