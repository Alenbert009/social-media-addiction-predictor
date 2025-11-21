import streamlit as st
import pandas as pd
import numpy as np
import joblib
model = joblib.load("final_model.pkl")
scaler = joblib.load("scaler.pkl")
st.set_page_config(page_title="Social Media Harassment Prediction")
st.title("📱 Social Media Harassment Prediction")
st.write("Fill in your details to check your addiction level.")
column_names = [
    'How many hours per day you use social media?',
    'When you are online, at how many social media you remain active:',
    '1. Has anyone ever told you offensive dirty stories or jokes using social media? ',
    '2. Has anyone ever tried to get you to talk about personal sexual things using social media? ',
    '3. Has anyone ever said offensive things about how you look, your body, or your sex life using social media?',
    "4. Has anyone using social media ever tried to have a romantic or sexual relationship even though you tried to let him know you didn't want to? ",
    '5. Has anyone using social media ever kept asking you to meet or go on a date even after you said “no”?',
    '6. Has anyone using social media ever made dirty remarks about women in general (for example saying that all women are whores)?',
    '7. Has anyone ever called you a lesbian or a “dyke” on social media?',
    '8. Has anyone using social media ever sent you  offensive “dirty” videos and/or images?',
    '9. Has anyone ever left a sexual comment or posted a picture of you in using social media?',
    '10. Has anyone ever tried to get you to watch him on a messenger or chat box?',
    '11. Has anyone ever tried to get you to have virtual sex over any social media which have instant messaging facility?',
    '12. Has anyone ever sent you spam that advertised for pornographic Websites using social media?',
    '13. Has anyone ever sent you pop-ups with links to pornographic Web sites?',
    '14. Has anyone ever   left an offensive “dirty” comment on the wall of social media?',
    '15. Has anyone ever sent messages that refer to or ask about your body, sex life, or intimate subjects through social media (for example asking if you are on your period right now))?',
    '16. Has anyone ever threaten to hack your computer/mobile and cause damage if you did not conduct the sexual act requested for (for example describing giving the person oral sex)?',
    '17. Has anyone ever sent frightening message through social to get you to perform sexual acts (for example cyber-sex)?',
    '18. Has anyone ever bribed you for conducting sexual acts (for example offering to send you money if you send him/her sexual obscene pictures)?',
    '19. Using Social Media, has anyone ever sexually harassed you?',
    'Facebook',
    'Instagram',
    'Twitter',
    'Whatsapp',
    'Others',
]
user_input = []
st.write("### 🔹 For harassment-related questions:")
st.write("Use: **0 = Never, 1 = Sometimes, 2 = Once or twice**")
for col in column_names:
    if col in ["Facebook", "Instagram", "Twitter", "Whatsapp","Others"]:
        value = st.selectbox(col,[0,1],format_func=lambda x:['No','Yes'][x])
    elif col == "How many hours per day you use social media?":
        hours = st.slider(col, 0.0, 7.0, 1.0, step=0.5)
        value=hours
    elif col == "When you are online, at how many social media you remain active:":
        value = st.slider(col, 0, 5, 1)
    else:
        value=st.selectbox(col,[0, 1, 2],format_func=lambda x:['Never','Sometimes','Once or Twice'][x])
    user_input.append(value)
final_input=np.array(user_input).reshape(1,-1)
scaled_input=scaler.transform(final_input)

if st.button("Predict Addiction Level"):
     prediction = model.predict(scaled_input)[0]
     if hours>6:
         prediction=2
     if prediction == 1:
        st.warning("⚠️ **Moderately Harassed** — Noticeable usage pattern.")
     elif prediction == 2:
        st.error("🚨 **Highly Harassed** — Very high usage and multiple apps.")
     elif prediction == 3:
        st.info("✅ **Not Harassed** — Usage seems normal.")  



