import streamlit as st
import google.generativeai as ai
import speech_recognition as sr

st.title("chat with AI...")

key = 'AIzaSyDhyEoqisuwYrOFOx7dCqGyWj2vKrPE_vM'

ai.configure(api_key=key)

model= ai.GenerativeModel(model_name="gemini-3.1-flash-lite-preview")

question=st.chat_input('Ask me anythin...', accept_audio=True)

if question:
    with st.chat_message('human'):
      if question.text:
        st.write(question.text)

      if question.audio:
         transcribed_text= transcribe_audio(question.audio)
         st.write(transcribed_text)
         finel_porpmt = question.text + transcribed_text
         
      else:
         finel_porpmt=question.text

      porpmt=f"""
          Answer this question:{question.text}
          Given that:
    
      
        1. Web Development:
           - Focus: Building websites (Front-end & Back-end).
           - Best for: People who want fast results, like visual design, or want to start freelancing quickly.
           - Difficulty: Easy to start.

        2. Cybersecurity:
           - Focus: Protecting systems, ethical hacking, and network security.
           - Best for: People who love puzzles, logical thinking, and have high patience.
           - Difficulty: Moderate (requires networking knowledge).

        3. Machine Learning:
           - Focus: AI models, data analysis, and predictive algorithms.
           - Best for: People strong in Math (Calculus/Statistics) and who enjoy working with data.
           - Difficulty: Hard (academic-heavy).
        """

    prompt_template = f"""
        You are a Tech Career Advisor. Use the following data to help the user:
        

        User Question: {finel_porpmt}

        Answer the user's question based ONLY on the data above. If they ask about choosing a track, give them a recommendation based on their interests and answer simply.
        """
        
    finel_porpmt = prompt_template
 

    with st.chat_message('ai'):
        with st.spinner('Loading...'):
         answer = model.generate_content(finel_porpmt)
        st.write(answer.text)

def transcribe_audio(file):
   listener=sr.Recognizer()
   with sr.AudioFile(file) as audio:
      recording=listener.record(audio)
      text=listener.recognize_google(recording, language='en-US')
      return text