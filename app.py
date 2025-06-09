import streamlit as st
import random
# 제목  
# 포켓몬 선택 게임
# Streamlit 앱 시작

st.title("⚡ 포켓몬 선택 게임 ⚡")
st.write("어떤 포켓몬을 선택할까요?")

col1, col2, col3 = st.columns(3)

with col1:
    # GitHub에 올린 이미지 사용
    st.image("images/picachu.png", width=150)
    if st.button("⚡ 피카츄"):
        st.write("피카츄를 선택했어요!")
        st.write("전기 공격! ⚡⚡⚡")
        st.balloons()

with col2:
    # GitHub에 올린 이미지 사용
    st.image("images/charmander.png", width=150)
    if st.button("🔥 파이리"):
        st.write("파이리를 선택했어요!")
        st.write("불꽃 공격! 🔥🔥🔥")
        st.balloons()

with col3:
    # GitHub에 올린 이미지 사용
    st.image("images/squirtle.png", width=150)
    if st.button("💧 꼬부기"):
        st.write("꼬부기를 선택했어요!")
        st.write("물 공격! 💧💧💧")
        st.balloons()

# 구분선
st.write("---")

# 더 멋진 버전 - 정보까지!
st.title("🌟 포켓몬 정보 게임 🌟")

# 포켓몬 정보 데이터
pokemon_info = {
    "피카츄": {"타입": "전기", "공격": "10만볼트", "이모지": "⚡"},
    "파이리": {"타입": "불꽃", "공격": "화염방사", "이모지": "🔥"},
    "꼬부기": {"타입": "물", "공격": "하이드로펌프", "이모지": "💧"}
}

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/picachu.png", width=120)
    if st.button("⚡ 피카츄", key="pika"):
        info = pokemon_info["피카츄"]
        st.success("피카츄 선택!")
        st.write(f"타입: {info['타입']}")
        st.write(f"공격: {info['공격']}")
        st.write(f"{info['이모지'] * 5}")
        st.toast("피카츄를 선택했어요!", icon="⚡")

with col2:
    st.image("images/charmander.png", width=120)
    if st.button("🔥 파이리", key="char"):
        info = pokemon_info["파이리"]
        st.success("파이리 선택!")
        st.write(f"타입: {info['타입']}")
        st.write(f"공격: {info['공격']}")
        st.write(f"{info['이모지'] * 5}")
        st.toast("파이리를 선택했어요!", icon="🔥")

with col3:
    st.image("images/squirtle.png", width=120)
    if st.button("💧 꼬부기", key="squi"):
        info = pokemon_info["꼬부기"]
        st.success("꼬부기 선택!")
        st.write(f"타입: {info['타입']}")
        st.write(f"공격: {info['공격']}")
        st.write(f"{info['이모지'] * 5}")
        st.toast("꼬부기를 선택했어요!", icon="💧")
        
# 구분선
st.write("---") 
st.write("---")
st.title("⚔️ 랜덤 포켓몬 배틀 ⚔️")

# 포켓몬 공격력 정보
attack_power = {
    "피카츄": 55,
    "파이리": 50,
    "꼬부기": 53
}

if st.button("배틀 시작!"):
    my_pokemon = random.choice(list(pokemon_info.keys()))
    enemy_pokemon = random.choice(list(pokemon_info.keys()))

    st.write(f"🎮 내가 선택한 포켓몬: **{my_pokemon}** {pokemon_info[my_pokemon]['이모지']}")
    st.write(f"👾 상대 포켓몬: **{enemy_pokemon}** {pokemon_info[enemy_pokemon]['이모지']}")

    my_power = attack_power[my_pokemon]
    enemy_power = attack_power[enemy_pokemon]

    st.progress(min(my_power, 100))
    st.progress(min(enemy_power, 100))

    if my_power > enemy_power:
        st.success(f"{my_pokemon} 승리! 🏆")
        st.balloons()
    elif my_power < enemy_power:
        st.error(f"{enemy_pokemon} 승리! 😱")
        st.snow()
    else:
        st.info("무승부! 다시 도전해보세요 🎲")