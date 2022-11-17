import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

subject = "tea"

prompt = f"Generate branding snippet for {subject}"

response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=100)

print(response)