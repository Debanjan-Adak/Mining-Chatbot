import gradio as gr

# Define initial setup for chatbot and history
compliance_initial_history = [
    {"role": "assistant", "content": "Welcome! I'm here to help with compliance questions."}
]

def respond(user_input, history):
    # Step 1: Retrieve relevant documents based on the user's input
    page_contents,contents_with_sources = search_docs(user_input) or "No relevant documents found."  # Ensure docs is a string

    # Step 2: Combine docs and the user input question
    input_text = f"{page_contents}\n\nQuestion: {user_input}"

    # Step 3: Generate a response using the combined input
    bot_response = generate_response(input_text) or "I'm sorry, I couldn't generate a response."  # Ensure response is a string

    # Step 4: Append the user's message and bot's response to the conversation history
    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": bot_response})

    # Return the updated history and the retrieved documents separately
    return history, history, contents_with_sources  # docs will be displayed in a separate textbox