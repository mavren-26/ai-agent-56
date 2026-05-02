#AI Brain + Chat Agent
import openai

openai.api_key = "YOUR_API_KEY"

def chat_with_ai(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful study assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content