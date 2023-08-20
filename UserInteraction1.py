#User Interaction - Chatbot Interface using Hugging Face's Transformers:
from transformers import pipeline

chatbot = pipeline("conversational")

print("Bot: Hello! I'm here to help you with fashion recommendations. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    response = chatbot("User: " + user_input)[0]['generated_text']
    print("Bot:", response.strip())
