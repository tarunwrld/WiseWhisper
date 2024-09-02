from st_on_hover_tabs import on_hover_tabs
import streamlit as st
import google.generativeai as genai
from googletrans import Translator
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

                st.subheader('Your interactive gateway to Indian law. Explore legal rights, regulations, and responsibilities effortlessly. Unlock a world of Indian legal knowledge with ease and confidence. Ask, explore, and discover today.')
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
            background-image: url("https://www.1900law.com/wp-content/uploads/mastheadimg-scale-1024x500.jpg");
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
            translator = Translator(service_urls=['translate.googleapis.com']) 
            language_map = {
                "Hindi": 'hi',
                "Punjabi": 'pa',
                "Telgu": 'te',
                "Tamil": 'ta',
                "Gujarati": 'gu'
            }
            if option in language_map:
                choice = language_map[option]
            translated_text = translator.translate(c, dest=choice)
            return translated_text.text
        
        # def talk(g):
        #     engine = pyttsx3.init()
        #     newVoiceRate = 145
        #     engine.setProperty('rate',newVoiceRate)
        #     engine.say(g)
        #     engine.runAndWait()

        def model(question):
            genai.configure(api_key=st.secrets["GENAI_KEY"])
            model = genai.GenerativeModel(
                "models/gemini-1.5-flash",
                system_instruction="You are an Indian Lawyer. You help people with Indian law queries. You don't answer any other questions that are not related to Indian queries.",
            )
            
            response = model.generate_content(
                question,
                generation_config=genai.types.GenerationConfig(
                    candidate_count=1,
                    stop_sequences=["x"],
                    max_output_tokens=500,
                    temperature=1.0,
                    stream=True
                ),
            )

           if hasattr(response, 'text'):
               for chunk in response:
                   if hasattr(chunk, 'text'):
                       return chunk.text
                    return "No valid chunk found"
            else:
                return "No content found"

            # client = InferenceClient()
            # messages = [
            #     {
            #         "role": "user",
            #         "content": question,
            #     },
            #     {
            #         "role": "assistant",
            #         "content": """
            #             Act like you are a Legal Indian Lawyer. 
            #             As a legal Indian lawyer, your primary focus is to provide legal advice and solutions to your clients queries related to Indian law. 
            #             You don't know anything except Indian law. 
            #             If a question is not related to Indian law, You will politely decline to provide an answer.
            #             You will not provide answer that hurts someone belief,
            #             Your answer will be genuine and will not cause chaos or disruption,
            #             If a question is related to Mathematics,Physics,Chemistry,English,Biology,Coding,Arts,Music,Dance,Technology etc that are not related to Indian Law then You will politely decline to provide an answer.
            #             """ 
            #     },
            # ]
            # response = client.chat_completion(
            #     messages=messages,
            #     tool_choice="auto",
            #     temperature=1e-2,
            #     max_tokens=350,
            #     top_p=0.95,
            #     seed=42,
            # )
            
            # # Extracting the response content
            # assistant_response = response.choices[0].message.content
            
            # return assistant_response
            
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
                translated_text = translator(text1, option)
                messages1.chat_message("assistant").write(translated_text)

        
if __name__ == "__main__":
    main()
