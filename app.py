from st_on_hover_tabs import on_hover_tabs
import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface import ChatHuggingFace
# from googletrans import Translator
from google_trans_new import google_translator
import time
# import pyttsx3
import random

st.set_page_config(
    page_title="WiseWhisper",
    page_icon=":robot_face:",
    layout="wide",
        menu_items={
            'About': "# Under Construction"
        }
    )

huggingfacehub_api_token1 = st.secrets["huggingfacehub_api_token"] 
def main():
    with st.sidebar:
        # st.sidebar.title("Navigation")
        hide_st_style ='''
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            # header {visibility: hidden;}

            @media(hover: hover) and (min-width: 769px){

                section[data-testid='stSidebar'] {
                    height: 100%;
                    min-width:75px !important;
                    width: 75px !important;
                    transform:translateX(0px);
                    position: relative;
                    z-index: 1;
                    top: 0;
                    left: 0;
                    background-color: #111;
                    overflow-x: hidden;
                    transition: 0.5s ease;
                    padding-top: 60px;
                    white-space: nowrap;
                }

                section[data-testid='stSidebar']:hover{
                    min-width: 330px !important;
                    }

                button[kind="header"] {visibility: hidden;}

                div[data-testid="collapsedControl"]{
                    display: none;
                }
            }
            </style>
            '''
        st.markdown(hide_st_style, unsafe_allow_html=True)
        page = on_hover_tabs(tabName=['Dashboard', 'WiseWhisper-Bot', 'Privacy Policy'], 
                        iconName=['dashboard', 'chatbot', 'economy'], default_choice=0)

    if page == "Dashboard":
        with st.container(): 
            page_bg_img = '''
                <style>
                    
                [data-testid = "stAppViewContainer"] {
                background-image: url("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnMzNWx0OXdwOHlmbWpjaDQ2MTNuM2FubTVlNWNpcDB5dzZ4ejQxNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/FtS4s175Lex35edOfd/giphy.gif");
                background-size: cover;
                }
                [data-testid = "stHeader"] {
                
                background-color : rgba(0,0,0,0);
                }
                [data-testid = "stToolbar"] {
                right: 2rem;
                }            
                </style>

                '''
            st.markdown(page_bg_img, unsafe_allow_html=True)
            left_column, right_column = st.columns(2)
            with left_column:
                st.subheader("// WiseWhisper- Your Professional Indian Laywer")

                st.title("Introducing WiseWhisper🤖!!")

                st.subheader(':yellow[Your interactive gateway to Indian law. Explore legal rights, regulations, and responsibilities effortlessly. Unlock a world of Indian legal knowledge with ease and confidence. Ask, explore, and discover today. ]')
                st.write(":red[Select a page from the sidebar to get started.]")
                st.divider()
                
                st.divider()
                

            with right_column:
                with st.container():
                    st.write(" ")

    elif page == "WiseWhisper-Bot":
        page_bg_img = '''
            <style>
            [data-testid = "stAppViewContainer"] {
            background-image: url("https://cdn.dribbble.com/users/32512/screenshots/4888827/circle_story_by_gleb.gif");
            background-size: cover;
            }
            
            [data-testid = "stHeader"] {
            background-color : rgba(0,0,0,0);
            }

            [data-testid = "stToolbar"] {
            right: 2rem;         
            }
            </style>
            '''

        st.markdown(page_bg_img, unsafe_allow_html=True)

        st.title("Take Advice From Your Lawyer Now🤖...")
        st.divider()
        st.write(":red[The WiseWhisper is in early stages can generate wrong answers,Start Your Query By typing below.]")

        def error():
            error_messages = [
            "I'm sorry, I didn't quite catch that. Could you please rephrase?",
            "Hmm, I'm not sure what you mean. Could you provide more context?",
            "Sorry, I didn't understand. Could you please try again?",
            "Apologies, I'm having trouble understanding. Can you clarify?",
            "It seems there's an issue with your input. Please try again.",
            "Sorry, I'm unable to process that input. Please provide a different one."
            ]
            return random.choice(error_messages)

        def greet_text():
            messages = [
            "Hi there! How can I assist you today?",
            "Hello! Welcome to our platform. How can I help you?",
            "Hey! Great to see you here. What can I do for you?",
            "Hola!",
            "Hey there! Need any assistance?",
            "Yo! What's up? How can I assist you?",
            "Hello! How may I be of service to you?",
            "Hi! Welcome. How can I assist you today?",
            "Hey! Welcome back. What do you need help with?",
            "Hi there! How can I assist you with your queries?",
            "Hello! Need help with anything?",
            "Hi! How may I assist you today?",
            ]
            return random.choice(messages)

        def translator(c,option):
            # translator = Translator()
            translator = google_translator() 
            language_map = {
                "Hindi": 'hi',
                "Punjabi": 'pa',
                "Telgu": 'te',
                "Tamil": 'ta',
                "Gujarati": 'gu'
            }
            if option in language_map:
                choice = language_map[option]
            # translated_text = translator.translate(c, dest=choice)
            translate_text = translator.translate(c,lang_tgt=choice) 
            return translated_text.text
        
        # def talk(g):
        #     engine = pyttsx3.init()
        #     newVoiceRate = 145
        #     engine.setProperty('rate',newVoiceRate)
        #     engine.say(g)
        #     engine.runAndWait()

        def model(question):
            llm = HuggingFaceEndpoint(
            repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            task="text-generation",
            max_new_tokens=250,
            do_sample=False,
            temperature=0.5,
            repetition_penalty=1.03,
            huggingfacehub_api_token=huggingfacehub_api_token1,
            )
            from langchain_core.messages import (
                HumanMessage,
                SystemMessage,
            )
            messages = [
                SystemMessage(
                    content="You are an Indian legal professional, and your answers should be considered as legal advice. You provide personalized legal advice on questions related to Indian fundamental rights. If a question is asked that is not related to Indian legal advice, respond with 'Sorry, I can only provide legal advice related to Indian fundamental rights.' Answers must be short and accurate, strictly related to the topic."
                ),
                HumanMessage(
                    content=question
                ),
            ]

            chat_model = ChatHuggingFace(llm=llm)
            res = chat_model.invoke(messages)
            return res.content
    
        def greet():
            for word in greet_text():
                yield word
                time.sleep(0.05)

        question = st.chat_input("Say something")

        left_column, right_column = st.columns([2, 1.3])
        with left_column:
            st.subheader("Query")
            messages = st.container(height=300)
            if question:
                if question.lower() in ["hi", "hy", "yo", "hello", "how are you", "hola", "heya", "hey"]:
                    messages.chat_message("user").write("You: " + question)
                    text1 = greet()
                    messages.chat_message("assistant").write(text1)
                    # talk(text1)

                elif len(question.split()) < 5:
                    text1 = error()
                    messages.chat_message("assistant").write(text1)
                    # talk(text1)

                else:
                    messages.chat_message("user").write("You: " + question)
                    text1 = model(question)
                    messages.chat_message("assistant").write(text1)
                    # talk(text1)

        # Right column (Select Language and Translation)
        with right_column:
            ll,rr = st.columns([2,1])
            with ll:
                st.subheader("Translated")
            messages1 = st.container(height=300)
            with rr:
                option = st.selectbox(
                    "Select Language",
                    ("Hindi", "Punjabi", "Gujarati", "Telugu", "Tamil")
                )

            if question:
                translated_text = translator(str(text1), option)
                messages1.chat_message("assistant").write(translated_text)

        
if __name__ == "__main__":
    main()
