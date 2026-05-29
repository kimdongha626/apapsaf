import streamlit as st
import pandas as pd
import joblib

# 1. 웹앱 제목 및 설명

st.title("🌱 스마트팜 착과율 예측 앱")
st.write("내부온도, 내부습도, 지온을 입력하면 예상 착과율을 예측해줍니다.")

# 2. 모델 로드 함수

@st.cache_resource
def load_my_model():
return joblib.load("tomato_model.pkl")

try:
rf_model = load_my_model()
except FileNotFoundError:
st.error("🚨 모델 파일('tomato_model.pkl')을 찾을 수 없습니다.")
rf_model = None

st.divider()

# 3. 사용자 입력 받기

st.subheader("📊 환경 데이터 입력")

col1, col2, col3 = st.columns(3)

with col1:
temp = st.number_input("내부온도 (°C)", -10.0, 50.0, 25.0, 0.1)

with col2:
humidity = st.number_input("내부습도 (%)", 0.0, 100.0, 60.0, 0.1)

with col3:
soil_temp = st.number_input("지온 (°C)", -10.0, 50.0, 20.0, 0.1)

st.divider()

# 4. 예측

if st.button("착과율 예측하기", type="primary"):

```
if rf_model is not None:

    input_data = pd.DataFrame(
        [[temp, humidity, soil_temp]],
        columns=['내부온도', '내부습도', '지온']
    )

    predicted = rf_model.predict(input_data)

    st.balloons()

    st.success(
        f"🔮 예측 착과율 : {predicted[0]:.1f}%"
    )
```
