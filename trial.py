from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('HF_TOKEN')
print(f'Token loaded: {token[:10]}...')

client = InferenceClient(token=token)
print('Testing API...')
response = client.chat.completions.create(
    model='microsoft/Phi-3-mini-4k-instruct',
    messages=[{'role': 'user', 'content': 'hi'}],
    max_tokens=50
)
print('Success!')