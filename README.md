# Conversational AI Voice Assistant (Audio Interface)

## Overview
The **Conversational AI Voice Assistant** is a speech-enabled AI system built with **LangChain** and **OpenAI's GPT-3.5**. It integrates **Speech Recognition** and **Text-to-Speech** capabilities, allowing users to interact with the AI using natural language voice commands.

The project demonstrates the integration of conversational AI with audio interfaces, providing an engaging, human-like interaction experience. The system processes voice input, uses a Large Language Model (LLM) for conversational responses, and outputs the response via speech synthesis.

## Technologies Used
- **LangChain**: Framework for creating conversational AI with large language models
- **OpenAI GPT-3.5**: For generating responses in natural language
- **SpeechRecognition**: For capturing voice input from the user
- **pyttsx3**: For converting AI text responses into speech
- **Python**: Programming language used to implement the assistant

## Features
- **Speech Recognition**: The assistant listens for audio commands via the microphone and converts speech to text.
- **Conversational AI**: The assistant uses **LangChain** and **GPT-3.5** to generate relevant and engaging responses.
- **Text-to-Speech**: The assistant replies to the user in a conversational tone using **pyttsx3**.

## How It Works
1. **Listening**: The assistant listens for a user's voice command via a microphone.
2. **Processing**: The captured voice input is converted into text using **SpeechRecognition**.
3. **Response Generation**: The text input is sent to the **GPT-3.5 model** using **LangChain**, where it is processed, and a response is generated based on the user's query.
4. **Speech Output**: The response is converted back to speech using **pyttsx3** and played to the user.

## Running the Project
### Prerequisites
1. Python 3.x
2. Install required libraries:
   ```bash
   pip install openai langchain SpeechRecognition pyttsx3 python-dotenv
   ```
3. Set up your **OpenAI API key** in a `.env` file:
   ```env
   OPENAI_API_KEY=your-api-key-here
   ```

### How to Run
1. Clone the repository and navigate to the project directory.
2. Run the Python script to start the assistant:
   ```bash
   python ai_friend.py
   ```
3. The assistant will begin listening for voice commands.

## Example
When asked, "What's the weather today?" the assistant might respond with, "The weather is sunny and 25°C today."

## Future Improvements
- Cloud Deployment: Integrating this project with **Google Cloud** for scalability and deployment.
- Multi-language Support: Adding support for multiple languages using **Speech-to-Text** APIs.
- Expanded Conversations: Adding more advanced conversation capabilities, such as topic switching and memory.
