# ai_friend.py

import os
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

# Load environment variables
load_dotenv()
OPENAI_API_KEY="*******"
# Initialize the Large Language Model (GPT-3.5 Turbo)
llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=1,
    model_name="gpt-3.5-turbo"
)

# Create a prompt template
template = """
You are a friendly chatbot with a great sense of humor. Keep responses concise and ask interesting questions. Be entertaining and engaging.
"""

# Initialize speech recognition
recognizer = sr.Recognizer()

# Initialize text-to-speech enginesk-QNyDe1E2E15yywTNOCW8T3BlbkFJsUAeHmQCSl4uKGcH2zgC
engine = pyttsx3.init()

def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for a command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        return None

def main():
    print("Welcome to your AI friend! Say something:")
    while True:
        user_input = listen_for_command()
        if user_input:
            # Prompt the language model
            response = llm.generate_response(template, user_input)
            print(f"AI friend: {response}")

            # Convert text response to speech
            engine.say(response)
            engine.runAndWait()

if __name__ == "__main__":
    main()
