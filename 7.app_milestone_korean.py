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

# 선택한 주차를 저장
# Select Week와 Weekly Milestone에서 같은 주차를 사용하기 위해 필요
if "selected_week" not in st.session_state:
    st.session_state.selected_week = 18


# ==========================================
# MILESTONE DATA
# 1~40주
# ==========================================

milestones = {

    1: {
        "baby": "아직 아기가 형성되는 단계 전으로, 몸은 새로운 주기를 준비해요. 임신 주수는 마지막 생리 시작일부터 계산하기 때문에 이 시기의 실제 수정 여부와 주차가 정확히 일치하지 않을 수 있어요.",
        "mom": "엽산이 포함된 임신 준비용 영양제를 챙기고, 채소·과일·통곡물처럼 다양한 식품을 골고루 먹어보세요. 규칙적인 수면과 가벼운 산책으로 몸을 편안하게 준비해요.",
        "message": "새로운 여정의 첫 장이에요. 천천히 시작해도 충분해요 🌷"
    },

    2: {
        "baby": "배란을 전후로 임신이 시작될 가능성이 있는 시기예요. 아직 아기의 장기와 신체기관이 만들어진 단계는 아니며, 임신 주수는 마지막 생리 시작일을 기준으로 계산해요.",
        "mom": "엽산을 꾸준히 섭취하고 술·담배는 피하는 것이 좋아요. 몸이 보내는 변화에 귀 기울이며 충분한 수분과 균형 잡힌 식사를 챙겨보세요.",
        "message": "아직 작고 보이지 않아도 새로운 시작은 이미 준비되고 있어요 ✦"
    },

    3: {
        "baby": "수정이 이루어진 경우 세포가 빠르게 나뉘며 초기 배아를 형성해요. 여러 세포가 이동하면서 앞으로 아기의 몸과 태반을 이루는 구조로 나뉘기 시작해요.",
        "mom": "엽산이 풍부한 채소와 콩류, 과일을 식사에 넣어보세요. 카페인과 복용 중인 약이 있다면 임신 가능성이 있는 시기에 적절한지 의료진과 확인하는 것이 좋아요.",
        "message": "작은 세포에서 놀라운 변화가 시작되고 있어요 💕"
    },

    4: {
        "baby": "배아가 자궁 안쪽에 자리 잡는 과정이 진행될 수 있어요. 이후 아기의 몸으로 발달할 세포와 태반을 형성하는 세포가 구분되기 시작해요.",
        "mom": "임신을 확인했다면 산전 진료 일정을 알아보세요. 채소·과일·단백질 식품을 골고루 먹고, 무리하지 않는 가벼운 움직임을 유지해요.",
        "message": "작은 생명이 머물 자리를 찾아가는 특별한 시기예요 🌸"
    },

    5: {
        "baby": "뇌와 척수로 이어지는 신경계의 기초가 만들어지기 시작하고 심장과 소화기관의 초기 구조도 발달해요. 주요 신체기관이 형성되기 시작하는 중요한 시기예요.",
        "mom": "엽산은 신경관 발달과 관련된 중요한 영양소예요. 잎채소·콩류·통곡물 등을 식사에 활용하고, 입덧이 있다면 한 번에 많이 먹기보다 조금씩 나누어 먹어보세요.",
        "message": "아기의 첫 번째 기관들이 하나씩 자리를 잡고 있어요 🌱"
    },

    6: {
        "baby": "뇌의 여러 영역이 구분되기 시작하고 심장은 규칙적인 박동을 보이기 시작해요. 눈과 귀의 초기 구조, 팔과 다리의 싹도 나타나요.",
        "mom": "속이 불편하다면 크래커나 바나나처럼 부담이 적은 음식을 조금씩 먹어보세요. 수분을 자주 보충하고 충분히 쉬면서 몸의 변화를 기록해두면 좋아요.",
        "message": "작은 심장과 신경계가 바쁘게 발달하고 있어요 💗"
    },

    7: {
        "baby": "뇌와 얼굴의 구조가 더욱 뚜렷해지고 눈과 귀가 계속 발달해요. 척추와 뼈가 될 조직도 만들어지면서 몸의 기본 틀이 잡혀가요.",
        "mom": "단백질이 들어 있는 달걀·두부·콩·살코기 등을 식사에 골고루 넣어보세요. 컨디션이 괜찮다면 짧은 산책으로 몸을 가볍게 움직여도 좋아요.",
        "message": "아기의 얼굴과 몸의 윤곽이 조금씩 선명해지고 있어요 🌷"
    },

    8: {
        "baby": "팔과 다리가 조금 더 길어지고 손과 발의 기본 형태가 나타나요. 뇌는 빠르게 발달하고 폐의 초기 구조도 만들어지기 시작해요.",
        "mom": "신선한 채소와 과일을 다양하게 먹고 단백질 식품도 챙겨주세요. 잠들기 전 잔잔한 음악을 듣거나 아기에게 오늘 있었던 일을 이야기해보는 것도 좋아요.",
        "message": "작은 손과 발이 만들어지는 사랑스러운 시간이에요 🍼"
    },

    9: {
        "baby": "팔꿈치와 발가락이 점점 뚜렷해지고 손발의 움직임을 위한 근육과 관절이 발달해요. 대부분의 주요 기관이 형성되기 시작한 뒤 계속 성장하고 정교해지는 단계예요.",
        "mom": "철분이 들어 있는 살코기·콩·시금치 등을 식사에 활용해보세요. 과일이나 채소와 함께 먹으면 다양한 영양소를 골고루 챙기는 데 도움이 돼요.",
        "message": "아기의 기본적인 몸이 점점 사람다운 모습으로 변하고 있어요 ✨"
    },

    10: {
        "baby": "눈꺼풀과 바깥귀의 형태가 더 뚜렷해지고 얼굴의 윤곽도 발달해요. 소화기관의 구조가 계속 정리되며 이 시기부터 배아에서 태아 단계로 넘어가요.",
        "mom": "규칙적인 식사와 충분한 물을 챙겨주세요. 첫 산전 진료를 준비하고 복용 중인 약이나 영양제가 있다면 의료진에게 알려두는 것이 좋아요.",
        "message": "이제 작은 아기는 더욱 또렷한 모습을 만들어가고 있어요 🌸"
    },

    11: {
        "baby": "얼굴과 팔다리가 더 뚜렷해지고 손가락과 발가락의 형태가 구분돼요. 간과 혈액을 만드는 기능이 발달하고 치아가 될 조직도 준비되기 시작해요.",
        "mom": "철분과 단백질을 함께 챙길 수 있는 살코기, 달걀, 콩류를 활용해보세요. 입덧이 조금 줄었다면 여러 색깔의 채소와 과일을 식탁에 더해보세요.",
        "message": "작은 손가락과 발가락까지 조금씩 모습을 갖춰가고 있어요 🌷"
    },

    12: {
        "baby": "손가락과 발가락이 더욱 분명해지고 손을 쥐는 움직임도 가능해져요. 뇌와 신경계가 계속 발달하면서 몸의 움직임을 조절하는 기초가 만들어져요.",
        "mom": "칼슘이 들어 있는 우유·요거트·두부 등을 식사에 활용해보세요. 오늘 들은 음악이나 좋아하는 책을 잠시 즐기며 편안한 시간을 만들어보세요.",
        "message": "첫 번째 큰 구간을 지나고 있어요. 정말 잘하고 있어요 💕"
    },

    13: {
        "baby": "뼈와 근육이 계속 발달하면서 팔다리의 움직임이 더욱 자연스러워져요. 얼굴의 비율도 조금씩 변하고 몸 전체의 성장 속도가 빨라져요.",
        "mom": "단백질과 칼슘을 함께 챙길 수 있도록 두부, 달걀, 유제품 등을 골고루 먹어보세요. 몸이 허락한다면 가벼운 산책으로 기분을 전환해보세요.",
        "message": "아기의 몸이 더 튼튼한 형태로 자라나고 있어요 🌱"
    },

    14: {
        "baby": "얼굴과 목의 형태가 더 분명해지고 뼈와 근육의 발달이 이어져요. 신경계가 계속 성장하면서 다양한 움직임을 만들어낼 준비를 해요.",
        "mom": "통곡물과 채소, 과일을 식사에 넣어 식이섬유를 챙겨보세요. 산책하면서 천천히 주변 풍경을 바라보거나 아기에게 말을 걸어보는 것도 좋아요.",
        "message": "두 번째 여정으로 넘어가는 멋진 전환점이에요 🌸"
    },

    15: {
        "baby": "뼈가 점점 단단해지고 근육 조직이 발달하면서 팔과 다리의 움직임이 활발해져요. 피부는 아직 얇고 섬세한 상태로 계속 발달해요.",
        "mom": "칼슘과 단백질이 들어 있는 유제품·두부·생선·콩류 등을 골고루 먹어보세요. 편안한 음악을 들으며 배를 부드럽게 감싸는 시간도 가져보세요.",
        "message": "아기는 움직임을 연습하며 하루하루 더 단단해지고 있어요 ✦"
    },

    16: {
        "baby": "뼈와 관절, 근육이 계속 발달하면서 팔다리 움직임이 더욱 다양해져요. 얼굴 근육도 발달하면서 표정과 비슷한 움직임을 연습하기 시작해요.",
        "mom": "철분과 단백질이 포함된 식사를 꾸준히 챙겨주세요. 짧은 산책이나 가벼운 스트레칭으로 몸을 편안하게 하고 수분도 충분히 마셔요.",
        "message": "작은 몸이 열심히 움직임을 배우고 있어요 🍼"
    },

    17: {
        "baby": "뼈의 발달이 이어지고 지방 조직이 조금씩 생기기 시작해요. 청각을 담당하는 구조도 계속 발달하면서 소리를 받아들일 준비를 해요.",
        "mom": "오메가-3 지방산이 들어 있는 생선 등을 식단에 적절히 활용하고, 생선 선택과 섭취량은 임신 중 권장 기준을 확인해보세요. 좋아하는 음악을 편안하게 들어보세요.",
        "message": "아기는 몸뿐 아니라 감각을 위한 준비도 차근차근 하고 있어요 🎵"
    },

    18: {
        "baby": "신경계와 근육의 연결이 계속 발달하면서 아기의 움직임이 더욱 활발해져요. 귀의 구조도 발달해 소리를 받아들이는 능력이 점점 준비돼요.",
        "mom": "철분과 단백질을 함께 챙기고 채소와 과일도 다양하게 먹어보세요. 아기에게 오늘 있었던 일을 이야기하거나 책을 소리 내어 읽어주는 시간을 가져보세요.",
        "message": "아기와 엄마가 서로의 하루를 느껴가는 시간이에요 💗"
    },

    19: {
        "baby": "청각 발달이 이어지면서 외부의 소리를 받아들이는 준비가 진행돼요. 피부를 보호하는 얇은 물질과 잔털이 나타나며 피부 구조도 계속 발달해요.",
        "mom": "칼슘과 단백질을 충분히 챙기고 물도 자주 마셔주세요. 편안한 음악을 들으며 깊게 호흡하거나 가벼운 산책으로 몸을 움직여보세요.",
        "message": "이제 아기는 세상의 소리를 만날 준비를 하고 있어요 🎶"
    },

    20: {
        "baby": "아기의 몸이 계속 자라고 신경계와 감각기관이 발달해요. 삼키는 움직임과 근육 움직임도 조금씩 연습하면서 몸의 기능을 조율해가요.",
        "mom": "임신 중기 진료와 필요한 검사를 일정에 맞춰 확인해보세요. 철분·칼슘·단백질이 들어 있는 식사를 하고 무리하지 않는 활동을 이어가요.",
        "message": "여정의 절반을 향해 왔어요. 정말 잘하고 있어요 🌷"
    },

    21: {
        "baby": "청각이 계속 발달하면서 엄마의 목소리나 주변 소리를 들을 수 있는 능력이 자라요. 소화기관도 삼키는 연습을 하며 기능을 익혀가요.",
        "mom": "단백질이 풍부한 두부·달걀·콩류와 다양한 채소를 함께 먹어보세요. 하루에 잠깐이라도 아기에게 말을 걸거나 책을 읽어주는 시간을 만들어보세요.",
        "message": "엄마의 목소리가 아기에게 닿는 시간이 조금씩 늘고 있어요 💕"
    },

    22: {
        "baby": "눈썹과 속눈썹이 나타나고 손톱이 손가락 끝을 향해 자라요. 근육이 발달하면서 움직임이 더 활발해지고 장에서는 첫 배변을 위한 물질도 만들어져요.",
        "mom": "철분과 단백질을 챙기고 충분한 수분을 마셔주세요. 오래 앉아 있었다면 가볍게 몸을 풀고, 편안한 자세로 휴식하는 시간을 가져보세요.",
        "message": "작은 손톱과 눈썹까지 자라고 있어요. 신기하죠? 🌸"
    },

    23: {
        "baby": "골수에서 혈액을 만드는 기능이 발달하고 폐의 아래쪽 기도 구조도 계속 만들어져요. 피부 아래에 지방이 조금씩 저장되기 시작해요.",
        "mom": "철분이 들어 있는 살코기·콩·채소와 비타민이 다양한 과일을 함께 챙겨보세요. 잠들기 전 조용한 음악을 듣거나 아기에게 이야기를 들려주세요.",
        "message": "아기는 태어날 날을 향해 작은 기능들을 하나씩 연습하고 있어요 🌱"
    },

    24: {
        "baby": "폐의 기도와 공기주머니가 계속 발달하고 신경계도 빠르게 성장해요. 아직 폐는 충분히 성숙하지 않았지만 출생 후 호흡을 위한 구조를 준비하고 있어요.",
        "mom": "단백질과 철분을 포함한 균형 잡힌 식사를 유지하고 수분도 챙겨주세요. 무리하지 않는 산책과 가벼운 스트레칭으로 몸을 편안하게 관리해보세요.",
        "message": "작은 폐도 미래의 첫 호흡을 위해 열심히 준비하고 있어요 🫶"
    },

    25: {
        "baby": "폐의 작은 기도와 혈관 구조가 계속 발달하고 뼈와 근육도 성장해요. 몸에 지방이 조금씩 쌓이면서 피부의 모습도 서서히 변해가요.",
        "mom": "오메가-3 지방산과 단백질을 식품으로 적절히 섭취해보세요. 생선은 임신 중 섭취 권장 기준을 확인하고, 하루 중 편안한 시간에 책을 읽어주세요.",
        "message": "아기는 몸의 기능을 하나씩 완성해가는 중이에요 ✨"
    },

    26: {
        "baby": "눈의 구조가 잘 발달하고 눈썹과 속눈썹도 뚜렷해져요. 손가락과 발가락의 지문이 만들어지고 폐에서는 호흡에 필요한 구조가 계속 발달해요.",
        "mom": "칼슘과 단백질이 포함된 식사를 챙기고 채소와 과일도 다양하게 먹어보세요. 편안한 음악이나 엄마의 목소리를 들려주는 시간을 가져보세요.",
        "message": "작은 지문까지 만들어지는 놀라운 시기예요 🍼"
    },

    27: {
        "baby": "뇌가 빠르게 성장하고 신경계가 몸의 여러 기능을 조절할 수 있도록 발달해요. 눈꺼풀을 열고 닫을 수 있게 되며 폐도 계속 성숙해져요.",
        "mom": "철분과 단백질을 챙기면서 규칙적인 식사를 유지해보세요. 수면 시간을 일정하게 만들고 몸이 편안한 자세로 충분히 쉬어주세요.",
        "message": "아기의 뇌와 신경계가 정말 바쁘게 성장하고 있어요 🌷"
    },

    28: {
        "baby": "눈을 뜨고 감는 움직임이 가능해지고 뇌 발달이 더욱 활발해져요. 폐는 출생 후 호흡을 위해 필요한 물질을 만들기 시작하며 계속 성숙해요.",
        "mom": "임신 후기에 필요한 진료 일정과 검사 내용을 확인해보세요. 철분·칼슘·단백질을 균형 있게 챙기고 가벼운 활동과 충분한 휴식을 함께 유지해요.",
        "message": "세 번째 구간에 들어섰어요. 여기까지 정말 잘 왔어요 💗"
    },

    29: {
        "baby": "뇌와 신경계의 연결이 계속 복잡해지고 몸의 움직임도 더욱 조절돼요. 폐는 계속 성숙하면서 출생 후 호흡을 준비하는 단계에 들어가요.",
        "mom": "철분이 풍부한 살코기·콩류와 비타민이 다양한 채소를 함께 먹어보세요. 하루 중 몸이 가장 편안한 시간에 짧게 산책하거나 음악을 들어보세요.",
        "message": "아기는 태어날 세상을 향해 한 단계씩 준비하고 있어요 🌸"
    },

    30: {
        "baby": "뇌가 빠르게 성장하면서 몸의 움직임과 여러 기능을 조절하는 능력이 발달해요. 폐도 계속 성숙하고 눈의 움직임과 수면 리듬도 발달해요.",
        "mom": "단백질과 칼슘을 꾸준히 챙기고 수분 섭취도 잊지 마세요. 출산 후 필요한 물품을 조금씩 정리하면서 마음을 편안하게 준비해보세요.",
        "message": "이제 아기를 만날 날이 조금씩 가까워지고 있어요 ✦"
    },

    31: {
        "baby": "아기는 빠르게 체중을 늘리며 피하지방을 저장해요. 뼈는 계속 발달하지만 아직 완전히 단단하지 않고, 폐에서는 규칙적인 호흡 연습 움직임이 나타나요.",
        "mom": "철분·칼슘·단백질을 골고루 섭취하고 과일과 채소도 챙겨주세요. 오래 서 있거나 앉아 있기보다 중간중간 자세를 바꾸고 쉬어주세요.",
        "message": "아기는 포근한 몸을 만들며 출생을 준비하고 있어요 🍼"
    },

    32: {
        "baby": "뇌와 신경계가 계속 성숙하고 폐의 기능도 발전해요. 몸에 지방이 늘면서 피부가 점점 매끈한 모습으로 변해가요.",
        "mom": "칼슘이 들어 있는 유제품이나 두부와 단백질 식품을 식사에 넣어보세요. 아기에게 이야기하거나 함께 들을 음악을 골라보며 출산 전 시간을 즐겨보세요.",
        "message": "아기의 작은 몸이 점점 더 포근하고 튼튼해지고 있어요 🌷"
    },

    33: {
        "baby": "뇌와 신경계의 발달이 계속되고 폐도 출생 후 호흡을 위한 성숙 과정을 이어가요. 몸에 지방이 축적되면서 체온을 유지할 준비도 진행돼요.",
        "mom": "철분과 단백질을 챙기고 충분한 물을 마셔주세요. 병원 방문 일정과 출산 준비물을 확인하면서 필요한 것부터 천천히 준비해보세요.",
        "message": "이제 정말 마지막 준비가 시작되고 있어요. 천천히 준비해요 💕"
    },

    34: {
        "baby": "뼈와 근육은 계속 발달하고 몸에는 지방이 더 쌓여요. 폐의 성숙과 함께 규칙적인 호흡 연습 움직임이 이어지며 출생을 위한 준비가 진행돼요.",
        "mom": "다양한 단백질 식품과 채소를 챙기고 칼슘과 철분 섭취도 확인해보세요. 무리한 활동보다는 편안한 산책과 충분한 수면으로 몸을 돌봐주세요.",
        "message": "아기는 하루하루 세상 밖으로 나올 준비를 하고 있어요 🌸"
    },

    35: {
        "baby": "피부 아래 지방이 늘면서 피부가 전보다 덜 주름져 보여요. 심장과 혈관 구조는 완성 단계에 가까워지고 근육과 뼈도 충분히 발달해가요.",
        "mom": "단백질과 칼슘이 들어 있는 식사를 꾸준히 하고 물을 자주 마셔주세요. 출산 가방과 필요한 물품을 미리 확인해두면 마음이 한결 편해질 수 있어요.",
        "message": "아기의 몸이 점점 신생아의 모습에 가까워지고 있어요 🍼"
    },

    36: {
        "baby": "아기는 계속 체중을 늘리고 몸에 지방을 저장해요. 수면과 각성의 리듬도 점점 뚜렷해지고 출생 후 체온을 유지할 준비가 이어져요.",
        "mom": "철분·칼슘·단백질을 균형 있게 챙기고 과일과 채소도 충분히 먹어주세요. 산전 진료 일정을 확인하고 몸의 변화가 있을 때 기록해두세요.",
        "message": "이제 만날 준비가 거의 끝나가고 있어요. 조금만 더 함께 가요 🌷"
    },

    37: {
        "baby": "몸의 주요 기관이 출생에 필요한 기능을 갖추어가고 뇌와 폐도 계속 성숙해요. 피부 아래 지방이 늘면서 아기의 몸은 더욱 통통해져요.",
        "mom": "균형 잡힌 식사를 유지하고 물을 충분히 마셔주세요. 병원까지 이동 방법과 연락처, 출산 가방을 다시 한번 확인해두면 좋아요.",
        "message": "이제 정말 가까워졌어요. 엄마도 아기도 잘 준비하고 있어요 💗"
    },

    38: {
        "baby": "아기는 계속 지방을 저장하고 체중을 늘려요. 손톱은 손가락 끝을 넘어 자랄 수 있고 피부와 머리카락도 출생을 앞두고 계속 변화해요.",
        "mom": "소화가 편한 단백질과 채소, 과일 등을 골고루 먹고 수분을 챙겨주세요. 출산에 필요한 준비물을 가까운 곳에 정리하고 충분히 쉬어주세요.",
        "message": "아기를 만날 순간이 정말 가까워졌어요. 깊게 숨 쉬고 천천히 기다려요 🌸"
    },

    39: {
        "baby": "뇌와 신경계는 출생 후에도 계속 발달하지만 아기는 출생에 필요한 신체 기능을 더욱 안정적으로 준비하고 있어요. 피부 아래 지방도 계속 쌓여요.",
        "mom": "식사를 거르지 말고 물을 충분히 마시면서 몸을 편안하게 관리하세요. 병원에 갈 때 필요한 준비물과 연락 방법을 마지막으로 확인해보세요.",
        "message": "마지막 기다림의 시간이네요. 곧 서로를 만나게 될 거예요 🫶"
    },

    40: {
        "baby": "40주가 되면 아기는 출생을 기다리는 단계에 들어가요. 피부와 지방 조직이 발달하고 뇌와 폐도 출생 후 새로운 환경에 적응할 준비를 계속해요.",
        "mom": "균형 잡힌 식사와 충분한 수분을 유지하면서 몸을 편안하게 쉬게 해주세요. 예정된 산전 진료를 확인하고 출산 신호나 궁금한 변화가 있다면 의료진에게 상담하세요.",
        "message": "40주 동안 정말 잘 걸어왔어요. 이제 만남의 순간을 기다려요 💕"
    }
}


# ==========================================
# CSS
# 기존 CSS 그대로
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

        # 시작한 주차를 기본 선택 주차로 함께 저장
        st.session_state.selected_week = pregnancy_week

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

            # 현재 임신 주차를 milestone 주차로 사용
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
# 선택한 주차의 실제 내용
# ==========================================

def show_milestone_content(week):

    data = milestones[week]

    # Baby Growth
    with st.container(border=True):

        st.caption("🍼 BABY GROWTH")

        st.write(
            data["baby"]
        )


    st.write("")


    # Mom's Care
    with st.container(border=True):

        st.caption("🌸 MOM'S CARE")

        st.write(
            data["mom"]
        )


    st.write("")


    # MOMI's Message
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


    # ==========================================
    # 선택한 주차의 데이터 표시
    # ==========================================

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

    # TODAY의 Weekly Milestone은
    # 현재 pregnancy_week를 selected_week에 저장한 뒤
    # 같은 milestone 데이터를 사용
    show_milestone_week()


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