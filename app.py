import streamlit as st

st.set_page_config(
    page_title="BMI & TDEE 計算系統",
    page_icon="💪",
    layout="centered"
)

st.markdown(
    """
    <style>
    .main {background-color: #f9f9f9;}
    h1 {color:#2c3e50;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💪 BMI / TDEE 熱量建議系統")
st.caption("學校健康管理專題｜適用青少年")

with st.container():
    st.subheader("📥 基本資料輸入")
    height = st.number_input("身高（cm）", 100, 250, step=1)
    weight = st.number_input("體重（kg）", 30, 200, step=1)
    age = st.number_input("年齡", 10, 100, step=1)
    sex = st.radio("性別", ["男", "女"], horizontal=True)

st.divider()

if st.button("📊 開始分析", use_container_width=True):

    bmi = weight / (height / 100) ** 2

    if sex == "男":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    tdee = bmr * 1.375

    st.subheader("📈 計算結果")
    col1, col2 = st.columns(2)
    col1.metric("BMI", f"{bmi:.2f}")
    col2.metric("TDEE", f"{tdee:.0f} 大卡")

    # 判斷
    result_msg = ""
    level = "success"

    if sex == "女":
        if bmi >= 22.7:
            result_msg = f"體重偏高，建議便當熱量：{tdee*0.8:.0f} ~ {tdee*0.9:.0f} 大卡"
            level = "warning"
        else:
            result_msg = "體重屬正常或偏輕，以上便當皆推薦"

    else:
        if age == 15:
            low, normal, over = 18.2, 23.1, 25.5
        elif age == 16:
            low, normal, over = 18.6, 23.4, 25.6
        elif age == 17:
            low, normal, over = 19.0, 23.6, 25.6
        else:
            low, normal, over = 19.2, 23.7, 25.6

        if bmi < low:
            result_msg = "體重過輕，以上便當皆推薦"
        elif bmi < normal:
            result_msg = "體重標準，以上便當皆推薦"
        elif bmi < over:
            result_msg = f"體重過重，建議便當熱量：{tdee*0.8:.0f} ~ {tdee*0.9:.0f} 大卡"
            level = "warning"
        else:
            result_msg = f"肥胖，建議便當熱量：{tdee*0.8:.0f} ~ {tdee*0.9:.0f} 大卡"
            level = "error"

    if level == "success":
        st.success(result_msg)
    elif level == "warning":
        st.warning(result_msg)
    else:
        st.error(result_msg)

    st.info(
        """
        🔹 **減脂**：TDEE × 75%～80%  
        🔹 **增肌**：TDEE + 250～500  
        🔹 **增肌減脂**：TDEE ±100  

        ⚠ 成長期不建議過度減熱量  
        ⚠ 特殊體質不適用
        """
    )
