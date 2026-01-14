import streamlit as st
import openai

# עיצוב בסיסי
st.set_page_config(page_title="SafeSpace AI", page_icon="🛡️")
st.markdown("<style>.stApp { direction: rtl; text-align: right; }</style>", unsafe_allow_html=True)

st.title("SafeSpace AI 🛡️")
st.subheader("אני כאן איתך. אפשר לדבר על הכל.")

# בדיקה אם יש מפתח סודי (API Key)
if "OPENAI_API_KEY" not in st.secrets:
    st.error("חסר מפתח API! נא להוסיף אותו ב-Settings של Streamlit.")
    st.stop()

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "היי, אני כאן להקשיב. מה על הלב שלך?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# כאן קורה הקסם - ה-AI עונה
if prompt := st.chat_input("כתוב לי כאן..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # פנייה לבינה המלאכותית
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "אתה עוזר אמפתי ותומך לנפגעי חרם ואלימות. תענה בעברית חמה ומחזקת."},
                *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            ]
        )
        answer = response.choices[0].message.content
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
