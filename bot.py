import openai

# API Call
openai.api_key = ""

# ChatBot Response
def get_chatbot_response(prompt, conversation_history):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150,
            stop=["\n"],
            temperature=0.7,
            context=conversation_history
        )
        conversation_history.append(response.choices[0].text.strip())
        return response.choices[0].text.strip()
    
# Error Handling
    except Exception as e:
        print(f"Error occurred: {e}")
        return "Sorry, there was an error. Please try again later."

# Main loop
def main():
    prompt = "Welcome to Design Thinking Chatbot. How can I assist you today?"
    conversation_history = []

    while True:
        user_input = input("User: ")
        prompt += f"\nUser: {user_input}"
        conversation_history.append(f"User: {user_input}")
        response = get_chatbot_response(prompt, conversation_history)
        print("Chatbot:", response)

# Main Function
if __name__ == "__main__":
    main()
