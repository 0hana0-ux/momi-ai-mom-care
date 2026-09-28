import streamlit as st
import streamlit.components.v1 as components
from datetime import date, datetime, timedelta
import calendar
import random
import pandas as pd
import altair as alt


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

# 선택한 주차를 저장
if "selected_week" not in st.session_state:
    st.session_state.selected_week = 18


# ==========================================
# DAILY HEALTH RECORDS
# 날짜별 건강 기록 저장
# ==========================================

if "health_records" not in st.session_state:
    st.session_state.health_records = {}


# ==========================================
# HOSPITAL DATA
# ==========================================

if "hospital_data" not in st.session_state:
    hospital_names = [
        "Seoul Women's Hospital",
        "Mirae Women's Hospital",
        "Harmony Women's Clinic",
        "Bloom Women's Hospital",
        "Grace Women's Hospital",
        "Moms Care Hospital",
        "Bright Hope Women's Clinic",
        "Evergreen Women's Hospital",
        "Pure Heart Women's Clinic",
        "Morning Star Hospital",
        "Little Bloom Women's Hospital",
        "Warm Nest Women's Clinic",
        "Blue Sky Women's Hospital",
        "Gentle Care Women's Clinic",
        "Spring Hope Hospital",
        "Lovely Mom Women's Hospital",
        "Rainbow Women's Clinic",
        "Sunny Days Women's Hospital",
        "Dream Tree Women's Clinic",
        "New Life Women's Hospital"
    ]

    first_names = [
        "Emily", "Sarah", "Daniel", "Olivia", "Sophia", "James",
        "Grace", "Michael", "Emma", "Noah", "Hannah", "Ethan",
        "Chloe", "Lucas", "Mia", "Henry", "Ella", "David",
        "Lily", "Alex", "Sophie", "Ryan", "Anna", "Leo",
        "Claire", "Matthew", "Julia", "Andrew", "Lucy", "William"
    ]

    last_names = [
        "Kim", "Lee", "Park", "Choi", "Jung", "Kang", "Han", "Yoon",
        "Lim", "Shin", "Seo", "Moon", "Kwon", "Baek", "Song", "Oh",
        "Hwang", "Ryu", "Jeon", "Jang"
    ]

    time_pool = [
        "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
        "13:00", "13:30", "14:00", "14:30", "15:00", "15:30",
        "16:00", "16:30", "17:00"
    ]

    rng = random.Random(20260921)
    generated_hospitals = {}
    available_dates = [date.today() + timedelta(days=i) for i in range(2, 46)]

    name_index = 0

    for hospital in hospital_names:
        doctors = []

        for doctor_number in range(4):
            first = first_names[name_index % len(first_names)]
            last = last_names[(name_index * 3 + doctor_number) % len(last_names)]
            name_index += 1

            doctor_schedule = {}
            selected_dates = sorted(rng.sample(available_dates, 9))

            for available_date in selected_dates:
                selected_times = sorted(rng.sample(time_pool, 3))
                doctor_schedule[available_date.isoformat()] = selected_times

            doctors.append({
                "name": f"Dr. {first} {last}",
                "specialty": "Obstetrics & Gynecology",
                "schedule": doctor_schedule
            })

        generated_hospitals[hospital] = doctors

    st.session_state.hospital_data = generated_hospitals

if "appointments" not in st.session_state:
    st.session_state.appointments = []

if "personal_schedules" not in st.session_state:
    st.session_state.personal_schedules = {}

if "hospital_selected_hospital" not in st.session_state:
    st.session_state.hospital_selected_hospital = None

if "hospital_selected_doctor" not in st.session_state:
    st.session_state.hospital_selected_doctor = None

if "hospital_selected_date" not in st.session_state:
    st.session_state.hospital_selected_date = None

if "hospital_selected_time" not in st.session_state:
    st.session_state.hospital_selected_time = None

if "schedule_month" not in st.session_state:
    st.session_state.schedule_month = date.today().replace(day=1)

if "schedule_selected_date" not in st.session_state:
    st.session_state.schedule_selected_date = date.today()


# ==========================================
# AI CONSULTATION SESSION STATE
# ==========================================

if "ai_messages" not in st.session_state:
    st.session_state.ai_messages = []

if "ai_current_menu" not in st.session_state:
    st.session_state.ai_current_menu = "main"

if "ai_menu_history" not in st.session_state:
    st.session_state.ai_menu_history = []


# ==========================================
# MILESTONE DATA
# 1~40주
# ==========================================

milestones = {

    1: {
        "baby": "This is the beginning of the pregnancy timeline. The body is preparing for ovulation and a possible pregnancy. Pregnancy weeks are counted from the first day of the last menstrual period.",
        "mom": "Start building healthy habits with folate-rich vegetables, fruits, beans, and whole grains. Regular sleep, hydration, and gentle daily movement can help prepare your body.",
        "message": "Every beautiful journey starts with a first little step. 🌷"
    },

    2: {
        "baby": "Ovulation may occur around this time, and fertilization can happen during this part of the cycle. The baby's organs have not yet formed; this is the very beginning of the pregnancy timeline.",
        "mom": "Continue taking folic acid if recommended for you, and choose balanced meals throughout the day. Avoid alcohol and smoking, and check any regular medications with your healthcare provider.",
        "message": "Something wonderful may be just beginning. Take it one day at a time. ✦"
    },

    3: {
        "baby": "If fertilization has occurred, the cells begin dividing rapidly as the early embryo develops. The cells start organizing into structures that will later form the baby and placenta.",
        "mom": "Keep folate-rich foods such as leafy greens, beans, and citrus fruits in your meals. If you feel tired or nauseous, small meals and regular hydration may feel easier.",
        "message": "A tiny beginning can lead to something truly amazing. 💕"
    },

    4: {
        "baby": "The early embryo may attach to the lining of the uterus during this stage. Cells begin taking on different roles that will eventually form the baby's body and supporting tissues.",
        "mom": "If pregnancy is confirmed, begin planning your prenatal care. Choose a variety of vegetables, fruits, whole grains, and protein foods while giving yourself plenty of gentle rest.",
        "message": "A tiny new beginning is finding its place. 🌸"
    },

    5: {
        "baby": "The early brain and spinal cord begin developing from the neural tube. The heart and digestive system also start forming, making this an important stage for early organ development.",
        "mom": "Folate is especially important during early pregnancy because it supports neural tube development. Try leafy greens, beans, fortified grains, and a prenatal supplement if recommended.",
        "message": "Some of your baby's first important structures are beginning to form. 🌱"
    },

    6: {
        "baby": "The early brain continues to develop, and the heart begins its early rhythmic activity. Small structures that will become the eyes, ears, arms, and legs are also starting to appear.",
        "mom": "If nausea is bothering you, try small meals such as crackers, bananas, rice, or toast. Sip water regularly and give yourself extra time to rest when your energy feels low.",
        "message": "A tiny heart and developing nervous system are already hard at work. 💗"
    },

    7: {
        "baby": "The brain and facial structures continue developing, while the early spine and bones begin taking shape. The tiny limb buds are becoming more defined.",
        "mom": "Include protein foods such as eggs, tofu, beans, or lean meat in your meals. If you feel comfortable, a short gentle walk can be a refreshing way to move your body.",
        "message": "Your baby's little face and body are slowly taking shape. 🌷"
    },

    8: {
        "baby": "The arms and legs become longer, and the hands and feet begin taking clearer shape. The brain continues rapid development, while the early lungs also begin forming.",
        "mom": "Enjoy a colorful mix of fruits and vegetables along with protein-rich foods. You can also spend a few quiet minutes listening to music or talking gently to your baby.",
        "message": "Tiny hands and feet are beginning to take shape. 🍼"
    },

    9: {
        "baby": "The elbows, fingers, and toes become more recognizable as muscles and joints continue developing. Most major organs have begun forming and are now growing and becoming more organized.",
        "mom": "Choose iron-containing foods such as lean meat, beans, spinach, and fortified grains. Pairing a variety of vegetables and fruits with meals can help you enjoy a wider range of nutrients.",
        "message": "Your baby's little body is becoming more recognizable every day. ✨"
    },

    10: {
        "baby": "The eyelids, outer ears, and facial features become more defined. The digestive system continues developing, and the embryo has now entered the fetal stage of development.",
        "mom": "Keep regular meals and hydration part of your routine. If you have prenatal appointments coming up, write down questions and bring a list of medications or supplements you take.",
        "message": "Your little one is beginning to look more and more like a tiny baby. 🌸"
    },

    11: {
        "baby": "The fingers and toes are clearly separated, while facial features continue to develop. The liver and blood-forming systems are becoming more active, and early tooth structures begin developing.",
        "mom": "Include iron and protein through foods such as lean meat, eggs, beans, and leafy greens. Add colorful fruits and vegetables to make meals both nutritious and enjoyable.",
        "message": "Even tiny fingers and toes are taking shape. 🌷"
    },

    12: {
        "baby": "The fingers and toes continue to develop, and the baby can make small movements. The brain and nervous system are becoming more organized as the body learns to coordinate movement.",
        "mom": "Calcium-rich foods such as milk, yogurt, tofu, or fortified alternatives can be useful choices. Relax with a favorite book or gentle music when you need a quiet moment.",
        "message": "You've made it through an important early stage. You're doing beautifully. 💕"
    },

    13: {
        "baby": "Bones and muscles continue developing, making the arms and legs stronger. Facial proportions also begin changing as the head and body gradually become more balanced.",
        "mom": "Choose meals that combine protein and calcium, such as tofu, eggs, yogurt, or beans. If your energy allows, enjoy a gentle walk and a little fresh air.",
        "message": "Your baby's little body is becoming stronger and more defined. 🌱"
    },

    14: {
        "baby": "The face and neck become more developed, while bones and muscles continue growing. The nervous system is also developing the connections needed for future movement and coordination.",
        "mom": "Whole grains, vegetables, and fruits can provide useful fiber and nutrients. Take a relaxed walk, listen to music, or talk softly to your baby during a peaceful moment.",
        "message": "A new chapter of growth is beginning. 🌸"
    },

    15: {
        "baby": "Bones continue becoming stronger, while muscles and joints allow the arms and legs to move more naturally. The skin is still very thin and continues developing its protective layers.",
        "mom": "Include calcium and protein through foods such as yogurt, tofu, eggs, beans, and fish that are appropriate during pregnancy. Try a relaxing playlist while resting.",
        "message": "Your baby is practicing little movements inside. ✦"
    },

    16: {
        "baby": "Bones, joints, and muscles continue developing, allowing a wider range of movement. Facial muscles are also developing, creating the foundations for future expressions and movements.",
        "mom": "Keep meals balanced with iron, protein, vegetables, and whole grains. Gentle stretching or a short walk can help you stay comfortably active if your healthcare provider has no restrictions.",
        "message": "Your little one is learning how to move and grow. 🍼"
    },

    17: {
        "baby": "Bones continue to develop, and the body begins storing small amounts of fat. Structures involved in hearing are also developing as the baby becomes more prepared to receive sounds.",
        "mom": "Foods containing omega-3 fatty acids, such as pregnancy-safe fish, can be part of a balanced diet. Check local pregnancy fish guidelines and enjoy calming music during your quiet time.",
        "message": "Your baby is preparing not only to grow, but also to experience the world. 🎵"
    },

    18: {
        "baby": "The nervous system and muscles continue connecting, allowing the baby's movements to become more active. The ears are developing further and becoming better prepared to receive sounds.",
        "mom": "Include iron, protein, vegetables, and fruits throughout your meals. Try reading a short book aloud or telling your baby about your day.",
        "message": "Your voice and your baby's growing world are getting closer every day. 💗"
    },

    19: {
        "baby": "Hearing structures continue developing, helping the baby become more responsive to sounds. The skin develops further and is covered by a protective coating that helps protect it from the surrounding fluid.",
        "mom": "Choose calcium-rich and protein-rich foods such as yogurt, tofu, eggs, or beans. Take a gentle walk, listen to calming music, or simply enjoy a few peaceful minutes together.",
        "message": "Your baby is slowly getting ready to hear the world around them. 🎶"
    },

    20: {
        "baby": "The brain and nervous system continue developing, while the baby's movements become more coordinated. Swallowing and digestive movements are also being practiced as the body learns new functions.",
        "mom": "Keep meals balanced with iron, calcium, protein, fruits, and vegetables. Check your prenatal appointment schedule and make time for gentle movement and comfortable rest.",
        "message": "You're halfway through this beautiful journey. Look how far you've come. 🌷"
    },

    21: {
        "baby": "The baby's hearing continues developing, making sounds easier to receive. The digestive system also practices swallowing as the baby becomes more familiar with basic body functions.",
        "mom": "Try protein-rich foods such as eggs, tofu, beans, and lean meat with plenty of vegetables. Reading aloud or talking softly to your baby can become a relaxing daily ritual.",
        "message": "Your little one is beginning to experience more of your world. 💕"
    },

    22: {
        "baby": "Eyebrows and eyelashes become more visible, while fingernails continue growing. Muscles are becoming stronger, and the digestive system continues practicing important movements.",
        "mom": "Include iron-rich foods such as lean meat, beans, and leafy greens, along with enough water. If you've been sitting for a long time, change positions and gently move your body.",
        "message": "Tiny eyebrows, eyelashes, and nails are appearing. How amazing is that? 🌸"
    },

    23: {
        "baby": "The bone marrow becomes more involved in making blood cells, while the airways and structures of the lungs continue developing. Fat begins accumulating under the skin.",
        "mom": "Combine iron-rich foods with colorful fruits and vegetables. A short bedtime story or calming music can be a simple way to create a peaceful routine.",
        "message": "Your baby is practicing one tiny function after another. 🌱"
    },

    24: {
        "baby": "The airways and air sacs in the lungs continue to develop, while the nervous system grows rapidly. The lungs are preparing for breathing after birth, although they are still developing.",
        "mom": "Choose balanced meals with protein and iron, such as eggs, beans, lean meat, and leafy greens. Stay hydrated and enjoy a gentle walk or light stretching if you feel comfortable.",
        "message": "Your baby's little lungs are getting ready for their first breath. 🫶"
    },

    25: {
        "baby": "The small airways and blood vessels in the lungs continue developing. Bones and muscles grow steadily, while more fat begins forming under the skin.",
        "mom": "Include protein and omega-3-rich foods such as eggs, beans, and pregnancy-safe fish when appropriate. Read a favorite book aloud and enjoy a calm moment with your baby.",
        "message": "Your baby is quietly preparing for life outside the womb. ✨"
    },

    26: {
        "baby": "The eyes continue developing, while eyebrows and eyelashes become more noticeable. Unique fingerprints are forming, and the lungs continue preparing for breathing.",
        "mom": "Choose meals with calcium, protein, vegetables, and fruit. You can listen to music together, talk to your baby, or simply relax with your hands resting comfortably on your belly.",
        "message": "Even tiny fingerprints are becoming uniquely your baby's. 🍼"
    },

    27: {
        "baby": "The brain grows rapidly and the nervous system becomes better at coordinating body functions. The eyelids can open and close, while the lungs continue their long process of maturation.",
        "mom": "Keep iron and protein-rich foods in your regular meals. Try creating a calming bedtime routine with gentle music, comfortable lighting, and enough time for sleep.",
        "message": "Your baby's brain and nervous system are growing so quickly. 🌷"
    },

    28: {
        "baby": "The baby can open and close the eyes, while brain development becomes increasingly active. The lungs continue developing important structures needed for breathing after birth.",
        "mom": "As the third trimester begins, keep up with prenatal visits and recommended checks. Continue balanced meals with iron, calcium, and protein while making room for plenty of rest.",
        "message": "You've reached another beautiful milestone. The final chapter is beginning. 💗"
    },

    29: {
        "baby": "The brain and nervous system continue forming more complex connections, helping control movement and body functions. The lungs keep maturing as the baby practices movements related to breathing.",
        "mom": "Enjoy iron-rich foods such as beans, leafy greens, and lean meat along with fruits and vegetables. A gentle walk or favorite music can help make your daily routine feel lighter.",
        "message": "Your baby is getting ready for a whole new world, one step at a time. 🌸"
    },

    30: {
        "baby": "The brain continues rapid growth and becomes increasingly involved in coordinating movement and body functions. The lungs and eyes also continue developing as the baby prepares for life after birth.",
        "mom": "Keep protein and calcium in your meals and drink water regularly. You can slowly organize baby supplies and create a comfortable space for the weeks ahead.",
        "message": "The day you'll meet your baby is getting closer. ✦"
    },

    31: {
        "baby": "The baby continues gaining weight and storing fat under the skin. Bones keep developing, while the lungs practice rhythmic movements that prepare the body for breathing.",
        "mom": "Choose meals with iron, protein, vegetables, and whole grains. Change positions regularly and take comfortable breaks if sitting or standing for long periods feels tiring.",
        "message": "Your baby is building a cozy little body for the outside world. 🍼"
    },

    32: {
        "baby": "The brain and nervous system continue maturing, while the lungs make steady progress toward greater function. More body fat develops, making the skin appear smoother.",
        "mom": "Include calcium-rich foods such as yogurt, milk, tofu, or fortified alternatives along with protein. Choose a favorite song or story to share during a quiet evening.",
        "message": "Your baby's little body is becoming softer, stronger, and more ready. 🌷"
    },

    33: {
        "baby": "The brain and nervous system continue developing, and the lungs keep maturing for life after birth. Increasing body fat helps the baby prepare to regulate body temperature.",
        "mom": "Keep iron and protein in your daily meals and drink enough water. Check your hospital plan, important contacts, and baby supplies so you can feel more prepared.",
        "message": "The final preparations are quietly happening inside and outside. 💕"
    },

    34: {
        "baby": "Bones and muscles continue developing while the baby stores more fat. The lungs keep maturing, and rhythmic breathing movements continue as the baby prepares for birth.",
        "mom": "Choose balanced meals with protein, vegetables, calcium, and iron. Gentle walks and comfortable rest can help you care for your changing body.",
        "message": "Your baby is getting closer to being ready for the big day. 🌸"
    },

    35: {
        "baby": "More fat develops under the skin, making the baby's appearance rounder and smoother. The heart and blood vessels are well developed, while muscles and bones continue growing.",
        "mom": "Keep protein and calcium-rich foods in your meals and drink water regularly. Start checking your hospital bag and make sure important items are easy to find.",
        "message": "Your little one is beginning to look more like the newborn you'll soon meet. 🍼"
    },

    36: {
        "baby": "The baby continues gaining weight and storing fat for life outside the womb. Brain development continues, and the baby's sleep and wake patterns become more noticeable.",
        "mom": "Keep meals balanced with iron, calcium, protein, fruits, and vegetables. Review your prenatal appointments and make your daily routine as comfortable and restful as possible.",
        "message": "You're getting so close now. Both of you are preparing beautifully. 🌷"
    },

    37: {
        "baby": "The baby's major body systems are prepared for life after birth, while the brain and lungs continue developing. More fat is stored under the skin as the baby becomes rounder.",
        "mom": "Continue regular meals, hydration, and comfortable activity. Review your route to the hospital, important phone numbers, and your birth bag so everything is ready.",
        "message": "The moment you've been waiting for is getting very close. 💗"
    },

    38: {
        "baby": "The baby continues gaining weight and storing body fat. Fingernails may extend beyond the fingertips, while the skin, hair, and other features continue changing as birth approaches.",
        "mom": "Choose easy-to-digest balanced meals with protein, vegetables, and fruit, and keep drinking water. Keep your hospital bag nearby and give yourself plenty of quiet rest.",
        "message": "Your little one is almost ready to meet you. 🌸"
    },

    39: {
        "baby": "The brain and nervous system continue developing even as the baby is well prepared for birth. More fat is stored under the skin, helping the baby prepare for life outside the womb.",
        "mom": "Continue eating regular balanced meals and staying hydrated. Keep your hospital information and important supplies ready, and contact your healthcare provider if you have questions about changes you notice.",
        "message": "Just a little more waiting. Your meeting is almost here. 🫶"
    },

    40: {
        "baby": "At around 40 weeks, the baby is ready for birth and continues preparing for life outside the womb. The brain and lungs keep developing while the body maintains healthy fat stores.",
        "mom": "Keep eating balanced meals, drinking enough water, and resting comfortably. Follow your prenatal care plan and contact your healthcare provider with questions about labor signs or changes you notice.",
        "message": "Forty weeks of growing, waiting, and loving. Your beautiful journey has brought you here. 💕"
    }
}


# ==========================================
# CSS
# 기존 디자인 그대로
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;500;600;700;800&family=Fredoka:wght@400;500;600;700&display=swap');

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

* {
    font-family:
        'Baloo 2',
        sans-serif;
}

.block-container {
    max-width: 720px;
    padding-top: 35px;
    padding-bottom: 70px;
}

h1,
h2,
h3 {
    font-family:
        'Fredoka',
        sans-serif !important;

    color: #735579 !important;

    text-align: center;
}

.stMarkdown,
.stCaption {
    text-align: center;
}

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

.stTextInput,
.stNumberInput,
.stDateInput,
.stSelectbox,
.stSlider {
    text-align: center;
}

.stTextInput label,
.stNumberInput label,
.stDateInput label,
.stSelectbox label,
.stSlider label {
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

div[data-testid="stVerticalBlockBorderWrapper"] p {
    text-align: center;

    color: #735F76;

    font-size: 15px;
}

.stCaption {
    color: #A88AAA !important;

    font-family:
        'Fredoka',
        sans-serif !important;

    font-weight: 500;
}

div[data-testid="stVerticalBlockBorderWrapper"]
h1 {
    font-size: 60px !important;

    color: #C47EAB !important;

    margin: 0;
}

hr {
    border:
        none;

    border-top:
        2px dashed
        #E6D4E7;
}

.stAlert {
    border-radius: 20px;
}

div[data-testid="stHorizontalBlock"] .stButton > button {
    font-size: 14px !important;

    padding: 12px 4px !important;

    min-height: 65px;

    white-space: pre-line;
}

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

        st.session_state.selected_week = pregnancy_week

        st.session_state.page = "home"

        st.rerun()


# ==========================================
# HOME
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

    with st.container(border=True):

        st.caption("CURRENT WEEK")

        st.markdown(
            f"# {week}"
        )

        st.caption("OF 40 WEEKS")

    st.write("")

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

    with st.container(border=True):

        st.caption("🎀 DUE DATE")

        st.write(
            due_date.strftime("%B %d, %Y")
        )

    st.write("")

    if st.button("EDIT PROFILE"):

        st.session_state.page = "signup"

        st.rerun()

    st.write("")

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

            st.session_state.selected_week = st.session_state.pregnancy_week

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
# 📝 DAILY HEALTH CHECK
# ==========================================

def show_daily_health():

    st.markdown(
        '<div class="logo">✦ MOMI ✦</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        "# 📝 Daily Health Check"
    )

    st.caption(
        "Take a little moment to check in with yourself"
    )

    show_momi()

    st.write("")

    check_date = st.date_input(
        "Check Date",
        value=date.today(),
        key="daily_check_date"
    )

    date_key = check_date.isoformat()

    existing = st.session_state.health_records.get(date_key, {})

    st.write("")

    with st.container(border=True):

        st.markdown("### 🩷 BODY")

        weight = st.number_input(
            "Weight (kg)",
            min_value=30.0,
            max_value=200.0,
            value=float(existing.get("weight", 60.0)),
            step=0.1
        )

    st.write("")

    with st.container(border=True):

        st.markdown("### 🌿 LIFESTYLE")

        sleep = st.number_input(
            "😴 Sleep (hours)",
            min_value=0.0,
            max_value=24.0,
            value=float(existing.get("sleep", 7.0)),
            step=0.1
        )

        water = st.selectbox(
            "💧 Water",
            ["0–2 cups", "3–4 cups", "5–6 cups", "7–8 cups", "9+ cups"],
            index=[
                "0–2 cups",
                "3–4 cups",
                "5–6 cups",
                "7–8 cups",
                "9+ cups"
            ].index(existing.get("water", "5–6 cups"))
        )

        meals = st.selectbox(
            "🍚 Meals",
            ["0 meals", "1 meal", "2 meals", "3 meals", "4+ meals"],
            index=[
                "0 meals",
                "1 meal",
                "2 meals",
                "3 meals",
                "4+ meals"
            ].index(existing.get("meals", "3 meals"))
        )

        healthy_food = st.selectbox(
            "🥗 Healthy Food",
            [
                "Not today",
                "A little",
                "Balanced meal"
            ],
            index=[
                "Not today",
                "A little",
                "Balanced meal"
            ].index(existing.get("healthy_food", "A little"))
        )

        exercise = st.selectbox(
            "🏃‍♀️ Exercise",
            [
                "None",
                "10–20 min",
                "20–40 min",
                "40+ min"
            ],
            index=[
                "None",
                "10–20 min",
                "20–40 min",
                "40+ min"
            ].index(existing.get("exercise", "None"))
        )

        pregnancy_learning = st.checkbox(
            "📚 I learned something about pregnancy today",
            value=bool(existing.get("pregnancy_learning", False))
        )

        baby_bonding = st.checkbox(
            "🎵 I spent a little time bonding with my baby",
            value=bool(existing.get("baby_bonding", False))
        )

    st.write("")

    with st.container(border=True):

        st.markdown("### 💕 FEELINGS")

        mood = st.selectbox(
            "😊 Mood",
            [
                "😄 Great",
                "🙂 Good",
                "😐 Okay",
                "😟 Worried",
                "😢 Low"
            ],
            index=[
                "😄 Great",
                "🙂 Good",
                "😐 Okay",
                "😟 Worried",
                "😢 Low"
            ].index(existing.get("mood", "🙂 Good"))
        )

        energy = st.selectbox(
            "⚡ Energy",
            [
                "⚡ High",
                "🙂 Normal",
                "🥱 Low"
            ],
            index=[
                "⚡ High",
                "🙂 Normal",
                "🥱 Low"
            ].index(existing.get("energy", "🙂 Normal"))
        )

        stress = st.slider(
            "😰 Stress",
            min_value=1,
            max_value=5,
            value=int(existing.get("stress", 2)),
            help="1 = very relaxed · 5 = very stressed"
        )

    st.write("")

    if st.button(
        "💾 SAVE TODAY'S CHECK",
        use_container_width=True
    ):

        st.session_state.health_records[date_key] = {
            "date": check_date,
            "weight": weight,
            "sleep": sleep,
            "water": water,
            "meals": meals,
            "healthy_food": healthy_food,
            "exercise": exercise,
            "pregnancy_learning": pregnancy_learning,
            "baby_bonding": baby_bonding,
            "mood": mood,
            "energy": energy,
            "stress": stress
        }

        st.success(
            f"Your health check for {check_date.strftime('%b %d, %Y')} has been saved! 🌷"
        )

    st.write("")

    if st.button(
        "❤️ VIEW HEALTH DASHBOARD",
        use_container_width=True
    ):

        st.session_state.page = "health_dashboard"

        st.rerun()

    st.write("")

    if st.button("← BACK TO TODAY"):

        st.session_state.page = "today"

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
# HEALTH DASHBOARD CHART COLORS
# ==========================================

SLEEP_COLOR = "#B8A1E3"
WATER_COLOR = "#8FD8C1"
EXERCISE_COLOR = "#F3A6B9"
WEIGHT_COLOR = "#AFA0E8"
MEALS_COLOR = "#F6C39A"
MOOD_COLOR = "#F29AC2"
ENERGY_COLOR = "#F4D77A"
STRESS_COLOR = "#E9A6A6"
LEARNING_COLOR = "#B8A1E3"
BONDING_COLOR = "#F29AC2"
HEALTHY_FOOD_COLOR = "#A8D5BA"


# ==========================================
# ❤️ HEALTH DASHBOARD
# ==========================================

def show_health_dashboard():

    st.markdown(
        '<div class="logo">✦ MOMI ✦</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        "# ❤️ Health Dashboard"
    )

    st.caption(
        "See how your daily health journey changes over time"
    )

    show_momi()

    st.write("")

    records = st.session_state.health_records

    if not records:

        with st.container(border=True):

            st.markdown(
                "### 🌱 Your health journey starts here"
            )

            st.write(
                "Complete your first Daily Health Check "
                "and your personal charts will appear here."
            )

        st.write("")

        if st.button(
            "📝 GO TO DAILY HEALTH CHECK",
            use_container_width=True
        ):

            st.session_state.page = "daily_health"

            st.rerun()

        st.write("")

        if st.button("← BACK TO HEALTH"):

            st.session_state.page = "health"

            st.rerun()

        return

    data = list(records.values())

    df = pd.DataFrame(data)

    df = df.sort_values("date")

    water_map = {
        "0–2 cups": 1,
        "3–4 cups": 3.5,
        "5–6 cups": 5.5,
        "7–8 cups": 7.5,
        "9+ cups": 9
    }

    meals_map = {
        "0 meals": 0,
        "1 meal": 1,
        "2 meals": 2,
        "3 meals": 3,
        "4+ meals": 4
    }

    exercise_map = {
        "None": 0,
        "10–20 min": 15,
        "20–40 min": 30,
        "40+ min": 45
    }

    healthy_food_map = {
        "Not today": 0,
        "A little": 1,
        "Balanced meal": 2
    }

    mood_map = {
        "😢 Low": 1,
        "😟 Worried": 2,
        "😐 Okay": 3,
        "🙂 Good": 4,
        "😄 Great": 5
    }

    energy_map = {
        "🥱 Low": 1,
        "🙂 Normal": 2,
        "⚡ High": 3
    }

    df["water_value"] = df["water"].map(water_map)
    df["meals_value"] = df["meals"].map(meals_map)
    df["exercise_value"] = df["exercise"].map(exercise_map)
    df["healthy_food_value"] = df["healthy_food"].map(healthy_food_map)
    df["mood_value"] = df["mood"].map(mood_map)
    df["energy_value"] = df["energy"].map(energy_map)

    df["learning_value"] = df["pregnancy_learning"].astype(int)
    df["bonding_value"] = df["baby_bonding"].astype(int)

    df["date_label"] = df["date"].apply(
        lambda x: x.strftime("%b %d")
    )

    with st.container(border=True):

        st.caption("🌷 YOUR HEALTH JOURNEY")

        st.markdown(
            f"### {len(df)} day(s) recorded"
        )

        st.write(
            "Keep checking in to see your personal trends grow."
        )

    st.write("")

    with st.container(border=True):

        st.markdown("### 😴 SLEEP")

        chart = (
            alt.Chart(df)
            .mark_line(
                point=True,
                strokeWidth=4
            )
            .encode(
                x=alt.X(
                    "date_label:N",
                    title="Date"
                ),
                y=alt.Y(
                    "sleep:Q",
                    title="Hours"
                ),
                tooltip=[
                    alt.Tooltip("date_label:N", title="Date"),
                    alt.Tooltip("sleep:Q", title="Sleep", format=".1f")
                ]
            )
            .encode(color=alt.value(SLEEP_COLOR))
            .properties(height=230)
        )

        st.altair_chart(
            chart,
            use_container_width=True
        )

    st.write("")

    with st.container(border=True):

        st.markdown("### 💧 WATER")

        chart = (
            alt.Chart(df)
            .mark_bar(
                cornerRadiusTopLeft=8,
                cornerRadiusTopRight=8
            )
            .encode(
                x=alt.X(
                    "date_label:N",
                    title="Date"
                ),
                y=alt.Y(
                    "water_value:Q",
                    title="Approx. cups"
                ),
                tooltip=[
                    alt.Tooltip("date_label:N", title="Date"),
                    alt.Tooltip("water:N", title="Water")
                ]
            )
            .encode(color=alt.value(WATER_COLOR))
            .properties(height=230)
        )

        st.altair_chart(
            chart,
            use_container_width=True
        )

    st.write("")

    with st.container(border=True):

        st.markdown("### 🏃‍♀️ EXERCISE")

        chart = (
            alt.Chart(df)
            .mark_bar(
                cornerRadiusTopLeft=8,
                cornerRadiusTopRight=8
            )
            .encode(
                x=alt.X(
                    "date_label:N",
                    title="Date"
                ),
                y=alt.Y(
                    "exercise_value:Q",
                    title="Minutes"
                ),
                tooltip=[
                    alt.Tooltip("date_label:N", title="Date"),
                    alt.Tooltip("exercise:N", title="Exercise")
                ]
            )
            .encode(color=alt.value(EXERCISE_COLOR))
            .properties(height=230)
        )

        st.altair_chart(
            chart,
            use_container_width=True
        )

    st.write("")

    with st.container(border=True):

        st.markdown("### ⚖️ WEIGHT")

        chart = (
            alt.Chart(df)
            .mark_line(
                point=True,
                strokeWidth=4
            )
            .encode(
                x=alt.X(
                    "date_label:N",
                    title="Date"
                ),
                y=alt.Y(
                    "weight:Q",
                    title="kg"
                ),
                tooltip=[
                    alt.Tooltip("date_label:N", title="Date"),
                    alt.Tooltip("weight:Q", title="Weight", format=".1f")
                ]
            )
            .encode(color=alt.value(WEIGHT_COLOR))
            .properties(height=230)
        )

        st.altair_chart(
            chart,
            use_container_width=True
        )

    st.write("")

    with st.container(border=True):

        st.markdown("### 🍚 MEALS")

        chart = (
            alt.Chart(df)
            .mark_bar(
                cornerRadiusTopLeft=8,
                cornerRadiusTopRight=8
            )
            .encode(
                x=alt.X(
                    "date_label:N",
                    title="Date"
                ),
                y=alt.Y(
                    "meals_value:Q",
                    title="Meals"
                ),
                tooltip=[
                    alt.Tooltip("date_label:N", title="Date"),
                    alt.Tooltip("meals:N", title="Meals")
                ]
            )
            .encode(color=alt.value(MEALS_COLOR))
            .properties(height=230)
        )

        st.altair_chart(
            chart,
            use_container_width=True
        )

    st.write("")

    with st.container(border=True):

        st.markdown("### 😊 MOOD")

        chart = (
            alt.Chart(df)
            .mark_line(
                point=True,
                strokeWidth=4
            )
            .encode(
                x=alt.X(
                    "date_label:N",
                    title="Date"
                ),
                y=alt.Y(
                    "mood_value:Q",
                    title="Mood",
                    scale=alt.Scale(domain=[1, 5])
                ),
                tooltip=[
                    alt.Tooltip("date_label:N", title="Date"),
                    alt.Tooltip("mood:N", title="Mood")
                ]
            )
            .encode(color=alt.value(MOOD_COLOR))
            .properties(height=230)
        )

        st.altair_chart(
            chart,
            use_container_width=True
        )

    st.write("")

    with st.container(border=True):

        st.markdown("### ⚡ ENERGY")

        chart = (
            alt.Chart(df)
            .mark_line(
                point=True,
                strokeWidth=4
            )
            .encode(
                x=alt.X(
                    "date_label:N",
                    title="Date"
                ),
                y=alt.Y(
                    "energy_value:Q",
                    title="Energy",
                    scale=alt.Scale(domain=[1, 3])
                ),
                tooltip=[
                    alt.Tooltip("date_label:N", title="Date"),
                    alt.Tooltip("energy:N", title="Energy")
                ]
            )
            .encode(color=alt.value(ENERGY_COLOR))
            .properties(height=230)
        )

        st.altair_chart(
            chart,
            use_container_width=True
        )

    st.write("")

    with st.container(border=True):

        st.markdown("### 😰 STRESS")

        chart = (
            alt.Chart(df)
            .mark_line(
                point=True,
                strokeWidth=4
            )
            .encode(
                x=alt.X(
                    "date_label:N",
                    title="Date"
                ),
                y=alt.Y(
                    "stress:Q",
                    title="Stress",
                    scale=alt.Scale(domain=[1, 5])
                ),
                tooltip=[
                    alt.Tooltip("date_label:N", title="Date"),
                    alt.Tooltip("stress:Q", title="Stress")
                ]
            )
            .encode(color=alt.value(STRESS_COLOR))
            .properties(height=230)
        )

        st.altair_chart(
            chart,
            use_container_width=True
        )

    st.write("")

    with st.container(border=True):

        st.markdown("### 📚 PREGNANCY LEARNING")

        learning_yes = int(df["pregnancy_learning"].sum())
        learning_no = len(df) - learning_yes

        learning_df = pd.DataFrame({
            "status": ["Learned", "Not yet"],
            "count": [learning_yes, learning_no]
        })

        chart = (
            alt.Chart(learning_df)
            .mark_arc(
                innerRadius=55
            )
            .encode(
                theta="count:Q",
                color=alt.Color(
                    "status:N",
                    scale=alt.Scale(
                        range=[LEARNING_COLOR, "#E8DFFF"]
                    )
                ),
                tooltip=[
                    alt.Tooltip("status:N", title="Status"),
                    alt.Tooltip("count:Q", title="Days")
                ]
            )
            .properties(height=250)
        )

        st.altair_chart(
            chart,
            use_container_width=True
        )

    st.write("")

    with st.container(border=True):

        st.markdown("### 🎵 BABY BONDING")

        bonding_yes = int(df["baby_bonding"].sum())
        bonding_no = len(df) - bonding_yes

        bonding_df = pd.DataFrame({
            "status": ["Bonding", "Not yet"],
            "count": [bonding_yes, bonding_no]
        })

        chart = (
            alt.Chart(bonding_df)
            .mark_arc(
                innerRadius=55
            )
            .encode(
                theta="count:Q",
                color=alt.Color(
                    "status:N",
                    scale=alt.Scale(
                        range=[BONDING_COLOR, "#FFE5F0"]
                    )
                ),
                tooltip=[
                    alt.Tooltip("status:N", title="Status"),
                    alt.Tooltip("count:Q", title="Days")
                ]
            )
            .properties(height=250)
        )

        st.altair_chart(
            chart,
            use_container_width=True
        )

    st.write("")

    with st.container(border=True):

        st.markdown("### 🥗 HEALTHY FOOD")

        chart = (
            alt.Chart(df)
            .mark_bar(
                cornerRadiusTopLeft=8,
                cornerRadiusTopRight=8
            )
            .encode(
                x=alt.X(
                    "date_label:N",
                    title="Date"
                ),
                y=alt.Y(
                    "healthy_food_value:Q",
                    title="Balanced food",
                    scale=alt.Scale(domain=[0, 2])
                ),
                tooltip=[
                    alt.Tooltip("date_label:N", title="Date"),
                    alt.Tooltip("healthy_food:N", title="Food")
                ]
            )
            .encode(color=alt.value(HEALTHY_FOOD_COLOR))
            .properties(height=230)
        )

        st.altair_chart(
            chart,
            use_container_width=True
        )

    st.write("")

    with st.container(border=True):

        st.markdown("### 🌷 RECENT RECORDS")

        display_df = df[
            [
                "date",
                "weight",
                "sleep",
                "water",
                "meals",
                "exercise",
                "mood",
                "energy",
                "stress"
            ]
        ].copy()

        display_df["date"] = display_df["date"].apply(
            lambda x: x.strftime("%b %d, %Y")
        )

        display_df.columns = [
            "Date",
            "Weight",
            "Sleep",
            "Water",
            "Meals",
            "Exercise",
            "Mood",
            "Energy",
            "Stress"
        ]

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )

    st.write("")

    if st.button(
        "📝 ADD / EDIT DAILY CHECK",
        use_container_width=True
    ):

        st.session_state.page = "daily_health"

        st.rerun()

    st.write("")

    if st.button("← BACK TO HEALTH"):

        st.session_state.page = "health"

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

    st.markdown(
        "### 🌸 SELECT WEEK"
    )

    st.write("")

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
# 선택한 주차의 실제 내용
# ==========================================

def show_milestone_content(week):

    data = milestones[week]

    with st.container(border=True):

        st.caption("🍼 BABY GROWTH")

        st.write(
            data["baby"]
        )

    st.write("")

    with st.container(border=True):

        st.caption("🌸 MOM'S CARE")

        st.write(
            data["mom"]
        )

    st.write("")

    with st.container(border=True):

        st.caption("✦ MOMI'S MESSAGE")

        st.write(
            data["message"]
        )


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

    show_milestone_content(week)

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
# AI CONSULTATION
# CLICK-BASED CONVERSATIONAL CHATBOT
# ==========================================

def ai_add_message(role, text):

    st.session_state.ai_messages.append({
        "role": role,
        "text": text
    })


def ai_start_conversation():

    if not st.session_state.ai_messages:

        mom_name = st.session_state.mom_name.strip()

        if mom_name:
            greeting = (
                f"Hi {mom_name}! 💗\n\n"
                "I'm here to help you explore your pregnancy journey.\n\n"
                "What would you like to know today?"
            )
        else:
            greeting = (
                "Hi! 💗\n\n"
                "I'm here to help you explore your pregnancy journey.\n\n"
                "What would you like to know today?"
            )

        ai_add_message("momi", greeting)

        st.session_state.ai_current_menu = "main"
        st.session_state.ai_menu_history = []


def ai_show_message(role, text):

    if role == "user":

        with st.container(border=True):
            st.caption("YOU")
            st.write(text)

    else:

        with st.container(border=True):
            st.caption("✦ MOMI")
            st.write(text)


def ai_go_to_menu(menu_name):

    current_menu = st.session_state.ai_current_menu

    if current_menu != menu_name:
        st.session_state.ai_menu_history.append(current_menu)

    st.session_state.ai_current_menu = menu_name


def ai_add_user_and_momi(user_text, momi_text, next_menu):

    ai_add_message("user", user_text)
    ai_add_message("momi", momi_text)

    st.session_state.ai_current_menu = next_menu


def ai_back():

    if st.session_state.ai_menu_history:

        previous_menu = st.session_state.ai_menu_history.pop()
        st.session_state.ai_current_menu = previous_menu

    else:

        st.session_state.ai_current_menu = "main"


def ai_current_week_message():

    week = int(st.session_state.pregnancy_week)

    data = milestones.get(week)

    if data:

        return (
            f"You're currently at Week {week}! 💗\n\n"
            f"This is a special stage in your pregnancy journey. "
            f"Your baby's development is continuing week by week.\n\n"
            f"{data['baby']}"
        )

    return (
        f"You're currently at Week {week}! 💗\n\n"
        "Your pregnancy journey is continuing one week at a time."
    )


def ai_milestone_message():

    week = int(st.session_state.pregnancy_week)

    data = milestones.get(week)

    if not data:
        return (
            f"I couldn't find milestone information for Week {week}."
        )

    return (
        f"Here's your Week {week} milestone, based on the same "
        "weekly information used in your Milestone section. 🌸\n\n"
        f"🍼 Baby Growth\n"
        f"{data['baby']}\n\n"
        f"🌸 Mom's Care\n"
        f"{data['mom']}\n\n"
        f"✦ MOMI's Message\n"
        f"{data['message']}"
    )


def ai_due_date_message():

    due_date = st.session_state.due_date

    return (
        f"Your current due date is {due_date.strftime('%B %d, %Y')}! 🎀\n\n"
        "This is the due date already saved in your MOMI profile. "
        "Your healthcare provider can give you the most accurate guidance "
        "about how your pregnancy timeline may change."
    )


def ai_next_hospital_message():

    upcoming = get_upcoming_appointments()

    if not upcoming:

        return (
            "You don't have an upcoming hospital appointment saved yet. 🏥\n\n"
            "You can book one through Hospital → Appointments, "
            "and I'll be able to show it here afterward."
        )

    appointment = upcoming[0]

    appointment_date = datetime.strptime(
        appointment["date"],
        "%Y-%m-%d"
    ).date()

    message = (
        "Here is your next upcoming hospital visit. 🏥\n\n"
        f"🏥 Hospital: {appointment['hospital']}\n\n"
        f"👨‍⚕️ Doctor: {appointment['doctor']}\n\n"
        f"📅 Date: {appointment_date.strftime('%B %d, %Y')}\n\n"
        f"⏰ Time: {appointment['time']}"
    )

    if "specialty" in appointment:
        message += (
            f"\n\n🩺 Specialty: {appointment['specialty']}"
        )

    return message


def ai_doctor_message():

    upcoming = get_upcoming_appointments()

    if upcoming:

        appointment = upcoming[0]

        message = (
            f"Your doctor on your next saved appointment is "
            f"{appointment['doctor']}. 👨‍⚕️\n\n"
            f"Hospital: {appointment['hospital']}"
        )

        if "specialty" in appointment:
            message += (
                f"\n\nSpecialty: {appointment['specialty']}"
            )

        return message

    selected_hospital = st.session_state.hospital_selected_hospital
    selected_doctor = st.session_state.hospital_selected_doctor

    if (
        selected_hospital is not None
        and selected_doctor is not None
        and selected_hospital in st.session_state.hospital_data
    ):

        doctors = st.session_state.hospital_data[selected_hospital]

        if selected_doctor < len(doctors):

            doctor = doctors[selected_doctor]

            return (
                f"Your currently selected doctor is "
                f"{doctor['name']}. 👨‍⚕️\n\n"
                f"Hospital: {selected_hospital}\n\n"
                f"Specialty: {doctor['specialty']}"
            )

    return (
        "You don't have a doctor connected to an upcoming appointment yet. 👨‍⚕️\n\n"
        "You can choose a hospital and doctor through Hospital → Appointments."
    )


def ai_baby_topic_message(topic):

    answers = {

        "brain":
            "Your baby's brain and nervous system continue developing throughout pregnancy. "
            "During this stage, nerve connections become more organized and help support "
            "movement and other body functions. 💗",

        "heart":
            "Your baby's heart develops early and continues growing throughout pregnancy. "
            "As pregnancy progresses, the heart becomes more developed and works as part "
            "of your baby's growing circulatory system. 🫀",

        "senses":
            "Your baby's sensory systems continue developing during pregnancy. "
            "The structures involved in hearing, vision, and other senses gradually mature "
            "as your baby prepares to experience the world outside the womb. 👂",

        "bones":
            "Your baby's bones, muscles, and joints continue developing throughout pregnancy. "
            "As these structures mature, your baby can make increasingly coordinated movements. 🦴",

        "lungs":
            "Your baby's lungs develop gradually throughout pregnancy. "
            "The airways and other lung structures continue maturing, while breathing-like "
            "movements help prepare the body for breathing after birth. 🌬️"
    }

    return answers[topic]


def ai_food_topic_message(topic):

    answers = {

        "eat":
            "A balanced pregnancy diet can include vegetables, fruits, whole grains, "
            "protein foods, and calcium-rich foods. Try to build meals around a variety "
            "of foods rather than focusing on one perfect meal. 🍎",

        "nutrients":
            "Important nutrients during pregnancy include folate, iron, calcium, protein, "
            "and other vitamins and minerals. A varied diet can help provide many of these, "
            "while your healthcare provider can advise you about any prenatal supplements. 🥬",

        "iron":
            "Iron-rich foods include lean meat, beans, lentils, leafy greens, eggs, and "
            "fortified grains. Including a variety of these foods can help support your "
            "body's increased nutritional needs during pregnancy. 🥩",

        "calcium":
            "Calcium supports normal bone development and your own bone health. "
            "Milk, yogurt, cheese, tofu, and fortified alternatives can be useful calcium-rich "
            "choices. Vitamin D also helps your body absorb calcium. 🥛",

        "fish":
            "Fish can provide protein and omega-3 fatty acids that are useful in a balanced "
            "pregnancy diet. Choose pregnancy-safe fish according to local guidance and "
            "avoid fish known to be high in mercury. 🐟",

        "caffeine":
            "During pregnancy, it is generally recommended to keep caffeine intake limited. "
            "Coffee, tea, energy drinks, chocolate, and some medicines can contain caffeine, "
            "so checking your total daily intake can be helpful. ☕",

        "hydration":
            "Regular hydration is important during pregnancy. Water is a simple everyday choice, "
            "and foods such as fruit, vegetables, soups, and yogurt can also contribute to fluid intake. 💧"
    }

    return answers[topic]


def ai_health_topic_message(topic):

    answers = {

        "sleep":
            "Pregnancy can change your sleep routine, so a comfortable and consistent bedtime "
            "routine can help. Give yourself enough time to rest and adjust your position or "
            "pillows for comfort as your body changes. 😴",

        "activity":
            "If your healthcare provider has not given you activity restrictions, gentle movement "
            "such as walking can be a comfortable way to stay active. Listen to your body and "
            "avoid pushing through pain or unusual discomfort. 🚶",

        "stress":
            "Pregnancy can bring many emotions. Slow breathing, quiet music, a short walk, "
            "gentle stretching, journaling, or talking with someone you trust can create a "
            "little space to relax. 🧘",

        "changes":
            "Pregnancy can bring many normal body changes, including changes in energy, appetite, "
            "sleep, digestion, and body shape. Every pregnancy is different, so questions about "
            "new or concerning symptoms are best discussed with your healthcare provider. 🤰",

        "hydration":
            "Keeping water nearby and drinking regularly can make hydration easier. "
            "Your fluid needs can vary with activity, weather, and your individual situation, "
            "so follow any specific guidance from your healthcare provider. 💧",

        "selfcare":
            "Pregnancy self-care can be simple: regular meals, enough rest, comfortable movement, "
            "hydration, and moments that help you feel calm. You do not need to make every day perfect "
            "to take good care of yourself. 🌸"
    }

    return answers[topic]


def ai_show_choices():

    menu = st.session_state.ai_current_menu

    # ==========================================
    # MAIN MENU
    # ==========================================

    if menu == "main":

        st.markdown("### What would you like to explore?")

        if st.button(
            "1. 👶 Baby & Pregnancy",
            use_container_width=True,
            key="ai_main_baby"
        ):

            ai_add_user_and_momi(
                "👶 Baby & Pregnancy",
                "Of course! What would you like to know about your baby? 💗",
                "baby"
            )

            st.rerun()

        if st.button(
            "2. 🥗 Food & Nutrition",
            use_container_width=True,
            key="ai_main_food"
        ):

            ai_add_user_and_momi(
                "🥗 Food & Nutrition",
                "Let's talk about food and nutrition! 🥗\n\nWhat would you like to know?",
                "food"
            )

            st.rerun()

        if st.button(
            "3. 💗 Mom's Health",
            use_container_width=True,
            key="ai_main_health"
        ):

            ai_add_user_and_momi(
                "💗 Mom's Health",
                "Let's take care of you, too. 💗\n\nWhat would you like to explore?",
                "health"
            )

            st.rerun()

        if st.button(
            "4. 📅 My Pregnancy",
            use_container_width=True,
            key="ai_main_pregnancy"
        ):

            ai_add_user_and_momi(
                "📅 My Pregnancy",
                "Let's look at your pregnancy information together. 💗\n\nWhat would you like to check?",
                "pregnancy"
            )

            st.rerun()

        return

    # ==========================================
    # BABY MENU
    # ==========================================

    if menu == "baby":

        st.markdown("### Choose a topic about your baby")

        if st.button(
            "1. 🌱 Baby's Development This Week",
            use_container_width=True,
            key="ai_baby_week"
        ):

            ai_add_user_and_momi(
                "🌱 Baby's Development This Week",
                ai_milestone_message(),
                "baby_after"
            )

            st.rerun()

        if st.button(
            "2. 🧠 Brain & Nervous System",
            use_container_width=True,
            key="ai_baby_brain"
        ):

            ai_add_user_and_momi(
                "🧠 Brain & Nervous System",
                ai_baby_topic_message("brain"),
                "baby_after"
            )

            st.rerun()

        if st.button(
            "3. 🫀 Heart Development",
            use_container_width=True,
            key="ai_baby_heart"
        ):

            ai_add_user_and_momi(
                "🫀 Heart Development",
                ai_baby_topic_message("heart"),
                "baby_after"
            )

            st.rerun()

        if st.button(
            "4. 👂 Senses & Hearing",
            use_container_width=True,
            key="ai_baby_senses"
        ):

            ai_add_user_and_momi(
                "👂 Senses & Hearing",
                ai_baby_topic_message("senses"),
                "baby_after"
            )

            st.rerun()

        if st.button(
            "5. 🦴 Bones & Muscles",
            use_container_width=True,
            key="ai_baby_bones"
        ):

            ai_add_user_and_momi(
                "🦴 Bones & Muscles",
                ai_baby_topic_message("bones"),
                "baby_after"
            )

            st.rerun()

        if st.button(
            "6. 🌬️ Lungs & Breathing",
            use_container_width=True,
            key="ai_baby_lungs"
        ):

            ai_add_user_and_momi(
                "🌬️ Lungs & Breathing",
                ai_baby_topic_message("lungs"),
                "baby_after"
            )

            st.rerun()

        return

    # ==========================================
    # BABY AFTER ANSWER
    # ==========================================

    if menu == "baby_after":

        st.markdown("### What would you like to explore next?")

        if st.button(
            "🫀 Heart Development",
            use_container_width=True,
            key="ai_baby_after_heart"
        ):

            ai_add_user_and_momi(
                "🫀 Heart Development",
                ai_baby_topic_message("heart"),
                "baby_after"
            )

            st.rerun()

        if st.button(
            "👂 Senses & Hearing",
            use_container_width=True,
            key="ai_baby_after_senses"
        ):

            ai_add_user_and_momi(
                "👂 Senses & Hearing",
                ai_baby_topic_message("senses"),
                "baby_after"
            )

            st.rerun()

        if st.button(
            "🌱 This Week's Development",
            use_container_width=True,
            key="ai_baby_after_week"
        ):

            ai_add_user_and_momi(
                "🌱 This Week's Development",
                ai_milestone_message(),
                "baby_after"
            )

            st.rerun()

        if st.button(
            "🏠 Main Menu",
            use_container_width=True,
            key="ai_baby_after_main"
        ):

            ai_add_user_and_momi(
                "🏠 Main Menu",
                "Of course! What would you like to explore next?",
                "main"
            )

            st.rerun()

        return

    # ==========================================
    # FOOD MENU
    # ==========================================

    if menu == "food":

        st.markdown("### Choose a nutrition topic")

        if st.button(
            "1. 🍎 What Should I Eat?",
            use_container_width=True,
            key="ai_food_eat"
        ):

            ai_add_user_and_momi(
                "🍎 What Should I Eat?",
                ai_food_topic_message("eat"),
                "food_after"
            )

            st.rerun()

        if st.button(
            "2. 🥬 Important Nutrients",
            use_container_width=True,
            key="ai_food_nutrients"
        ):

            ai_add_user_and_momi(
                "🥬 Important Nutrients",
                ai_food_topic_message("nutrients"),
                "food_after"
            )

            st.rerun()

        if st.button(
            "3. 🥩 Iron-Rich Foods",
            use_container_width=True,
            key="ai_food_iron"
        ):

            ai_add_user_and_momi(
                "🥩 Iron-Rich Foods",
                ai_food_topic_message("iron"),
                "food_after"
            )

            st.rerun()

        if st.button(
            "4. 🥛 Calcium & Vitamin D",
            use_container_width=True,
            key="ai_food_calcium"
        ):

            ai_add_user_and_momi(
                "🥛 Calcium & Vitamin D",
                ai_food_topic_message("calcium"),
                "food_after"
            )

            st.rerun()

        if st.button(
            "5. 🐟 Fish & Pregnancy",
            use_container_width=True,
            key="ai_food_fish"
        ):

            ai_add_user_and_momi(
                "🐟 Fish & Pregnancy",
                ai_food_topic_message("fish"),
                "food_after"
            )

            st.rerun()

        if st.button(
            "6. ☕ Caffeine",
            use_container_width=True,
            key="ai_food_caffeine"
        ):

            ai_add_user_and_momi(
                "☕ Caffeine",
                ai_food_topic_message("caffeine"),
                "food_after"
            )

            st.rerun()

        if st.button(
            "7. 💧 Hydration",
            use_container_width=True,
            key="ai_food_hydration"
        ):

            ai_add_user_and_momi(
                "💧 Hydration",
                ai_food_topic_message("hydration"),
                "food_after"
            )

            st.rerun()

        return

    # ==========================================
    # FOOD AFTER ANSWER
    # ==========================================

    if menu == "food_after":

        st.markdown("### What would you like to explore next?")

        if st.button(
            "🥬 Important Nutrients",
            use_container_width=True,
            key="ai_food_after_nutrients"
        ):

            ai_add_user_and_momi(
                "🥬 Important Nutrients",
                ai_food_topic_message("nutrients"),
                "food_after"
            )

            st.rerun()

        if st.button(
            "🥩 Iron-Rich Foods",
            use_container_width=True,
            key="ai_food_after_iron"
        ):

            ai_add_user_and_momi(
                "🥩 Iron-Rich Foods",
                ai_food_topic_message("iron"),
                "food_after"
            )

            st.rerun()

        if st.button(
            "🐟 Fish & Pregnancy",
            use_container_width=True,
            key="ai_food_after_fish"
        ):

            ai_add_user_and_momi(
                "🐟 Fish & Pregnancy",
                ai_food_topic_message("fish"),
                "food_after"
            )

            st.rerun()

        if st.button(
            "☕ Caffeine",
            use_container_width=True,
            key="ai_food_after_caffeine"
        ):

            ai_add_user_and_momi(
                "☕ Caffeine",
                ai_food_topic_message("caffeine"),
                "food_after"
            )

            st.rerun()

        if st.button(
            "🏠 Main Menu",
            use_container_width=True,
            key="ai_food_after_main"
        ):

            ai_add_user_and_momi(
                "🏠 Main Menu",
                "Of course! What would you like to explore next?",
                "main"
            )

            st.rerun()

        return

    # ==========================================
    # MOM'S HEALTH MENU
    # ==========================================

    if menu == "health":

        st.markdown("### Choose a health topic")

        if st.button(
            "1. 😴 Sleep",
            use_container_width=True,
            key="ai_health_sleep"
        ):

            ai_add_user_and_momi(
                "😴 Sleep",
                ai_health_topic_message("sleep"),
                "health_after"
            )

            st.rerun()

        if st.button(
            "2. 🚶 Light Activity",
            use_container_width=True,
            key="ai_health_activity"
        ):

            ai_add_user_and_momi(
                "🚶 Light Activity",
                ai_health_topic_message("activity"),
                "health_after"
            )

            st.rerun()

        if st.button(
            "3. 🧘 Relaxation & Stress",
            use_container_width=True,
            key="ai_health_stress"
        ):

            ai_add_user_and_momi(
                "🧘 Relaxation & Stress",
                ai_health_topic_message("stress"),
                "health_after"
            )

            st.rerun()

        if st.button(
            "4. 🤰 Common Body Changes",
            use_container_width=True,
            key="ai_health_changes"
        ):

            ai_add_user_and_momi(
                "🤰 Common Body Changes",
                ai_health_topic_message("changes"),
                "health_after"
            )

            st.rerun()

        if st.button(
            "5. 💧 Hydration",
            use_container_width=True,
            key="ai_health_hydration"
        ):

            ai_add_user_and_momi(
                "💧 Hydration",
                ai_health_topic_message("hydration"),
                "health_after"
            )

            st.rerun()

        if st.button(
            "6. 🌸 Pregnancy Self-Care",
            use_container_width=True,
            key="ai_health_selfcare"
        ):

            ai_add_user_and_momi(
                "🌸 Pregnancy Self-Care",
                ai_health_topic_message("selfcare"),
                "health_after"
            )

            st.rerun()

        return

    # ==========================================
    # HEALTH AFTER ANSWER
    # ==========================================

    if menu == "health_after":

        st.markdown("### What would you like to explore next?")

        if st.button(
            "😴 Sleep",
            use_container_width=True,
            key="ai_health_after_sleep"
        ):

            ai_add_user_and_momi(
                "😴 Sleep",
                ai_health_topic_message("sleep"),
                "health_after"
            )

            st.rerun()

        if st.button(
            "🚶 Light Activity",
            use_container_width=True,
            key="ai_health_after_activity"
        ):

            ai_add_user_and_momi(
                "🚶 Light Activity",
                ai_health_topic_message("activity"),
                "health_after"
            )

            st.rerun()

        if st.button(
            "🧘 Relaxation & Stress",
            use_container_width=True,
            key="ai_health_after_stress"
        ):

            ai_add_user_and_momi(
                "🧘 Relaxation & Stress",
                ai_health_topic_message("stress"),
                "health_after"
            )

            st.rerun()

        if st.button(
            "🌸 Pregnancy Self-Care",
            use_container_width=True,
            key="ai_health_after_selfcare"
        ):

            ai_add_user_and_momi(
                "🌸 Pregnancy Self-Care",
                ai_health_topic_message("selfcare"),
                "health_after"
            )

            st.rerun()

        if st.button(
            "🏠 Main Menu",
            use_container_width=True,
            key="ai_health_after_main"
        ):

            ai_add_user_and_momi(
                "🏠 Main Menu",
                "Of course! What would you like to explore next?",
                "main"
            )

            st.rerun()

        return

    # ==========================================
    # MY PREGNANCY MENU
    # ==========================================

    if menu == "pregnancy":

        st.markdown("### Explore your pregnancy information")

        if st.button(
            "1. 📖 My Current Week",
            use_container_width=True,
            key="ai_pregnancy_week"
        ):

            ai_add_user_and_momi(
                "📖 My Current Week",
                ai_current_week_message(),
                "pregnancy_after"
            )

            st.rerun()

        if st.button(
            "2. 🌸 This Week's Milestone",
            use_container_width=True,
            key="ai_pregnancy_milestone"
        ):

            ai_add_user_and_momi(
                "🌸 This Week's Milestone",
                ai_milestone_message(),
                "pregnancy_after"
            )

            st.rerun()

        if st.button(
            "3. 📅 My Due Date",
            use_container_width=True,
            key="ai_pregnancy_due"
        ):

            ai_add_user_and_momi(
                "📅 My Due Date",
                ai_due_date_message(),
                "pregnancy_after"
            )

            st.rerun()

        if st.button(
            "4. 🏥 My Next Hospital Visit",
            use_container_width=True,
            key="ai_pregnancy_hospital"
        ):

            ai_add_user_and_momi(
                "🏥 My Next Hospital Visit",
                ai_next_hospital_message(),
                "pregnancy_after"
            )

            st.rerun()

        if st.button(
            "5. 👨‍⚕️ My Doctor",
            use_container_width=True,
            key="ai_pregnancy_doctor"
        ):

            ai_add_user_and_momi(
                "👨‍⚕️ My Doctor",
                ai_doctor_message(),
                "pregnancy_after"
            )

            st.rerun()

        return

    # ==========================================
    # PREGNANCY AFTER ANSWER
    # ==========================================

    if menu == "pregnancy_after":

        st.markdown("### What would you like to check next?")

        if st.button(
            "📖 My Current Week",
            use_container_width=True,
            key="ai_pregnancy_after_week"
        ):

            ai_add_user_and_momi(
                "📖 My Current Week",
                ai_current_week_message(),
                "pregnancy_after"
            )

            st.rerun()

        if st.button(
            "🌸 This Week's Milestone",
            use_container_width=True,
            key="ai_pregnancy_after_milestone"
        ):

            ai_add_user_and_momi(
                "🌸 This Week's Milestone",
                ai_milestone_message(),
                "pregnancy_after"
            )

            st.rerun()

        if st.button(
            "📅 My Due Date",
            use_container_width=True,
            key="ai_pregnancy_after_due"
        ):

            ai_add_user_and_momi(
                "📅 My Due Date",
                ai_due_date_message(),
                "pregnancy_after"
            )

            st.rerun()

        if st.button(
            "🏥 My Next Hospital Visit",
            use_container_width=True,
            key="ai_pregnancy_after_hospital"
        ):

            ai_add_user_and_momi(
                "🏥 My Next Hospital Visit",
                ai_next_hospital_message(),
                "pregnancy_after"
            )

            st.rerun()

        if st.button(
            "👨‍⚕️ My Doctor",
            use_container_width=True,
            key="ai_pregnancy_after_doctor"
        ):

            ai_add_user_and_momi(
                "👨‍⚕️ My Doctor",
                ai_doctor_message(),
                "pregnancy_after"
            )

            st.rerun()

        if st.button(
            "🏠 Main Menu",
            use_container_width=True,
            key="ai_pregnancy_after_main"
        ):

            ai_add_user_and_momi(
                "🏠 Main Menu",
                "Of course! What would you like to explore next?",
                "main"
            )

            st.rerun()


def show_ai_consultation():

    ai_start_conversation()

    st.markdown(
        '<div class="logo">✦ MOMI ✦</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        "# 🤖 AI Consultation"
    )

    st.caption(
        "Talk to MOMI through guided choices"
    )

    show_momi()

    st.write("")

    # ------------------------------------------
    # CHAT HISTORY
    # ------------------------------------------

    for message in st.session_state.ai_messages:

        ai_show_message(
            message["role"],
            message["text"]
        )

        st.write("")

    # ------------------------------------------
    # CURRENT CHOICES
    # ------------------------------------------

    ai_show_choices()

    st.write("")

    # ------------------------------------------
    # NAVIGATION
    # ------------------------------------------

    if st.session_state.ai_current_menu != "main":

        if st.button(
            "↩ Back",
            use_container_width=True,
            key="ai_back_button"
        ):

            ai_add_message(
                "user",
                "↩ Back"
            )

            ai_back()

            ai_add_message(
                "momi",
                "Sure! Let's go back. 💗"
            )

            st.rerun()

    st.write("")

    if st.session_state.ai_current_menu != "main":

        if st.button(
            "🏠 Main Menu",
            use_container_width=True,
            key="ai_main_menu_bottom"
        ):

            ai_add_message(
                "user",
                "🏠 Main Menu"
            )

            ai_add_message(
                "momi",
                "Of course! What would you like to explore next?"
            )

            st.session_state.ai_menu_history = []
            st.session_state.ai_current_menu = "main"

            st.rerun()

    st.write("")

    if st.button(
        "🔄 Start Over",
        use_container_width=True,
        key="ai_start_over"
    ):

        st.session_state.ai_messages = []
        st.session_state.ai_current_menu = "main"
        st.session_state.ai_menu_history = []

        st.rerun()

    st.write("")

    if st.button(
        "← BACK TO AI",
        use_container_width=True,
        key="ai_back_to_ai"
    ):

        st.session_state.page = "ai"

        st.rerun()


# ==========================================
# HOSPITAL
# ==========================================

def hospital_card(title, lines):

    with st.container(border=True):
        st.markdown(f"### {title}")
        for line in lines:
            st.write(line)


def get_upcoming_appointments():

    today = date.today()
    upcoming = []

    for appointment in st.session_state.appointments:
        appointment_date = datetime.strptime(
            appointment["date"], "%Y-%m-%d"
        ).date()

        if appointment_date >= today:
            upcoming.append(appointment)

    upcoming.sort(
        key=lambda item: (
            item["date"],
            item["time"]
        )
    )

    return upcoming


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

    upcoming = get_upcoming_appointments()

    if upcoming:
        next_visit = upcoming[0]

        with st.container(border=True):
            st.caption("🏥 NEXT VISIT")
            st.markdown(f"### {next_visit['hospital']}")
            st.write(f"👨‍⚕️ {next_visit['doctor']}")
            st.write(
                f"📅 {datetime.strptime(next_visit['date'], '%Y-%m-%d').strftime('%B %d, %Y')}"
            )
            st.write(f"⏰ {next_visit['time']}")

    st.write("")

    if st.button("← BACK TO HOME"):

        st.session_state.page = "home"

        st.rerun()


def show_appointments():

    st.markdown(
        '<div class="logo">✦ MOMI ✦</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        "# 📋 Appointments"
    )

    st.caption(
        "Book and manage your hospital appointments"
    )

    show_momi()

    st.write("")

    upcoming = get_upcoming_appointments()

    if upcoming:
        with st.container(border=True):
            st.caption("YOUR UPCOMING APPOINTMENTS")

            for index, appointment in enumerate(upcoming):
                appointment_date = datetime.strptime(
                    appointment["date"], "%Y-%m-%d"
                ).date()

                st.markdown(f"### 🏥 {appointment['hospital']}")
                st.write(f"👨‍⚕️ {appointment['doctor']}")
                st.write(
                    f"📅 {appointment_date.strftime('%B %d, %Y')} · ⏰ {appointment['time']}"
                )

                if st.button(
                    "Cancel Appointment",
                    key=f"cancel_appointment_{index}",
                    use_container_width=True
                ):
                    st.session_state.appointments.remove(appointment)
                    st.rerun()

                if index < len(upcoming) - 1:
                    st.write("")

        st.write("")

    st.markdown("### 1. SELECT HOSPITAL")

    if st.session_state.hospital_selected_hospital is None:

        hospitals = list(st.session_state.hospital_data.keys())

        for row in range(0, len(hospitals), 2):
            col1, col2 = st.columns(2)

            for col, hospital_index in zip(
                [col1, col2],
                range(row, min(row + 2, len(hospitals)))
            ):
                hospital = hospitals[hospital_index]

                with col:
                    if st.button(
                        f"🏥 {hospital}",
                        key=f"hospital_select_{hospital_index}",
                        use_container_width=True
                    ):
                        st.session_state.hospital_selected_hospital = hospital
                        st.session_state.hospital_selected_doctor = None
                        st.session_state.hospital_selected_date = None
                        st.session_state.hospital_selected_time = None
                        st.rerun()

    else:

        selected_hospital = st.session_state.hospital_selected_hospital

        with st.container(border=True):
            st.caption("SELECTED HOSPITAL")
            st.markdown(f"### 🏥 {selected_hospital}")

        st.write("")

        if st.button("↩ CHANGE HOSPITAL", use_container_width=True):
            st.session_state.hospital_selected_hospital = None
            st.session_state.hospital_selected_doctor = None
            st.session_state.hospital_selected_date = None
            st.session_state.hospital_selected_time = None
            st.rerun()

        st.write("")

        st.markdown("### 2. SELECT DOCTOR")

        if st.session_state.hospital_selected_doctor is None:

            doctors = st.session_state.hospital_data[selected_hospital]

            for doctor_index, doctor in enumerate(doctors):
                with st.container(border=True):
                    st.markdown(f"### 👨‍⚕️ {doctor['name']}")
                    st.caption(doctor["specialty"])

                    if st.button(
                        "VIEW AVAILABLE TIMES",
                        key=f"doctor_select_{doctor_index}",
                        use_container_width=True
                    ):
                        st.session_state.hospital_selected_doctor = doctor_index
                        st.session_state.hospital_selected_date = None
                        st.session_state.hospital_selected_time = None
                        st.rerun()

                st.write("")

        else:

            doctor_index = st.session_state.hospital_selected_doctor
            doctor = st.session_state.hospital_data[selected_hospital][doctor_index]

            with st.container(border=True):
                st.caption("SELECTED DOCTOR")
                st.markdown(f"### 👨‍⚕️ {doctor['name']}")
                st.write(doctor["specialty"])

            st.write("")

            if st.button("↩ CHANGE DOCTOR", use_container_width=True):
                st.session_state.hospital_selected_doctor = None
                st.session_state.hospital_selected_date = None
                st.session_state.hospital_selected_time = None
                st.rerun()

            st.write("")

            st.markdown("### 3. SELECT DATE")

            doctor_dates = sorted(doctor["schedule"].keys())

            date_columns = st.columns(3)

            for date_index, date_key in enumerate(doctor_dates):
                available_date = datetime.strptime(
                    date_key, "%Y-%m-%d"
                ).date()

                with date_columns[date_index % 3]:
                    if st.button(
                        available_date.strftime("%b %d"),
                        key=f"appointment_date_{date_index}",
                        use_container_width=True
                    ):
                        st.session_state.hospital_selected_date = date_key
                        st.session_state.hospital_selected_time = None
                        st.rerun()

            if st.session_state.hospital_selected_date is not None:

                selected_date = st.session_state.hospital_selected_date

                st.write("")

                st.markdown("### 4. SELECT TIME")

                selected_date_object = datetime.strptime(
                    selected_date, "%Y-%m-%d"
                ).date()

                st.caption(
                    selected_date_object.strftime("%B %d, %Y")
                )

                times = doctor["schedule"][selected_date]
                time_columns = st.columns(3)

                for time_index, available_time in enumerate(times):
                    with time_columns[time_index % 3]:
                        if st.button(
                            available_time,
                            key=f"appointment_time_{time_index}",
                            use_container_width=True
                        ):
                            st.session_state.hospital_selected_time = available_time
                            st.rerun()

                if st.session_state.hospital_selected_time is not None:

                    selected_time = st.session_state.hospital_selected_time

                    st.write("")

                    with st.container(border=True):
                        st.caption("APPOINTMENT SUMMARY")
                        st.markdown(f"### 🏥 {selected_hospital}")
                        st.write(f"👨‍⚕️ {doctor['name']}")
                        st.write(
                            f"📅 {selected_date_object.strftime('%B %d, %Y')}"
                        )
                        st.write(f"⏰ {selected_time}")
                        st.caption(doctor["specialty"])

                    st.write("")

                    if st.button(
                        "✓ CONFIRM APPOINTMENT",
                        use_container_width=True
                    ):

                        new_appointment = {
                            "hospital": selected_hospital,
                            "doctor": doctor["name"],
                            "specialty": doctor["specialty"],
                            "date": selected_date,
                            "time": selected_time
                        }

                        duplicate = any(
                            item["hospital"] == new_appointment["hospital"]
                            and item["doctor"] == new_appointment["doctor"]
                            and item["date"] == new_appointment["date"]
                            and item["time"] == new_appointment["time"]
                            for item in st.session_state.appointments
                        )

                        if not duplicate:
                            st.session_state.appointments.append(
                                new_appointment
                            )

                        st.session_state.hospital_selected_hospital = None
                        st.session_state.hospital_selected_doctor = None
                        st.session_state.hospital_selected_date = None
                        st.session_state.hospital_selected_time = None
                        st.session_state.page = "next_hospital"
                        st.rerun()

    st.write("")

    if st.button("← BACK TO HOSPITAL", use_container_width=True):
        st.session_state.page = "hospital"
        st.rerun()


def show_schedule():

    st.markdown(
        '<div class="logo">✦ MOMI ✦</div>',
        unsafe_allow_html=True
    )

    st.markdown("# 📅 Schedule")
    st.caption("See your hospital visits and personal plans at a glance")

    show_momi()

    st.write("")

    current_month = st.session_state.schedule_month
    year = current_month.year
    month = current_month.month

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("←", key="schedule_prev_month", use_container_width=True):
            if month == 1:
                st.session_state.schedule_month = date(year - 1, 12, 1)
            else:
                st.session_state.schedule_month = date(year, month - 1, 1)
            st.rerun()

    with col2:
        st.markdown(
            f"### {current_month.strftime('%B %Y')}",
            unsafe_allow_html=True
        )

    with col3:
        if st.button("→", key="schedule_next_month", use_container_width=True):
            if month == 12:
                st.session_state.schedule_month = date(year + 1, 1, 1)
            else:
                st.session_state.schedule_month = date(year, month + 1, 1)
            st.rerun()

    st.write("")

    calendar_matrix = calendar.monthcalendar(year, month)
    weekday_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    weekday_columns = st.columns(7)
    for index, weekday in enumerate(weekday_names):
        with weekday_columns[index]:
            st.caption(weekday)

    for week_row, week_dates in enumerate(calendar_matrix):
        day_columns = st.columns(7)

        for day_index, day_number in enumerate(week_dates):
            with day_columns[day_index]:
                if day_number == 0:
                    st.write("")
                else:
                    calendar_date = date(year, month, day_number)
                    date_key = calendar_date.isoformat()

                    appointment_here = [
                        item for item in st.session_state.appointments
                        if item["date"] == date_key
                    ]

                    personal_here = st.session_state.personal_schedules.get(
                        date_key, []
                    )

                    marker = ""
                    if appointment_here:
                        marker += "🏥"
                    if personal_here:
                        marker += "✦"

                    label = f"{day_number}"
                    if marker:
                        label += f"\n{marker}"

                    if st.button(
                        label,
                        key=f"calendar_day_{year}_{month}_{day_number}",
                        use_container_width=True
                    ):
                        st.session_state.schedule_selected_date = calendar_date
                        st.rerun()

    selected_date = st.session_state.schedule_selected_date

    st.write("")

    with st.container(border=True):
        st.caption("SELECTED DATE")
        st.markdown(
            f"### {selected_date.strftime('%B %d, %Y')}"
        )

    st.write("")

    selected_key = selected_date.isoformat()

    appointments_today = [
        item for item in st.session_state.appointments
        if item["date"] == selected_key
    ]

    if appointments_today:
        st.markdown("### 🏥 HOSPITAL APPOINTMENTS")

        for appointment in appointments_today:
            with st.container(border=True):
                st.caption("AUTOMATIC APPOINTMENT")
                st.markdown(f"### {appointment['hospital']}")
                st.write(f"👨‍⚕️ {appointment['doctor']}")
                st.write(f"⏰ {appointment['time']}")
                st.caption(appointment["specialty"])

        st.write("")

    personal_today = st.session_state.personal_schedules.get(
        selected_key, []
    )

    if personal_today:
        st.markdown("### ✏️ PERSONAL SCHEDULE")

        for item_index, item in enumerate(personal_today):
            with st.container(border=True):
                st.caption("PERSONAL SCHEDULE")
                st.markdown(f"### {item['title']}")
                st.write(f"⏰ {item['time']}")
                if item["note"]:
                    st.write(item["note"])

                if st.button(
                    "Delete",
                    key=f"delete_personal_{selected_key}_{item_index}",
                    use_container_width=True
                ):
                    personal_today.pop(item_index)
                    if not personal_today:
                        del st.session_state.personal_schedules[selected_key]
                    st.rerun()

        st.write("")

    st.markdown("### ✏️ ADD PERSONAL SCHEDULE")

    with st.container(border=True):
        schedule_title = st.text_input(
            "Title",
            placeholder="e.g. Prenatal Yoga",
            key="new_schedule_title"
        )

        schedule_time = st.text_input(
            "Time",
            placeholder="e.g. 19:00",
            key="new_schedule_time"
        )

        schedule_note = st.text_input(
            "Note",
            placeholder="Add a short note",
            key="new_schedule_note"
        )

        if st.button(
            "＋ SAVE SCHEDULE",
            use_container_width=True
        ):
            if schedule_title.strip():
                if selected_key not in st.session_state.personal_schedules:
                    st.session_state.personal_schedules[selected_key] = []

                st.session_state.personal_schedules[selected_key].append({
                    "title": schedule_title.strip(),
                    "time": schedule_time.strip() or "All day",
                    "note": schedule_note.strip()
                })

                st.rerun()
            else:
                st.warning("Please enter a title for your schedule.")

    st.write("")

    if st.button("← BACK TO HOSPITAL", use_container_width=True):
        st.session_state.page = "hospital"
        st.rerun()


def show_next_hospital_visit():

    st.markdown(
        '<div class="logo">✦ MOMI ✦</div>',
        unsafe_allow_html=True
    )

    st.markdown("# 🏥 Next Hospital Visit")
    st.caption("Your next hospital visit and appointment details")

    show_momi()

    st.write("")

    upcoming = get_upcoming_appointments()

    if not upcoming:

        with st.container(border=True):
            st.caption("NEXT VISIT")
            st.markdown("### No upcoming hospital visits")
            st.write(
                "Book an appointment to see your next visit here."
            )

        st.write("")

        if st.button(
            "📋 BOOK AN APPOINTMENT",
            use_container_width=True
        ):
            st.session_state.page = "hospital_appointments"
            st.rerun()

    else:

        appointment = upcoming[0]
        appointment_date = datetime.strptime(
            appointment["date"], "%Y-%m-%d"
        ).date()

        with st.container(border=True):
            st.caption("🏥 NEXT VISIT")
            st.markdown(f"# {appointment['hospital']}")
            st.write("")
            st.markdown(f"### 👨‍⚕️ {appointment['doctor']}")
            st.caption(appointment["specialty"])
            st.write("")
            st.markdown(
                f"### 📅 {appointment_date.strftime('%B %d, %Y')}"
            )
            st.markdown(f"### ⏰ {appointment['time']}")

        st.write("")

        with st.container(border=True):
            st.caption("🎒 THINGS YOU MAY WANT TO BRING")
            st.write("✓ ID Card")
            st.write("✓ Maternity Record Book")
            st.write("✓ Medical Documents")
            st.write("✓ Insurance Card")
            st.write("✓ Previous Test Results")

        st.write("")

        if st.button(
            "📋 VIEW APPOINTMENT",
            use_container_width=True
        ):
            st.session_state.page = "hospital_appointments"
            st.rerun()

    st.write("")

    if st.button("← BACK TO TODAY", use_container_width=True):
        st.session_state.page = "today"
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

    show_daily_health()


elif st.session_state.page == "weekly_milestone":

    show_milestone_week()


elif st.session_state.page == "next_hospital":

    show_next_hospital_visit()


# ==========================================
# HEALTH
# ==========================================

elif st.session_state.page == "health":

    show_health()


elif st.session_state.page == "health_dashboard":

    show_health_dashboard()


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

    show_ai_consultation()


# ==========================================
# HOSPITAL
# ==========================================

elif st.session_state.page == "hospital":

    show_hospital()


elif st.session_state.page == "hospital_schedule":

    show_schedule()


elif st.session_state.page == "hospital_appointments":

    show_appointments()


elif st.session_state.page == "hospital_messages":

    show_empty_page(
        "💌 Hospital Messages",
        "Check your hospital messages"
    )