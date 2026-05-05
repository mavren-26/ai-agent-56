import openai
#code 
openai.api_key = "YOUR_API_KEY"

def ai_plan():
    prompt = "Create a 1-day study plan for: " + ", ".join(subjects)
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    print("\n🤖 AI Study Plan:")
    print(response.choices[0].message.content)
