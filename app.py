import streamlit as st
import random

# 🎵 배경음악 삽입 (경로는 로컬 기준 또는 GitHub raw URL로 바꿔도 가능)
st.audio("music/battle_theme.mp3", format="audio/mp3", start_time=0)

# 포켓몬 정보
pokemon_info = {
    "피카츄": {"타입": "전기", "공격": "10만볼트", "이모지": "⚡"},
    "파이리": {"타입": "불꽃", "공격": "화염방사", "이모지": "🔥"},
    "꼬부기": {"타입": "물", "공격": "하이드로펌프", "이모지": "💧"}
}

# 이미지 경로 정의
pokemon_images = {
    "피카츄": "images/picachu.png",
    "파이리": "images/charmander.png",
    "꼬부기": "images/squirtle.png"
}

# -------------------------
# ⚡ 포켓몬 선택 게임 화면
# -------------------------
st.title("⚡ 포켓몬 선택 게임 ⚡")
st.write("어떤 포켓몬을 선택할까요?")

col1, col2, col3 = st.columns(3)
with col1:
    st.image(pokemon_images["피카츄"], width=150)
    if st.button("⚡ 피카츄"):
        st.write("피카츄를 선택했어요!")
        st.write("전기 공격! ⚡⚡⚡")
        st.balloons()

with col2:
    st.image(pokemon_images["파이리"], width=150)
    if st.button("🔥 파이리"):
        st.write("파이리를 선택했어요!")
        st.write("불꽃 공격! 🔥🔥🔥")
        st.balloons()

with col3:
    st.image(pokemon_images["꼬부기"], width=150)
    if st.button("💧 꼬부기"):
        st.write("꼬부기를 선택했어요!")
        st.write("물 공격! 💧💧💧")
        st.balloons()

# -------------------------
# 🌟 포켓몬 정보 게임
# -------------------------
st.write("---")
st.title("🌟 포켓몬 정보 게임 🌟")

col1, col2, col3 = st.columns(3)
with col1:
    st.image(pokemon_images["피카츄"], width=120)
    if st.button("⚡ 피카츄", key="pika"):
        info = pokemon_info["피카츄"]
        st.success("피카츄 선택!")
        st.write(f"타입: {info['타입']}")
        st.write(f"공격: {info['공격']}")
        st.write(f"{info['이모지'] * 5}")
        st.toast("피카츄를 선택했어요!", icon="⚡")

with col2:
    st.image(pokemon_images["파이리"], width=120)
    if st.button("🔥 파이리", key="char"):
        info = pokemon_info["파이리"]
        st.success("파이리 선택!")
        st.write(f"타입: {info['타입']}")
        st.write(f"공격: {info['공격']}")
        st.write(f"{info['이모지'] * 5}")
        st.toast("파이리를 선택했어요!", icon="🔥")

with col3:
    st.image(pokemon_images["꼬부기"], width=120)
    if st.button("💧 꼬부기", key="squi"):
        info = pokemon_info["꼬부기"]
        st.success("꼬부기 선택!")
        st.write(f"타입: {info['타입']}")
        st.write(f"공격: {info['공격']}")
        st.write(f"{info['이모지'] * 5}")
        st.toast("꼬부기를 선택했어요!", icon="💧")

# -------------------------
# ⚔️ 내가 선택한 포켓몬 배틀
# -------------------------
st.write("---")
st.title("⚔️ 내가 선택한 포켓몬 배틀 ⚔️")

pokemon_names = list(pokemon_info.keys())
attack_power = {
    "피카츄": 55,
    "파이리": 50,
    "꼬부기": 53
}

# 1. 내 포켓몬 선택
my_choice = st.selectbox("내가 고를 포켓몬은?", pokemon_names)

# 2. 상대 포켓몬 무작위 선택
enemy_choice = random.choice(pokemon_names)

# 3. 배틀 시작!
if st.button("🔥 배틀 시작!"):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎮 내 포켓몬")
        st.image(pokemon_images[my_choice], width=150)
        st.write(f"**{my_choice}** {pokemon_info[my_choice]['이모지']}")

    with col2:
        st.subheader("👾 상대 포켓몬")
        st.image(pokemon_images[enemy_choice], width=150)
        st.write(f"**{enemy_choice}** {pokemon_info[enemy_choice]['이모지']}")

    my_power = attack_power[my_choice]
    enemy_power = attack_power[enemy_choice]

    st.write("⚔️ 공격력 비교")
    st.progress(my_power)
    st.progress(enemy_power)

    if my_power > enemy_power:
        st.success(f"{my_choice} 승리! 🏆")
        st.balloons()
    elif my_power < enemy_power:
        st.error(f"{enemy_choice} 승리! 😱")
        st.snow()
    else:
        st.info("무승부! 다시 도전해보세요 🎲")
