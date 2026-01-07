import os
from groq import Groq


class ChatBackend:
    """Backend handler for Groq API"""
    
    def __init__(self, api_key, model="llama-3.1-8b-instant"):
        """Initialize Groq client"""
        self.client = Groq(api_key=api_key)
        self.model = model
    
    def stream_response(self, messages, temperature=0.7, max_tokens=512):
        """Stream response from Groq"""
        try:
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
                    
        except Exception as e:
            yield f"Error: {str(e)}"
