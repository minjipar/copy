
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Fighting Designer", layout="centered")

st.title("🧠 Fighting Designer")
st.markdown("제품명과 특징을 입력하면, 톤에 맞는 카피를 자동으로 만들어줘요!")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

product = st.text_input("📦 제품명", placeholder="예: 촉촉한 착붙쿠션")
features = [st.text_input(f"✨ 특징 {i+1}", key=f"feature_{i}") for i in range(3)]

tone = st.selectbox("🎙️ 카피 스타일을 선택하세요", [
    "이커머스톤",
    "29CM톤",
    "배민톤",
    "광고카피톤",
    "자연주의톤"
])

if st.button("✨ 카피 생성하기"):
    prompt = f"""제품명: {product}
특징: {', '.join([f for f in features if f])}
카피 스타일: {tone}
→ 이 제품을 매력적으로 보이게 할 수 있는 마케팅 카피 3개 써줘. 한국어로 짧고 인상적으로!"""

    with st.spinner("카피 생성 중..."):
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a witty Korean copywriter who creates marketing copy for products based on input."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        result = response.choices[0].message.content
        for line in result.split("\n"):
            if line.strip():
                st.success(line.strip())
