# TDA Chatbot Fullstack

A clean Streamlit chatbot demonstrating:
- Frontend/Backend separation
- Streamlit streaming with st.write_stream()
- Groq API integration for fast, free LLM access
- Real-time response streaming

## Quick Start

### 1. Navigate to Project

bash
cd ~/Desktop/TDA_chatbot_fullstack


### 2. Setup Virtual Environment

bash
# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate


### 3. Install Dependencies

bash
pip install -r requirements.txt


### 4. Get Groq API Key

1. Go to https://console.groq.com/keys
2. Sign up (free)
3. Click "Create API Key"
4. Copy your token (starts with gsk_)

### 5. Configure Environment

bash
# Create .env file
cp .env.example .env

# Edit and add your token
nano .env


Add this line to .env:

GROQ_API_KEY=gsk_your_actual_token_here


### 6. Run the App

bash
streamlit run app.py


Visit http://localhost:8501

## Project Structure

TDA_chatbot_fullstack/
├── backend.py          # Groq API logic (Business layer)
├── app.py             # Streamlit UI (Presentation layer)
├── requirements.txt   # Python dependencies
├── .env              # API keys (create from .env.example)
├── .env.example      # Template for environment variables
└── README.md         # This file


## Architecture

### Backend (backend.py)

- ChatBackend class: Handles Groq API calls
- stream_response(): Generator that yields tokens in real-time
- Clean separation of business logic
- Easy to test independently

### Frontend (app.py)

- Streamlit UI: Simple chat interface with sidebar
- st.write_stream(): Displays tokens with typewriter effect
- Session state: Maintains conversation history
- Sidebar controls: Model selection, temperature, clear chat

## Features

- Real-time streaming responses
- Multiple model options
- Temperature control for response creativity
- Chat history management
- Clean frontend/backend separation
- Free tier friendly (Groq API)

## Available Models

1. llama-3.1-8b-instant - Fast, efficient (Default)
2. llama-3.3-70b-versatile - More powerful, higher quality
3. mixtral-8x7b-32768 - Large context window

## Technical Details

### Streaming Implementation

python
# Generator yields tokens as they arrive
def stream_response(self, messages, temperature, max_tokens):
    stream = self.client.chat.completions.create(
        model=self.model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=True
    )
    
    for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content


### Session State Management

python
if 'messages' not in st.session_state:
    st.session_state.messages = []


## Customization

### Change Default Model

Edit backend.py:

python
def __init__(self, api_key, model="llama-3.1-8b-instant"):


### Adjust Default Temperature

Edit app.py:

python
temperature = st.slider("Temperature", 0.0, 1.0, 0.7)  # Change 0.7


### Add More Models

Edit app.py:

python
model = st.selectbox("Model", [
    "llama-3.1-8b-instant",
    "llama-3.3-70b-versatile",
    "mixtral-8x7b-32768",
    "your-new-model-here"
])


## Troubleshooting

### Issue: "Please add API key in sidebar"
- Fix: Add your Groq API key in the sidebar
- Get a free key at https://console.groq.com/keys

### Issue: Rate limit errors
- Fix: Groq free tier allows 30 requests/minute
- Wait a minute and try again

### Issue: Import errors
- Fix: Make sure you installed all dependencies
- Run: pip install -r requirements.txt

### Issue: Module not found
- Fix: Activate your virtual environment
- Run: source .venv/bin/activate

## Dependencies

- streamlit >= 1.46.0
- groq >= 0.4.0
- python-dotenv >= 1.0.0

## Resources

- Streamlit Documentation: https://docs.streamlit.io
- Groq API Documentation: https://console.groq.com/docs
- Streamlit Chat Tutorial: https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps

## Next Steps

Potential extensions:
- Add conversation export/import
- Implement conversation branching
- Add document upload for context
- Deploy to Streamlit Cloud
- Add user authentication
- Implement conversation search

## License

MIT License - Free to use for learning and teaching

---

Built for teaching Streamlit streaming and LLM API integration
