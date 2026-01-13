import streamlit as st
import time

# הגדרות עיצוב בסיסיות
st.set_page_config(page_title="SafeSpace - מרחב בטוח", page_icon="🛡️")

# תיקון השגיאה: הגדרת RTL לעברית בצורה נכונה
st.markdown("""
    <style>
    .stApp { direction: rtl; text-align: right; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ SafeSpace AI")
st.subheader("אני כאן איתך. אפשר לדבר על הכל.")

# הודעת פתיחה של ה-AI
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "היי, אני כאן כדי להקשיב. אם עבר עליך יום קשה, אם יש חרם או סתם תחושה לא טובה - אני איתך. מה על הלב שלך?"}
    ]

# הצגת היסטוריית השיחה
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# קבלת קלט מהמשתמש
if prompt := st.chat_input("כתוב לי כאן..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        # תגובה זמנית עד שנחבר בינה מלאכותית חכמה יותר
        assistant_response = "אני שומע אותך וחשוב לי שתדע שאתה לא לבד. לספר למישהו זה צעד ראשון וגדול. תרצה לפרט קצת יותר מה קרה?"
        
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.1)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# תפריט עזרה דחופה
with st.sidebar:
    st.error("🆘 זקוק לעזרה מיידית?")
    st.write("מוקד 105 (הגנה על ילדים)")
    st.write("ער\"ן: התקשרו 1201")
   
