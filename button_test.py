import streamlit as st

# 버튼 테스트 앱
st.title("재미있는 반응들")

if st.button("풍선"):
    st.balloons()
    st.write("풍선이 올라갔어요!")

if st.button("눈"):
    st.snow()
    st.write("눈이 내리고 있어요!")

if st.button("축하"):
    st.success("축하합니다!")   

if st.button("경고"):
    st.warning("조심하세요!")

if st.button("오류"):
    st.error("오류가 발생했습니다!")

st.title("버튼 3형제")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("😀 기쁨"):
        st.write("기뻐요!")
        st.balloons()  # 기쁠 때는 풍선!

with col2:
    if st.button("😢 슬픔"):
        st.write("슬퍼요!")
        st.info("괜찮아요, 힘내세요! 💪")

with col3:
    if st.button("😮 놀람"):
        st.write("놀라워요!")
        st.snow()  # 놀랄 때는 눈!