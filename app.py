import streamlit as st
st.set_page_config(page_title="Social Media Addiction Predictor")
st.title("📱 Social Media Addiction Predictor")
st.write("Fill in your details to check your addiction level.")
education = st.selectbox(
    "Your Education Level:",
    ["Undergraduate","Above Undergraduate","Below Undergraduate"]
)
area = st.selectbox(
    "Your Area:",
    ["Municipal Urban", "Metropolitan", "Rural"]
)
num_social_media = st.selectbox(
    "Number of Social Media Apps You Use:",
    [1, 2, 3, 4, 5]
)
hours_used = st.slider(
    "Daily Hours Spent on Social Media:",
    min_value=0,
    max_value=7,
    value=1
)
if st.button("Predict Addiction Level"):
     if hours_used >= 6 or (num_social_media>4 and hours_used in [3,4,5]):
        st.error("🚨 **Highly Addicted** — Very high usage and multiple apps.")
     elif 2 <= hours_used <= 6:
        st.warning("⚠️ **Moderately Addicted** — Noticeable usage pattern.")
     else:
        st.success("✅ **Not Addicted** — Usage seems normal.")
        
     st.subheader("🔍 Your Input Data")
     st.write(f"**Education:** {education}")
     st.write(f"**Area:** {area}")
     st.write(f"**Number of Social Media Apps:** {num_social_media}")
     st.write(f"**Daily Hours Used:** {hours_used} hours")


