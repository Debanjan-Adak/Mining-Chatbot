# Define the Gradio UI layout
with gr.Blocks() as demo:
    gr.Markdown("# Mining Compliance AI", elem_id="centered-header")
    with gr.Row():
        with gr.Column(scale=1):  # Left-side column for Retrieved Documents
            docs_display = gr.Textbox(
                label="Retrieved Documents",
                placeholder="Relevant documents will appear here...",
                interactive=False
            )

        with gr.Column(scale=2):  # Right-side column for Chatbot
            compliance_chatbot = gr.Chatbot(
                elem_id="chatbot",
                label="Compliance Bot",
                type="messages",
                value=compliance_initial_history,  # Set initial history
                avatar_images=(
                    None,
                    "https://em-content.zobj.net/source/twitter/376/hugging-face_1f917.png",
                ),
            )
            compliance_prompt = gr.Textbox(
                max_lines=1,
                label="Chat Message",
                placeholder="Type your message here..."
            )

            # History variable to store chat history
            compliance_history = gr.State(compliance_initial_history)

            # Define the submit action for the chatbot
            compliance_prompt.submit(
                respond,
                inputs=[compliance_prompt, compliance_history],
                outputs=[compliance_chatbot, compliance_history, docs_display]
            )

# Launch the Gradio interface
demo.launch(debug=True)