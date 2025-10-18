from openai import OpenAI 

client = OpenAI("YOUR_API_KEY")

prompt = ""

while True: 
    prompt = input("You: ")
    chat_completions = client.chat.completions.create(
        [
            {
                "role": "user",
                "content": prompt
            }
        ]
        model = "gpt-4o-mini"
    ),

    chat_response = chat_completions.choice[0].message.content
    print("AI: ",chat_response)

