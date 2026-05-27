import streamlit as st
import pandas as pd
import joblib

# 1. 웹앱 제목 및 설명
st.title("🌱 스마트팜 착과율 예측 앱")
st.write("내부온도, 내부습도, 지온을 입력하면 예상 착과율을 예측해줍니다.")

# 2. 모델 로드 함수 
@st.cache_resource  
def load_my_model():
    # ⚠️ 실제 저장하신 랜덤포레스트 모델 파일명으로 변경해주세요! (예: rf_model.pkl 등)
    return joblib.load("tomato_model.pkl") 

try:
    rf_model = load_my_model()
except FileNotFoundError:
    st.error("🚨 모델 파일('rf_model.pkl')을 찾을 수 없습니다. 파일이 스크립트와 같은 폴더에 있는지 확인해주세요.")
    rf_model = None

st.divider() # 구분선

# 3. 사용자 입력 받기 (수치 입력 컴포넌트)
st.subheader("📊 환경 데이터 입력")

col1, col2, col3 = st.columns(3)

with col1:
    temp = st.number_input("내부온도 (°C)", min_value=-10.0, max_value=50.0, value=25.0, step=0.1)
with col2:
    humidity = st.number_input("내부습도 (%)", min_value=0.0, max_value=100.0, value=60.0, step=0.1)
with col3:
    soil_temp = st.number_input("지온 (°C)", min_value=-10.0, max_value=50.0, value=20.0, step=0.1)

st.divider()

# 4. 예측 버튼 및 결과 출력
if st.button("착과율 예측하기", type="primary"):
    if rf_model is not None:
        # 요청하신 DataFrame 변환 방식 적용
        # ⚠️ 만약 모델 학습 시 영문명으로 학습했다면 columns=['temp', 'humidity', 'soil_temp'] 형태로 맞춰야 합니다.
        input_data = pd.DataFrame([[temp, humidity, soil_temp]], columns=['내부온도', '내부습도', '지온'])
        
        # 예측 진행
        predicted = rf_model.predict(input_data)
        
        # 결과 시각화
        st.balloons() # 축하 풍선 효과 🎉
        st.success(f"🔮 예측 착과율 : **{predicted[0]:.1f}%**")