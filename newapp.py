import streamlit as st
import google.generativeai as ai

st.title("😊📖Sandeep Chatbot😊📖")

if st.checkbox("Hallo Everyone Good Morning, Do you want to Ask any question from Chatbot"):

    my_key = "AIzaSyDP7YqjNzwWr5rm7ZJUGnQo_jvv5y6GoVY"
    ai.configure(api_key=my_key)
    model = ai.GenerativeModel("gemini-2.0-flash")
    chat = model.start_chat()

    msg = st.text_area("Ask your question:-")

    if st.button("Send to AI"):
        user_msg = msg.strip().lower()
        developer_keywords = [
    "who built", "who made", "who created", "developer","develop" "creator", "maker", 
    "banaya kisne", "kisne banaya", "who programmed", "created by", "developed you",
    "developer name", "Sandeep ji ne tumhe banaya", "who coded you",
    "tumhe kisne banaya", "tumhara developer kaun hai", 
    "Sandeep ji ne hi banaya", "kya Sandeep ji ne banaya", "kisi aur ne banaya",
    "did Sandeep ji build you", "Sandeep created you", "are you built by Sandeep ji",
    "tumhe Sandeep ji ne banaya ya kisi aur ne","tumhe kisne program kiya hai","kya tumhe Sandeep ji ne hi banaya hai","who is the developer of",
    "kisne is chatbot ko develop kiya","kya tumhe Sandeep ji ne develop kiya hai ""developer kaun",
    "mere developer Sandeep ji hai"," Chatbot developer kaun hai","chatbot developer Sandeep ji hai",
    "tumhara kya kaam hai",
]  
        purpose_keywords = [
            "kis liye", "kis kaam ke liye", "kaam kya", "what is your purpose", 
            "why were you made", "why did Sandeep ji create", "what do you do", 
            "tumhara kaam kya", "why Sandeep ji made you", "Sandeep ji ne kis work ke liye tumhe banaya",
            "tumhara kaam kya hai",
        ]

        if any(k in user_msg for k in purpose_keywords):
            answer = "Sandeep ji ne mujhe banaya hai taki main logo ki help kar Saku."
        elif any(k in user_msg for k in developer_keywords):
            answer = "Mujhe Sandeep ji ne banaya hai 😊🙏"
        else:
            result = chat.send_message(msg)
            answer = result.text

        st.markdown("**Sandeep Chatbots Response:**")
        st.write(answer)
