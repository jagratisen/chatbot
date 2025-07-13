# Step 1: Predefined responses
chatbot_responses = {
    "What is the total revenue of Apple?": "Apple's total revenue in 2023 was $383.29 billion.",
    "What is the net income of Microsoft?": "Microsoft's net income in 2023 was $72.36 billion.",
    "How has Tesla's revenue changed from 2021 to 2023?": "Tesla's revenue increased from $53.82 billion in 2021 to $96.77 billion in 2023.",
    "What are the total assets of Apple in 2023?": "Apple's total assets in 2023 were $352.58 billion.",
    "What is the operating cash flow of Tesla?": "Tesla's operating cash flow in 2023 was $13.57 billion."
}

# Step 2: Chatbot function using input()
def simple_chatbot():
    print(" Welcome to the Financial Chatbot!")
    print("Type one of the predefined questions or type 'exit' to quit.\n")

    for question in chatbot_responses:
        print(f"🔹 {question}")

    while True:
        user_input = input("\n You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif user_input in chatbot_responses:
            print(" Bot:", chatbot_responses[user_input])
        else:
            print(" Bot: Sorry, I can only respond to predefined questions.")

# Step 3: Run the chatbot
simple_chatbot()