import streamlit as st
import time

# הגדרות עיצוב בסיסיות
st.set_page_config(page_title="SafeSpace - מרחב בטוח", page_icon="🛡️")

# הוספת עיצוב RTL (מימין לשמאל) לעברית
st.markdown("""
    <style>
    .stApp { direction: rtl; text-align: right; }
    </style>
    """, unsafe_allow_status=True)

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
    # הצגת הודעת המשתמש
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # יצירת תגובה מה-AI (סימולציה של אמפתיה)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # כאן בעתיד נחבר את ה-API של OpenAI. כרגע נשתמש בתגובה תומכת לדוגמה:
        assistant_response = "אני שומע כמה זה קשה לך. חשוב שתדע שאתה לא לבד בזה. בא לך לשתף אותי בעוד פרטים על מה שקרה?"
        
        # אפקט כתיבה
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.1)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# תפריט עזרה דחופה בצד
with st.sidebar:
    st.error("🆘 זקוק לעזרה מיידית?")
    st.write("מוקד 105 (הגנה על ילדים)")
    st.write("ער\"ן: התקשרו 1201")
    if st.button("אני מרגיש בסכנה"):
        st.warning("אנא פנה למבוגר שאתה סומך עליו עכשיו.")
