import streamlit as st
import time

# הגדרות עיצוב בסיסיות
st.set_page_config(page_title="SafeSpace - page_icon="🛡️")


st.markdown("""
    <style>
    .stApp { direction: rtl; text-align: right; }
    </style>
    """, unsafe_allow_status=True)

st.title("🛡️ SafeSpace AI")
st.subheader


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": 
    ]


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

  
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
      
        assistant_response = 
        
      
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.1)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})


with st.sidebar:
    st.error(" ?")
    st.write("מוקד 105 (הגנה על ילדים)")
    st.write("ער\"ן: התקשרו 1201")
    if st.button("אני מרגיש בסכנה"):
        st.warning("אנא פנה למבוגר שאתה סומך עליו עכשיו.")
